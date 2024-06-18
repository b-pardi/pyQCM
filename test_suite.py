import unittest
import pandas as pd
import numpy as np
import os
import sys
import re
from unittest.mock import patch, MagicMock, mock_open

# Assuming the script provided is in a file named `data_formatter.py`
from format_file import (
    open_df_from_file, extract_num_from_string, rename_cols,
    add_offsets, unnormalize, dissipation_magnitude_adjustment,
    format_QCM_next, format_QCMi, format_Qsense, format_AWSensors,
    check_file_previously_formatted, format_raw_data
)

class TestDataFormatter(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_csv_data = "Frequency,Dissipation\n1,0.1\n2,0.2\n3,0.3\n"
        self.sample_txt_data = "Frequency\tDissipation\n1\t0.1\n2\t0.2\n3\t0.3\n"
        self.sample_df = pd.DataFrame({
            'Frequency': [1, 2, 3],
            'Dissipation': [0.1, 0.2, 0.3]
        })
        self.cols_dict = {'Frequency': 'fundamental_freq', 'Dissipation': 'fundamental_dis'}

    @patch('builtins.open', new_callable=mock_open, read_data="Frequency,Dissipation\n1,0.1\n2,0.2\n3,0.3\n")
    @patch('pandas.read_csv')
    def test_open_df_from_file_csv(self, mock_read_csv, mock_file):
        mock_read_csv.return_value = self.sample_df
        df = open_df_from_file('test.csv')
        pd.testing.assert_frame_equal(df, self.sample_df)

    @patch('builtins.open', new_callable=mock_open, read_data="Frequency\tDissipation\n1\t0.1\n2\t0.2\n3\t0.3\n")
    @patch('pandas.read_csv')
    def test_open_df_from_file_txt(self, mock_read_csv, mock_file):
        mock_read_csv.return_value = self.sample_df
        df = open_df_from_file('test.txt')
        pd.testing.assert_frame_equal(df, self.sample_df)

    def test_extract_num_from_string(self):
        self.assertEqual(extract_num_from_string('fundamental_freq'), 1)
        self.assertEqual(extract_num_from_string('3rd_freq'), 3)
        self.assertEqual(extract_num_from_string('5th_freq'), 5)

    def test_rename_cols(self):
        df = pd.DataFrame({
            'Frequency': [1, 2, 3],
            'Dissipation': [0.1, 0.2, 0.3]
        })
        expected_df = pd.DataFrame({
            'fundamental_freq': [1, 2, 3],
            'fundamental_dis': [0.1, 0.2, 0.3]
        })
        renamed_df = rename_cols(df, self.cols_dict)
        pd.testing.assert_frame_equal(renamed_df, expected_df)

    def test_add_offsets(self):
        calibration_df = pd.DataFrame({
            'fundamental_freq': [0.5],
            'fundamental_dis': [0.05]
        })
        fmt_df = pd.DataFrame({
            'fundamental_freq': [1, 2, 3],
            'fundamental_dis': [0.1, 0.2, 0.3]
        })
        expected_df = pd.DataFrame({
            'fundamental_freq': [1.5, 2.5, 3.5],
            'fundamental_dis': [0.15, 0.25, 0.35]
        })
        result_df = add_offsets(calibration_df, fmt_df)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_unnormalize(self):
        df = pd.DataFrame({
            'fundamental_freq': [1, 2, 3],
            '3rd_freq': [0.33, 0.66, 0.99]
        })
        expected_df = pd.DataFrame({
            'fundamental_freq': [1, 2, 3],
            '3rd_freq': [1, 2, 3]
        })
        result_df = unnormalize(df)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_dissipation_magnitude_adjustment(self):
        df = pd.DataFrame({
            'fundamental_dis': [1, 2, 3],
            '3rd_dis': [0.1, 0.2, 0.3]
        })
        expected_df = pd.DataFrame({
            'fundamental_dis': [1e-6, 2e-6, 3e-6],
            '3rd_dis': [1e-7, 2e-7, 3e-7]
        })
        result_df = dissipation_magnitude_adjustment(df)
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch('data_formatter.rename_cols')
    def test_format_QCM_next(self, mock_rename_cols):
        df = self.sample_df
        mock_rename_cols.return_value = df
        result_df = format_QCM_next(df)
        mock_rename_cols.assert_called_once_with(df, {
            'Time':'abs_time', 'Relative_time':'Time',
            'Frequency_0':'fundamental_freq', 'Dissipation_0':'fundamental_dis',
            'Frequency_1':'3rd_freq', 'Dissipation_1':'3rd_dis',
            'Frequency_2':'5th_freq', 'Dissipation_2':'5th_dis',
            'Frequency_3':'7th_freq', 'Dissipation_3':'7th_dis',
            'Frequency_4':'9th_freq', 'Dissipation_4':'9th_dis',
            'Frequency_5':'11th_freq', 'Dissipation_5':'11th_dis',
            'Frequency_6':'13th_freq', 'Dissipation_6':'13th_dis',
            'Temperature':'Temp'
        })
        pd.testing.assert_frame_equal(result_df, df)

    @patch('data_formatter.rename_cols')
    def test_format_QCMi(self, mock_rename_cols):
        df = self.sample_df
        mock_rename_cols.return_value = df
        result_df = format_QCMi(df)
        mock_rename_cols.assert_called_once_with(df, {
            'Channel A QCM Time [sec]':'Time',
            'Channel A Fundamental Frequency [Hz]':'fundamental_freq','Channel A Fundamental Dissipation [ ]':'fundamental_dis',
            'Channel A 3. Overtone [Hz]':'3rd_freq', 'Channel A 3. Dissipation  [ ]':'3rd_dis',
            'Channel A 5. Overtone [Hz]':'5th_freq', 'Channel A 5. Dissipation  [ ]':'5th_dis',
            'Channel A 7. Overtone [Hz]':'7th_freq', 'Channel A 7. Dissipation  [ ]':'7th_dis',
            'Channel A 9. Overtone [Hz]':'9th_freq', 'Channel A 9. Dissipation  [ ]':'9th_dis',
            'Channel A 11. Overtone [Hz]':'11th_freq', 'Channel A 11. Dissipation  [ ]':'11th_dis',
            'Channel A 13. Overtone [Hz]':'13th_freq', 'Channel A 13. Dissipation  [ ]':'13th_dis',
            'Channel A Temp [Celsius]':'Temp'
        })
        pd.testing.assert_frame_equal(result_df, df)

    @patch('data_formatter.rename_cols')
    @patch('data_formatter.dissipation_magnitude_adjustment')
    @patch('data_formatter.unnormalize')
    @patch('data_formatter.add_offsets')
    def test_format_Qsense(self, mock_add_offsets, mock_unnormalize, mock_dissipation_magnitude_adjustment, mock_rename_cols):
        df = self.sample_df
        mock_rename_cols.return_value = df
        mock_dissipation_magnitude_adjustment.return_value = df
        mock_unnormalize.return_value = df
        mock_add_offsets.return_value = df
        calibration_df = pd.DataFrame({'fundamental_freq': [0.5], 'fundamental_dis': [0.05]})
        result_df = format_Qsense(df, calibration_df)
        mock_rename_cols.assert_called_once_with(df, {
            'Time_1':'Time',
            'F_1:1':'fundamental_freq', 'D_1:1':'fundamental_dis',
            'F_1:3':'3rd_freq', 'D_1:3':'3rd_dis',
            'F_1:5':'5th_freq', 'D_1:5':'5th_dis',
            'F_1:7':'7th_freq', 'D_1:7':'7th_dis',
            'F_1:9':'9th_freq', 'D_1:9':'9th_dis',
            'F_1:11':'11th_freq', 'D_1:11':'11th_dis',
            'F_1:13':'13th_freq', 'D_1:13':'13th_dis',
            'Meas. Temp. Time':'Temp_Time', 'Tact':'Temp'
        })
        mock_dissipation_magnitude_adjustment.assert_called_once_with(df)
        mock_unnormalize.assert_called_once_with(df)
        mock_add_offsets.assert_called_once_with(calibration_df, df)
        pd.testing.assert_frame_equal(result_df, df)

    @patch('data_formatter.rename_cols')
    @patch('data_formatter.dissipation_magnitude_adjustment')
    @patch('data_formatter.unnormalize')
    @patch('data_formatter.add_offsets')
    def test_format_AWSensors(self, mock_add_offsets, mock_unnormalize, mock_dissipation_magnitude_adjustment, mock_rename_cols):
        df = self.sample_df
        mock_rename_cols.return_value = df
        mock_dissipation_magnitude_adjustment.return_value = df
        mock_unnormalize.return_value = df
        mock_add_offsets.return_value = df
        calibration_df = pd.DataFrame({'fundamental_freq': [0.5], 'fundamental_dis': [0.05]})
        result_df = format_AWSensors(df, calibration_df)
        mock_rename_cols.assert_called_once_with(df, {
            'Time_(s)':'Time',
            'Delta_F/n_n=3_(Hz)':'3rd_freq', 'Delta_D_n=3_()':'3rd_dis',
            'Delta_F/n_n=5_(Hz)':'5th_freq', 'Delta_D_n=5_()':'5th_dis',
            'Delta_F/n_n=7_(Hz)':'7th_freq', 'Delta_D_n=7_()':'7th_dis',
            'Delta_F/n_n=9_(Hz)':'9th_freq', 'Delta_D_n=9_()':'9th_dis',
            'Delta_F/n_n=11_(Hz)':'11th_freq', 'Delta_D_n=11_()':'11th_dis'
        })
        mock_dissipation_magnitude_adjustment.assert_called_once_with(df)
        mock_unnormalize.assert_called_once_with(df)
        mock_add_offsets.assert_called_once_with(calibration_df, df)
        pd.testing.assert_frame_equal(result_df, df)

    @patch('data_formatter.Exceptions')
    def test_check_file_previously_formatted(self, mock_exceptions):
        df = pd.DataFrame({'fundamental_freq': [1, 2, 3]})
        ext = '.csv'
        result = check_file_previously_formatted(df, ext)
        self.assertTrue(result)
        mock_exceptions.warning_popup.assert_called_once()

    @patch('data_formatter.open_df_from_file')
    @patch('data_formatter.check_file_previously_formatted')
    @patch('data_formatter.format_QCM_next')
    @patch('data_formatter.format_QCMi')
    @patch('data_formatter.format_Qsense')
    @patch('data_formatter.format_AWSensors')
    def test_format_raw_data(self, mock_format_AWSensors, mock_format_Qsense, mock_format_QCMi, mock_format_QCM_next, mock_check_file_previously_formatted, mock_open_df_from_file):
        data_file = 'test_data/test.csv'
        mock_open_df_from_file.return_value = self.sample_df
        mock_check_file_previously_formatted.return_value = False
        mock_format_AWSensors.return_value = self.sample_df
        format_raw_data('AWSensors', data_file, False)
        mock_open_df_from_file.assert_called_with(data_file)
        mock_check_file_previously_formatted.assert_called_with(self.sample_df, '.csv')
        mock_format_AWSensors.assert_called_once()

if __name__ == '__main__':
    unittest.main()
