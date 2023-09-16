### MAIN README
# Please execute 'install_packages.py' BEFORE running this script.
- Import errors may occur otherwise
# when done with program, please click 'Exit' button instead of closing window.
- Can cause terminal to freeze sometimes if just closing windows.

## File Information

- To select the data file to analyze, simply click the select data file button.
    - This will open your machine's file explorer window to select the file.
    - By default it will show the 'raw_data' folder in the program directory, however you can select a file anywhere on your computer.
- Once file is selected, specify which of the 3 supported apparatuses your data came from.
    - The program will convert the data file to a consistent format used by the remainder of program's execution.
    - **Do Not** alter the column names of the data file the experimental device outputs, as the formatting routine relies on the default output the device for reformatting.
    - Once formatting is done, there will be a file saved in the raw_data directory that the software will read.
    - **Do Not** alter this file either.
    - Support will be added in future releases for users to add new experimental devices to be formatted.
- Depending on which source selected, there will be a prompt to either enter absolute or relative baseline time.
- Next is to specify theoretical or calibration values for calculations in the modeling section.
    - If user selectes theoretical, it will use theoretical peak frequency values and theoretical C (-17.7) for Sauerbrey model.
    - If user selects calibration, there is the prompt to either:
        - copy/paste calibration values into 'calibration_data' folder
        - into a file 'COPY-PASTE_CALIBRATION_DATA_HERE.csv'
    - OR:
        - click a button and enter the values into the software directly
- Once all information is entered, user can then click 'Submit File Information'.
- **Please Note** if you are using Qsense and do not have the calibration values for your experiment, you are limited to just visualization, no modeling features will work correctly due to the nature of how Qsense only records the change in frequency, not the actual values

## Plot Customization
- At the bottom of the data file column, there is a 'customize plot options button'.
- Here you can specify the following:
    - Font type.
    - Various font sizes.
    - Tick direction.
    - Scale of time
    - Saved figure file format.
    - Index of points to plot.
        - i.e. every 5th point.
    - Bounds of axis for visualization plots
        - Time bounds are in units that are selected for time scale above
        - Frequency bounds are in terms of DELTA f, not f
        - Dissipation bounds are (your number) E-6
    - Colors of each overtone.
- When selections are confirmed, they are saved for all future executions of the program.
- There is also the option to load default values.
- If selections are confirmed and there are entries not selected, values previously saved will be used

## Overtone Selections
- The middle 2 columns offer the user to plot the raw data for any overtone desire, as well as the shifted (baseline corrected) data.
- Please note that all plot options and modeling features require shifted data, raw data's only purpose is visualization, it is not used for anything other than just being plotted.

## Plot options
- Users have the following options for plots beyond basic visualization:
    - Multiaxis plot for change in frequency and change in dissipation together against time.
    - Normalize change in frequency for all data with their respective overtones
        - Note, all plots in this section are normalized when selecting this, however interactive plot and all modeling plots will NOT be normalized unless the model dictates so.
        - all plots that are normalized will indicate on the y axis reading (Df/n).
        - i.e. thin film in air model is normalized avg change in frequency of each overtone against the overtone number squared.
    - Plotting change in dissipation against change in frequency.
    - Plotting temperature against time.
    - Slope correction.
        - Takes the shifted data 1 step further.
        - Finds slope of baseline time range, and 'rotates' all points by that amount
        - will ensure slope of baseline is ~0
    - Interactive plot (further detailed below).
    - Modeling/further analysis (further detailed below).
    - Change the scale of time on the x axis for ALL plots.
        - seconds (default), minutes, hours.
    - Change the format of image plots are saved in.
        - png (default), tiff, pdf.

## Modeling Window
- Modeling Window is only relevant if the interactive plot is selected.
- Visit this window AFTER submitting when the interactive plot opens up.
- Before making your selection of data in the interactive plot, enter the range that is being selected in the entry field and click confirm.
    - The name of the range is arbitrary and can be called whatever the user desires, it will be used for identifying that selection's data in modeling sections, and be used for plot titles and file names.
- Once you have entered a name for range being selected, and made the selection in the interactive plot (detailed below), input and confirm the next range before making more selections.
    - The latest selection for each range will be saved. So if the user enters in 'baseline' for the range, then makes a selection, if another selection is done before inputting and confirming the next range, that first baseline selection will be overwritten.
     - i.e. if you select data for range 'x' in file 'data1.csv', but a selection for that was already made and data is already there, even if there are other ranges in the file, only data for range 'x' file 'data1.csv' will be overwritten, and data for range 'y' in 'data1.csv' and range 'x' in 'data2.csv' will remain untouched.
    - This means that the user is not committed to a selection once it's been made, as adjustments can be made.
- Once all selections made, the user can choose from any of the available modeling/further analysis options to execute on the selected data.
- These plots are saved to qcmd-plots/modeling.
- Remember to click the 'Clear Saved Range Data' when moving to a new experiment to remove all old selections.

## Interactive Plot
- When checking the interactive plot box, an entry field appears to enter which overtone you would like to visulize in the plot.
    - Note that the overtone you select to visualize does not effect the output of any plots or analysis, as the software acts on selections made in the plot to ALL overtones in that range.
- For whichever overtone is to be analyzed in the interactive plot, ensure that that overtone is selected in the baseline corrected data section as well, as it relies on the cleaned data processing done there.
- Selections are made by clicking and dragging anywhere in either of the left 2 plots, OR inputting the x values into the text field above in the form of XMIN,XMAX and hitting enter.
- Selected range is zoomed in and displayed in right side of figure, and all calculations on the selections are save into csv files in the 'selected_ranges' folder.
- A linear regression will be done on the zoomed data as well to indicate the drift.
- note, if you normalized your data via one of the options being selected, this data will NOT be normalized for the sake of modeling functions used after.
- if you opted to correct the slope however, this option WILL be applied.

## Errors
- Errors will be displayed in the terminal running the scripts.
- Caught exceptions will have notes about what went wrong and how correct it. These exceptions are generally a user error.
    - If there is an error that is uncaught, it is likely a bug, or an exception that was missed.
    - Please attempt to reproduce the error and explicitly outline the steps taken to do so and report them to the developer along with the traceback (what is output in the terminal when error occurs).

## Bugs
# Determining a Bug
- If you catch an error or something runs but it gives an unexpected output, here are the steps to generate a bug report:
1. Check the README.md and ensure steps were followed correctly.
2. Check the terminal and see if this exception was caught.
    - if there is an exception with a message describing how it happened and how to remedy, the error is caught.
        - Example of caught error:
        - Exceptions.ShapeMismatchException: SHAPE MISMATCH ERROR CAUGHT: ERROR: Different number of overtones selected in UI than found in stats file
        Dims must be equal, found (7,) and (5,)
        - Example of uncaught error:
        - ValueError: invalid literal for int() with base 10: ''
3. Attempt to replicate steps and ensure the bug is reproducible.
4. If the caught error and/or README don't solve the error, this bug needs to be reported.

# Reporting the Bug
- In the bug report, include the following:
1. Date, your name, email, and university/team you are a part of
2. Criticality of bug:
    - 1: Cosmetic issues i.e. mispelling in UI or wrong color in plot for given overtone.
    - 2: Terminal outputted an error, but software output was as expected.
    - 3: Specific function had error or was incorrect, but other facets were correct and software still runs.
    - 4: Software crashes entirely or is essentially unusable giving all desired outputs incorrectly.
    - Please also describe why you chose that criticality rating
3. Name of code editor using
    - Spyder, VSCode, atom, command prompt, etc.
4. Desired goal/end result
5. Describe the steps taken from the beginning of software's execution til when the bug occured (again these should be reproducible).
    - **Please Be explicit and pedantic** any steps that are not listed will be assumed to be skipped/glossed over/not entered
    - note that the last step entered should be the one that caused the bug to occur
6. Copy/paste the Traceback of the program's failure (if there was a Traceback outputted into the terminal)
    - a Traceback is essentially everything the terminal outputs when an error is found during execution (it will be prefaced with the word 'Traceback')
    - example Traceback:
    ~~~
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Brandon\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "C:\Users\Brandon\Documents\00 School Files 00\University\Mechano Biology Research\bratadio\main.py", line 805, in submit
    input.clean_interactive_plot_overtone = int(self.interactive_plot_overtone_select.get())
ValueError: invalid literal for int() with base 10: ''
    ~~~
7. Output of software if output is incorrect (and if there even was an output), and data file(s) used
    - sent as attachments


## IF USING SPYDER
- By default, plt will show plots in console box and span selector will not work.
- Follow these steps to make selection plots open in new window:
    Tools > Preferences > IPython console > Graphics > Graphics Backend > Apply & OK.


--------------------------------------------------------------


