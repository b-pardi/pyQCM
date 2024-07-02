import pytest
from PIL import Image, ImageChops
import sys
import os

''' Note to reviewers
As this is my first big project, I know I handled ui/backend interaction in a less than optimal way,
If I could start this project over I would change a lot,
So for now please forgive my subpar coding practices in this early project of mine
'''

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.analyze import analyze_data
from src.format_file import format_raw_data
from main import Input

QCMI_FP = "sample_generations/qcmi-bsa-after/QSM-I-BSA_1mgpml.csv"
QSENSE_FP = "sample_generations/qsense-bsa-after/BSA.1mgml-1.280723-unprotected.xlsx"

img_exts = ['.png', '.tiff', '.pdf']

# filenames of plots that should generate in testing
plot_filenames = [
    'dissipation_plot.png',
    'frequency_plot.png',
    'RAW-dissipation-plot.png',
    'RAW-resonant-freq-plot.png',
    'freq_dis_V_time.png',
    'temp_vs_time_plot.png'
]

def copy_file(src_fp, dest_fp):
    try:
        with open(src_fp, 'rb') as src_file:
            with open(dest_fp, 'wb') as dest_file:
                dest_file.write(src_file.read())
    except IOError as e:
        print(f"Unable to copy file. {e}")

def clear_plots(plot_dir):
    for existing_plot_fn in os.listdir(plot_dir):
        fp = os.path.join(plot_dir, existing_plot_fn)
        if os.path.isfile(fp) and any(existing_plot_fn.endswith(ext) for ext in img_exts):
            os.remove(fp)

def clear_data_files(data_dir):
    # List all files in the directory
    files = os.listdir(data_dir)
    
    # Loop through the files
    for file_name in files:
        # Check if the file contains the substring
        if 'Formatted-' in file_name:
            # Construct the full file path
            file_path = os.path.join(data_dir, file_name)
            
            # Remove the file
            os.remove(file_path)
            print(f"Removed file: {file_path}")


def plots_are_similar(sample_plot, generated_plot, thresh=0.01):
    sample_img = Image.open(sample_plot).convert('RGB')
    generated_img = Image.open(generated_plot).convert('RGB')
    
    diff = list(ImageChops.difference(sample_img, generated_img).getdata())
    num_diff_pixels = sum(sum(rgb_pixel) for rgb_pixel in diff)
    percent_diff = num_diff_pixels / (sample_img.size[0] * sample_img.size[1] * 3 * 255)
    print(percent_diff)

    return percent_diff < thresh

@pytest.fixture
def init_qcmi_input_data():
    # simulating user input with these class instantiations
    qcmi_input = Input()
    qcmi_input.file = "sample_generations/qcmi-bsa-after/QSM-I-BSA_1mgpml.csv"
    qcmi_input.will_plot_raw_data = True
    qcmi_input.will_plot_clean_data = True
    qcmi_input.is_relative_time = True
    qcmi_input.rel_t0 = 10 # beginning of baseline time
    qcmi_input.rel_tf = 100 # end of baseline time
    qcmi_input.will_plot_temp_v_time = True
    qcmi_input.will_plot_dF_dD_together = True # indicates if user selected multi axis plot of dis and freq
    qcmi_input.file_src_type = 'QCM-i' # different machines output data differently
    for key in qcmi_input.which_plot['raw'].keys():
        qcmi_input.which_plot['raw'][key] = True
        qcmi_input.which_plot['clean'][key] = True

    plot_dir = os.path.join(os.getcwd(), 'qcmd-plots/')
    data_dir = os.path.join(os.getcwd(), 'raw_data/')
    clear_plots(plot_dir)
    clear_data_files(data_dir)
    yield plot_dir, qcmi_input
    clear_plots(plot_dir)
    clear_data_files(data_dir)

@pytest.fixture
def init_qsense_input_data():
    # simulating user input with these class instantiations
    qsense_input = Input()
    qsense_input.file = "sample_generations/qsense-bsa-after/BSA.1mgml-1.280723-unprotected.xlsx"
    qsense_input.will_plot_raw_data = True
    qsense_input.will_plot_clean_data = True
    qsense_input.is_relative_time = True
    qsense_input.rel_t0 = 10 # beginning of baseline time
    qsense_input.rel_tf = 100 # end of baseline time
    qsense_input.will_plot_temp_v_time = True
    qsense_input.will_plot_dF_dD_together = True # indicates if user selected multi axis plot of dis and freq
    qsense_input.file_src_type = 'Qsense' # different machines output data differently
    for key in qsense_input.which_plot['raw'].keys():
        if not key.__contains__('fundamental'):
            qsense_input.which_plot['raw'][key] = True
            qsense_input.which_plot['clean'][key] = True

    plot_dir = os.path.join(os.getcwd(), 'qcmd-plots/')
    data_dir = os.path.join(os.getcwd(), 'raw_data/')
    clear_plots(plot_dir)
    clear_data_files(data_dir)
    yield plot_dir, qsense_input
    clear_plots(plot_dir)
    clear_data_files(data_dir)

def test_qcmi_plots(init_qcmi_input_data):
    # ensure plot dir clear before running
    plot_dir, qcmi_input = init_qcmi_input_data

    # copy the formatted file from sample_generations to directory that analyze data reads files from
    copy_file("sample_generations/qcmi-bsa-after/Formatted-QSM-I-BSA_1mgpml.csv", "raw_data/Formatted-QSM-I-BSA_1mgpml.csv")

    analyze_data(qcmi_input)

    # check if plots generated
    dir_files = os.listdir(plot_dir)
    missing_files = [file for file in plot_filenames if file not in dir_files]
    assert len(missing_files) == 0, f"missing plots: {missing_files}"

    # check if plots match the sample generations
    for file in dir_files:
        if any(file.endswith(ext) for ext in img_exts):
            sample_file = os.path.join('sample_generations/qcmi-bsa-after/', file)
            generated_file = os.path.join('qcmd-plots/', file)
            print(sample_file,generated_file)
            assert plots_are_similar(sample_file, generated_file)

def test_qsense_plots(init_qsense_input_data):
    # ensure plot dir clear before running
    plot_dir, qsense_input = init_qsense_input_data

    # copy the formatted file from sample_generations to directory that analyze data reads files from
    copy_file("sample_generations/qsense-bsa-after/Formatted-BSA.1mgml-1.280723-unprotected.csv", "raw_data/Formatted-BSA.1mgml-1.280723-unprotected.csv")

    analyze_data(qsense_input)

    # check if plots generated
    dir_files = os.listdir(plot_dir)
    missing_files = [file for file in plot_filenames if file not in dir_files]
    assert len(missing_files) == 0, f"missing plots: {missing_files}"

    # check if plots match the sample generations
    for file in dir_files:
        if any(file.endswith(ext) for ext in img_exts):
            sample_file = os.path.join('sample_generations/qsense-bsa-after/', file)
            generated_file = os.path.join('qcmd-plots/', file)
            print(sample_file,generated_file)
            assert plots_are_similar(sample_file, generated_file)

if __name__ == '__main__':
    pytest.main()