'''
THIS SCRIPT IS A WORK IN PROGRESS PLEASE DO NOT RUN YET IT WILL FAIL
'''

import pytest
from unittest.mock import patch
import pandas as pd
import numpy as np
import sys
import os
import tkinter as tk
from tkinter import ttk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from main import App, Col1, Col2, Col3, Col4

@pytest.fixture
def app():
    app = App()
    app.update()  # Process any pending events
    yield app
    print("Tests are done, closing the app...")
    app.quit()
    app.update_idletasks()
    app.destroy()

def test_ui_spawns(app):
    # Ensure title is correct
    assert app.title() == "BraTaDio - pyQCM-D Analyzer"
        
    # Check if random intvar is correctly initialized
    assert isinstance(app.int_plot_data_fmt_var, tk.IntVar)
    assert app.int_plot_data_fmt_var.get() == -1
    
    # Check if main container frame exists
    container = app.nametowidget(app.children['!frame'])
    assert isinstance(container, tk.Frame)

    # Check if the scrollbars exist and are configured correctly
    assert isinstance(app.scrollbarX, ttk.Scrollbar)
    assert str(app.scrollbarX.cget('orient')) == 'horizontal'
    assert isinstance(app.scrollbarY, ttk.Scrollbar)
    assert str(app.scrollbarY.cget('orient')) == 'vertical'

    
    # Check if Col1 is correctly initialized
    col1 = app.frames[Col1]
    assert isinstance(col1, Col1)
    assert col1.is_visible == True
    assert col1.col_position == 0
    assert col1.filename_label.cget('text') == "Data file"

    # Check btn of Col1
    assert hasattr(col1, 'browse_files_button')
    assert isinstance(col1.browse_files_button, tk.Button)
    assert col1.browse_files_button.cget('text') == "Select data file"

    # Simulate button click and check the file dialog
    with patch('tkinter.filedialog.askopenfilename', return_value="test_file.txt"):
        col1.browse_files_button.invoke()
        col1.update()
        assert col1.filename_label.cget('text').__contains__("test_file.txt")
    
    # Check if Col2 is correctly initialized
    col2 = app.frames[Col2]
    assert isinstance(col2, Col2)
    assert col2.is_visible == True
    assert col2.col_position == 1
    assert col2.file_name_label.cget('text') == "Enter Data File Information"
    
    # Check if Col3 is correctly initialized
    col3 = app.frames[Col3]
    assert isinstance(col3, Col3)
    assert col3.is_visible == True
    assert col3.col_position == 2
    assert col3.label.cget('text') == "Col3 Label"
    
    # Check if Col4 is correctly initialized
    col4 = app.frames[Col4]
    assert isinstance(col4, Col4)
    assert col4.is_visible == True
    assert col4.col_position == 3
    assert col4.label.cget('text') == "Col4 Label"

if __name__ == "__main__":
    pytest.main()