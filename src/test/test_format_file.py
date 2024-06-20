import pytest
import pandas as pd
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.format_file import freqs, disps, open_df_from_file, add_offsets, unnormalize, dissipation_magnitude_adjustment, format_QCMi, format_Qsense

# Sample DataFrames for testing
calibration_df = pd.DataFrame({ # df that's added to main data df
    'fundamental_freq': [0.1],
    'fundamental_dis': [0.01],
    '3rd_freq': [0.5],
    '3rd_dis': [0.05]
}
)
base_df = pd.DataFrame({ # main data df
    'Time': [0, 1, 2],
    'fundamental_freq': [100, 101, 102],
    'fundamental_dis': [0.1, 0.1, 0.1],
    '3rd_freq': [200, 201, 202],
    '3rd_dis': [0.2, 0.2, 0.2],
    'Temp': [25, 25, 25]
})

offsets_expected_df = pd.DataFrame({ # res of calibration_df + base_df
        'Time': [0, 1, 2],
        'fundamental_freq': [100.1, 101.1, 102.1],
        'fundamental_dis': [0.11, 0.11, 0.11],
        '3rd_freq': [200.5, 201.5, 202.5],
        '3rd_dis': [0.25, 0.25, 0.25],
        'Temp': [25, 25, 25]
})

# mults data of each overtone by its overtone num. so freq_3 will be base_df[freq_3] * 3
unnormalize_expected_df = pd.DataFrame({ 
    'Time': [0, 1, 2],
    'fundamental_freq': [100, 101, 102],
    'fundamental_dis': [0.1, 0.1, 0.1],
    '3rd_freq': [600, 603, 606],
    '3rd_dis': [0.2, 0.2, 0.2],
    'Temp': [25, 25, 25]
})

# multiplies dissipation data by 1e-6 to adjusted its order of magnitude
magnitude_adjusted_expected_df = pd.DataFrame({
        'Time': [0, 1, 2],
        'fundamental_freq': [100, 101, 102],
        'fundamental_dis': [0.1e-6, 0.1e-6, 0.1e-6],  # Adjusted by 1e-6
        '3rd_freq': [200, 201, 202],
        '3rd_dis': [0.2e-6, 0.2e-6, 0.2e-6],  # Adjusted by 1e-6
        'Temp': [25, 25, 25]
})

@pytest.mark.parametrize("fp, fmt_func", [
    ("sample_generations/qcmi-bsa-after/QSM-I-BSA_1mgpml.csv", format_QCMi),  # csv file of qcmi data
    ("sample_generations/qsense-bsa-after/BSA.1mgml-1.280723-unprotected.xlsx", format_Qsense)  # excel exported qsense file
])
def test_basic_reading(fp, fmt_func):
    df = open_df_from_file(fp)
    assert isinstance(df, pd.DataFrame)

    # check n rows and col headers to verify formatting
    fmt_df = fmt_func(df)
    assert df.shape[0] == fmt_df.shape[0]

    cols = ['Time']
    for i in range(len(freqs)):
        cols.append(freqs[i])
        cols.append(disps[i])
    cols.append('Temp')
    print(cols, list(fmt_df.columns))
    are_cols_matching = all(elem in list(fmt_df.columns) for elem in cols)
    assert are_cols_matching == True

def test_qsense_file_formatting():
    # verify numerical formatting steps individually with dummy data
    # testing add offsets
    offsets_res_df = add_offsets(calibration_df, base_df.copy())
    pd.testing.assert_frame_equal(offsets_res_df, offsets_expected_df)

    # testing unnormalization
    unnormalize_res_df = unnormalize(base_df.copy())
    pd.testing.assert_frame_equal(unnormalize_res_df, unnormalize_expected_df)

    # testing magnitude adjustment
    magnitude_res_df = dissipation_magnitude_adjustment(base_df.copy())
    pd.testing.assert_frame_equal(magnitude_res_df, magnitude_adjusted_expected_df)
    print("Passed!")

def test_qsd_reading():
    qsd_fp = "sample_generations/qsense-bsa-after/BSA.1mgml-1.280723_QSD.qsd"
    qsd_df = open_df_from_file(qsd_fp)
    assert isinstance(qsd_df, pd.DataFrame)

if __name__ == "__main__":
    pytest.main()