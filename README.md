
# py-QCM-BraTaDio README

  

## Important Notes before Starting

### Please execute 'install_packages.py' BEFORE running this script
- Import errors may occur otherwise.

### This software was designed and tested in a WINDOWS environment
- If using Mac, please be aware that issues may occur

### When done with program, please click 'Exit' button instead of closing window
- Can cause terminal to freeze sometimes if just closing windows.

### 'sample_generations' folder contains sample data to test with software, as well as figures output by that sample data

### IF USING SPYDER

- By default, plt will show plots in console box and span selector will not work.
- Follow these steps to make selection plots open in new window:
Tools > Preferences > IPython console > Graphics > Graphics Backend > Apply & OK.

![Figure 1 - pyQCM-BraTaDio UI for reference](https://iili.io/J7rm8Wg.png)
### Figure 1 - pyQCM-BraTaDio UI for reference
(1) Initialization conditions, (2) selection of frequencies and dissipation for data mining, visualization, and modeling, (3) interactive plotting options for data range selection, and (4) selection of plotting options and modeling.

## File Information (1)
- To select the data file to analyze, simply click the select data file button.
- This will open your machine's file explorer window to select the file.
- By default it will show the 'raw_data' folder in the program directory, however you can select a file anywhere on your computer.
- Once file is selected, specify which of the 4 supported experimental devices your data came from.
	- These devices include Open QCM-Next, QCM-I, QSense, and AWSensors
	- The program will convert the data file to a consistent format used by the remainder of program's execution.
	-  **Do Not** alter the column names of the data file the experimental device outputs, as the formatting routine relies on the default output the device for reformatting.
	- Once formatting is done, there will be a file saved in the raw_data directory that the software will read, prepending 'Formatted-' to the original name of your data file.
	-  **Do Not** alter this file either.
- Depending on which source selected, there will be a prompt to either enter absolute or relative baseline time.
	- This refers to the equilibrium time used to shift the data by.
	- For testing purposes, it is appropriate to enter 0-100 (in seconds) as a sample baseline time.
	- In practice, this should be the last x number of seconds where the frequency is stable before the experiment begins.
- Next is to specify theoretical or calibration values for calculations in the modeling section.
	- If user selects theoretical, it will use theoretical peak frequency values and theoretical mass sensitivity constant, C = -17.7 ng/(Hz*cm^2) for Sauerbrey model.
	- If user selects calibration, there is the prompt to either:
		- Copy/paste offset values into a file 'offset_data/COPY-PASTE_CALIBRATION_DATA_HERE.csv'
			- There are populated values in this value already for demonstrative purposes.
		- OR click a button 'Enter values here' and enter the values into the software directly
- **Once all information is entered, user can then click 'Submit File Information'.**

- **NOTE** if you are using QSense or AWSensors and do not have the calibration values for your experiment, you are limited to just visualization, no modeling features will work correctly due to the nature of how QSense only records the change in frequency, not the actual values.
- **NOTE** if you are using QCM-I or Open QCM-Next, upon selecting 'offset' a label popups up to notify you that entering these values is unnecessary, as these devices record information that QSense and AWSensors do not, so the offset is found computationally.

  

## Plot Customization (1.1)

- At the bottom of the data file column, there is a 'customize plot options button', Here you can specify the following:
	- Font type.
	- Various font sizes.
	- Tick direction.
	- Scale of time
	- Saved figure file format.
	- Saved figure DPI (Dots Per Inch)
		- This corresponds to quality, default is 200
	- Index of points to plot.
		- i.e. every 5th point.
	- Bounds of axis for visualization plots
		- Time bounds are in units that are selected for time scale above
		- Frequency bounds are in terms of DELTA f, not f
		- Dissipation bounds are (your number) * E-6
	- Colors of each overtone.
- When selections are confirmed, they are saved for all future executions of the program.
- There is also the option to load default values.
- If selections are confirmed and there are entries not selected, values previously saved will be used.
  

## Overtone Selections (2)

- The middle 2 columns offer the user to plot the raw data for any overtone desired, as well as the reference level adjusted data.
- In addition to selecting the overtones this is also where you select to plot the interactive plot, either for raw or reference level adjusted data.
	- Interactive plot details in later section
- **NOTE** all plot options and modeling features require reference level adjusted data, raw data's only purpose is visualization, it is not used for anything other than just being plotted.
  

## Plot options (4)
![Figure 2 - various plot options provided by pyQCM-BraTaDio](https://iili.io/J7434Rf.png)
### Figure 2 - various plot options provided by pyQCM-BraTaDio

- Users have the following options for plots beyond basic visualization:
	- Change in frequency as a function of time (plotted by default), Figure 2a.
	- Normalized change in frequency as a function of time, Figure 2b.
	- Change in Dissipation as a function of time (plotted by default), Figure 2c.
	- Multi-axis change in frequency and dissipation as a function of time, Figure 2d.
	- Multi-axis normalized change in frequency and dissipation as a function of time, Figure 2e.
	- Temperature as a function of time, Figure 2f.
	- Change in dissipation as a function of change in frequency, Figure 2g.
	- Change in dissipation as a function of normalized change in frequency, Figure 2h.
	
		- **NOTE**, when selecting normalization, all plots in this section are normalized, however interactive plot and all modeling plots will NOT be normalized unless the model dictates so.
		- All plots that are normalized will indicate on the y axis reading (Df/n).

- Additional options include:
	- Drift correction.
			- Finds slope (drift) of baseline, and rotates all points by the amount required to flatten the baseline.
	- Interactive plot (further detailed below).
	- Modeling/further analysis (further detailed below).  

## Interactive Plot (3)

![Figure 3.1 - UI prompting for interactive plot](https://iili.io/J74fOoQ.png)
### Figure 3.1 - UI prompting for interactive plot
Activating the interactive plot option requires to select an overtone and assign a label or identifier for data mining.

- When checking the interactive plot box, an entry field appears to enter which overtone you would like to visualize in the plot. Enter the number of the overtone to display the data for in the plot.

	- **NOTE** that the overtone you select to visualize does not effect the output of any plots or analysis, as the software acts on selections made in the plot to ALL overtones in that range.
	- We visualize just 1 overtone in this plot to make it look cleaner and give the user and easier time making selections.
	- For whichever overtone is to be analyzed in the interactive plot, ensure that that overtone is selected in the baseline corrected data section as well, as it relies on the cleaned data processing done there.
- Before making any selections, make sure you have selected a range identifier.
	- This identifier typically will correspond to what was done in the experiment to produce the specific range of data to be selected.
	- However, the identifier is arbitrary, and is for your reference. The software uses this later when saving calculations and displaying plots for your reference.
	- Once the identifier is entered, click 'Confirm range' to update the software of the identifier for the data you are about to select.
	-  **NOTE** selections will overwrite data of the same identifier, but will NOT overwrite selections from different identifiers.
	- i.e. if you select data for range 'x' in file 'data1.csv', but a selection for that was already made and data is already there, even if there are other ranges in the file, only data for range 'x' file 'data1.csv' will be overwritten, and data for range 'y' in 'data1.csv' and range 'x' in 'data2.csv' will remain untouched.
	- This means if you make an erroneous selection, you can simply make another one and correct it, and you can also make multiple selections from the same data using different identifiers for each selection.

![Figure 3 - Interactive plot](https://iili.io/J743rHG.png)
### Figure 3.2 - Interactive plot
(a) Input line for time range selection, (b) change in frequency interactive plot, (c) zoomed-in region from the change in frequency interactive plot and frequency drift, (d) change in dissipation interactive plot, and (e) zoomed-in region from the change in dissipation interactive plot and dissipation drift.

- Selections are made by clicking and dragging anywhere in plots (b) or (d), or inputting the x values into the text field above (a) in the form of XMIN,XMAX and hitting enter.
	- All 3 of these are grouped. i.e. if you make a selection in one, it'll update the other two with that selection
- Selected range is zoomed in and displayed in right side of figure (c) and (e), and all basic statistical calculations on the selections are save into csv files in the 'selected_ranges' folder.
- A linear regression will be done on the zoomed data as well to indicate the drift.
- **NOTE**, if you normalized your data via one of the options being selected, this data will NOT be normalized for the sake of modeling functions used after.
	- if you opted to correct the slope however, this option WILL be applied.


## Modelling Window (4)

### Modeling Window is only relevant if the interactive plot is selected and selections have been made *ex ante*.
- Once all desired selections in the interactive plot are made, the user can choose from any of the available modelling/further analysis options to apply models to the selected data, by clicking the 'Modelling' button.
- Available model application options include:
	- Plotting average delta f and delta D of each overtone.
	- Sauerbrey mass.
	- Thin film in liquid.
	- Thin film in air.
	- Crystal Thickness.
		- Contrary to above model applications, crystal thickness relies on offset data, not interactive plot selections. 
- All models except crystal thickness rely on selectiong in the interactive plot.
- These plots are saved to qcmd-plots/modeling.

 - **NOTE** while you can make multiple selections from multiple data files and have them all saved without overwriting, it is *highly* recommended to 'Clear saved range data' between experiments, as the modelling functions will not work correctly across multiple files.  

## Errors

- Known errors (originating from erroneous user input) will be displayed in a popup window when encountered
- The software does not close when this occurs, and the user is able to correct the error and resume processing.

## Bugs

### Determining a Bug

- If you catch an error or something runs but it gives an unexpected output, here are the steps to generate a bug report:

1. Check the README.md and ensure steps were followed correctly.

2. Check the terminal or error popup (if applicable) and see if this exception was caught.

3. Attempt to replicate steps and ensure the bug is reproducible.

4. If the caught error and/or README don't solve the error, this bug needs to be reported.

  

## Reporting the Bug
If you are proficient with github, please open an issue in the repository.
For those who are not, there is an included 'BraTaDio_example_bug_report.docx' in the repository. This can be filled out and emailed to the developer. **Please Be explicit and pedantic** 

 ----------------------------------------------------------
