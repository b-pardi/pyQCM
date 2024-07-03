### WIP

bug fixes:

format changes:
- matplotlib, use font family, not fontname
- for input altered flag, prompt user with warning message

features:

optimizations/refactoring: 
- remove latex features
- refactor analyze() to put each opt into its own function

waiting on data: 
- thin film in air data to test accuracy of corresponding model
- full gordon-kanazawa data

### CHANGE LOG

7/3
- added FAQ to readme

7/2
- Small fmt changes to paper
- Moved credit.txt to actual paper
- fixed issue when clicking X on toolbar to close window it would crash
- added to readme regarding font types in plot customization
- fixed test_analyze
    - formatted file was not being put in raw_data directory
    - When testing this code, formatted files were already in there so they passed
    - now sample generations' formatted files are copied to raw_data directory where analyze_data reads files from, and clears them out after
- added demo video to readme
- changed default font to sans serif
- ensure that in analyze testing, default plot options are set so that fonts and font sizes don't skew plot differences
- updated sample generations to be plotted with the new default values for accurate comparison in testing
- fixed bug where if preformatted file exists is selected by user and is not in raw_data directory it cannot find the file
- fixed bug where window to open figures folder would open new window each time

6/24
- added author credits file: credit.txt
- removed equal contribution author

6/20
- added an orcid to paper
- changed int plot options of ui so opts just appear in col4 instead of in col 2 and 3 below overtones
- added popup msg box to indicate plots have been generated
- added same popup box to modelling plots
    - refactored modelling class to not be instantiated in main app class
    - instead of calling analysis function directly, model btns call class funcs that wrap the modelling functions in a try-except
- changed number only entries to spin boxes
    - validation functions to check if integer entered
    - entries requiring overtone numbers have validation cmds to check if odd number 1-13
- program no longer closes if invalid file entered, just shows err msg

6/19
- added rowcon and colcon to ui col frames to set weights to fill empty space
- added tests for reading qsense and qcmi data
    - test if files can be read in df
    - test if files can be read and formatted accordingly
    - test if qsd files can be read
- added tests for plot generation for qsense and qcmi data
    - given sample qcmi input test if plots are generated
    - test if plots are within < 1% difference of those in sample generation
- more documentation updating
- cited python packages in paper
- updated file structure
- automated ui test code checking
    - ui opened
    - intvar init correctly
    - main container exists
    - scrollbars exist
    - all columns initialized
    - browse file button works
    - col 2 and 3 drop overtone checkboxes when top checkbox clicked
    - modelling window opens when button clicked

6/18
- added to readme:
    - statement of need
    - more detailed installation instr
    - other minor details
- added error checking to ensure baseline time range given was large enough to find frequency and dissipation data for an average
- removed drift correction
- removed deprecated files

4/24
- fixed bug where multiaxis and dissipation v frequency would only plot last selected overtone

4/10
- fixed bug where (only for 1 specific dataset) when using Sauerbrey mass analysis it loaded the interactive plot output stats file data as strings???
    - ensured a typecast of data loaded from that file

2/11
- adjusted warning label for missing data to show if >0.1% of entries missing, and notify of what overtones data is missing

2/6
- updated readme and added versions to requirements.txt

1/31
- adjusted error checking for missing overtone data

1/26: READY TO PUBLISH!
- certain warnings like file not selected would close software. replace this with warning message
- removed sigma_calibration_freqs, a vestigial variable made initially to contain error in the offset values, but offset values have no error. bandaid fixing this was causing issues, so it has been removed and functions utilizing it (e.g. thin film air) have been adjusted
- fixed crystal thickness that broke for literally no reason
- added warning to crystal to thickness if ydata empty (right before curve fit) to ensure offset values is selected over theoretical, and that raw data channels are selected
- commented out option for 1 or 4 sensors, will be implemented fully later
- updated sample generations contents

1/25
- added check and warning for if column headers are preformatted and asking user to double check the file and change it or proceed as is
- added check and warning for missing values
- changed how na values are dropped
- fixed bug involving qsense temp v time
- fixed bug where qsense was not un-normalizing
- refactored dissipation magnitude adjustment in file formatting to its own function
- adjust dissipation unit conversion to not occur for qsd files as it's already in correct magnitude

1/8
- finished documentation overhaul, specifically modelling.py

1/2 - 1/5
- major code documentation overhaul
- minor refactoring
- removed deprecated code for raw interactive plot
    - regular interactive plot can already handle either

12/28 - 12/29
- preliminary read raw .qsd implementation (credit to Jean-Michel)

11/18 - 11/19
- calibration vals frame visibility updates when changing from device that requires calibration vals to one that doesn't and vice versa
- software can now handle files that have some overtones columns not present (i.e. only having recorded 3rd, 5th, 7th when the device usually records 1st through 11th)
    - added local disps to format awsensors and qsense for magnitude conversion, to use only dissipation values that are recorded in the columns
    - unnormalization now grabs all column headers and filters through dissipation ones grabbing the number in front to use as the multiple scalar to unnormalize
    - adding offsets now simplified
        - go through cols in calibration df, if col also in fmt df, add value of that col to all vals in fmt df
        - this change was brought on by the need to address that some data files will not just have no data in cols for some overtones, but the overtones may not have cols there at all
    - updated qsense formatting function to scale magnitude of dissipation values same way as awsensors regarding the part accounting for some dissipation columns not recorded
- implemented pop up error messages for exception handling
    - all exceptions that were being caught previously now include error pop up windows (error msgs still print in terminal for debugging purposes as well)
    - exceptions that were caught and closed the program no longer close it, opting for the popup instead
    - added new exception catch in file formatting for if columns in data file don't match ones of chosen device manufacturer
- implemented warning messages for things that are not as serious as errors

10/26
- fixed bug where int plot would show delta in the y axis label when plotting raw data
- added support for openqcm next to auto calculate offsets like qcmi
    - adjusted UI options for prompting user of this
    - set flag for calculating offsets to True for qcmnext

10/14
- removed AWSensors option for input file type until we can get a data file to confirm
- added extension .xlsm to file browser class in main ui, and to opening df in format file
- fixed issue where during file formatting when renaming columns it would crash if columns not all columns for all overtones were present
    - change initially applied to and tested with qcmi
    - soon after applied to qsense and qcm next
- refactored qcmi formatting process in a cleaner way using 1 dictionary instead of 1 dict and 1 list
- removed label corresponding to fwhm in calibration window

10/12
- removed FWHM option from calibration window since QCMI auto grabs offsets
- bug fix with double digit overtone order for dissipation

9/30
- changed all user visible instances of mu or mean to average for consistency

9/24
- removed gordon kanazawa from UI
    - will be added in future version when flushed out

9/16
- fixed raw data interactive plot time conversion issue
- fixed calibration window scroll bar issue
    - applied same fix to other windows even though problems weren't evident in them
- fix horizontal scroll bar in main ui
- fixed qsense raw data bug where would only go as far as temp time column would
- fixed temperature vs time time scale issue
- fixed plot opts scroll bar issue
    - tkinter is annoying and update idletasks isn't working
    - solution was to resize window by 1 pixel when things changed on screen thereby making the window update


9/9
- UI has been updated to reflect automatic qcmi offset calculation
    - when selecting qcmi and then selecting offset data, instead of a prompt to enter calibration values, user is shown a label that informs them of qcmi auto offset calculation
    - when clicking qsense and then offset, normal offset entry label/button shown
- qcmi offset calculation function adjusted to not add 'temp time'
- calibration window functionality adjusted to accommodate adding of index column from qcmi offset calculations to maintain consisten file format

9/5-9/8
- updated theoretical values for offset data
- fixed qcmi issue
    - qcmi will no longer use user entered offset values
    - offsets for modeling purposes will use the average of full frequency and dissipation values in data file within the baseline
    - adjusted UI to explain qcmi will not need manually entered offsets
    - add boolean to input class that will be true if qcmi selected and need to calculate offset
    - add to analyze.py to calculate offsets for qcmi
        - calculations just averaging values of each overtones full values (not deltas)
    - save these calculations to offset file
- qcmi feature added an index row to offset data file
    - adjusted ad offsets function to compensate for this and correctly still add the offsets
- as per new information from Bernardo, adjusted qsense file conversions specifically for dissipation
    - dissipation no longer unnormalized (since it wasn't normalized to begin with)
    - dissipation multiplied by 1e-6 instead of 10e-6
    - dissipation works correctly now!!


8/18
- scrollbar
    - added inner_frame inside app_canvas inside container in the app class
    - added y scrollbar
    - bound y scrollbar to mousewheel
    - y scollbar will scroll with wheel intelligently
        - will scroll on app window only when mouse hovering over it
    - added x scrollbar
    - fixed dimensions of window
- added y scrollbar to plot customization window
- added scrollbar to offset data window
- gordon-kanazawa
    - Df_n was attempted to use a range, will now be an average
    - viscocity and density of liquid will not be separated, system of eqns doesn't have a dependent variable to split those up
    - values being reported will be eta*rho of liquid, the kinematic viscocity
    - solved gk values will reported for each overtone in each range into a csv file (no plots since no dependent variable)
    - removed gk_objective
    - adjust gk_eqn to be a simple equation not for finding fitting parameters, and just solving for kinematic viscocity
- moved temperature vs time dataframe separation further up in analyze_data() execution to fix bug where either data would not be found for overtone when selected, or it would mess up the time associated with the overtones' data in the rest of plots
- removed baseline corrections for temp v time
- added customization option to adjust dpi in customization window
- updated json files to accommodate figure dpi user setting
- adjusted all figure saving to use aforementioned user customization option


8/17
- new information says qsense data is normalized by default, added unnormalize() function to format_file.py to unnormalize data when converting file

- format changes:
    - change window title to BraTaDio - pyQCM-D Analyzer
    - t in crystal thickness make lowercase and f lower case in frequency
    - shear dependent compliance for slope of thin film in liquid and report just slope 1/pascal
    - sauerbray mass m lower case
    - capital s for sauerbray in modeling window
    - also in model window lower case crystal thickness
    - change slope correction to drift correction

8/14
- bug fix with file conversion when adding offset data. If no overtones skipped, would try to iterate over integer (0), so made default empty list, as well as check if list of overtones skipped is empty or not 

8/11
- added radio buttons to select dissipation or FWHM to offset values window
- radio buttons now adjust labelled to entries to reflect above choice
- when confirming selections, function converts values from FWHM to dissipation
- formatting for input data from AWSensors
    - added radio button option to file selection column of UI
    - added format_AWSensors function to format_file.py
        - similar to qsense, but with column reordering and removing
    - refactored and moved the code that adds offset data to qsense to a separate function, for reusability in AWSensors
    - added ability to remove indicies of calibration values being added to data file, as AWSensors only has overtones 3-11
- R^2 now reported for crystal thickness in plot
- bug fix, when not using all overtones for cyrstal thickness, it

- format changes:
    - adjusted instruction label for calibration window, opting to detail it in manuscript
    - change crystal thickness model to read overtone selection from 'raw'
    - change lower case d to capital D
    - change column titles for 2 and 3 to raw/shifted overtone selection
    - remove 'model' in crystal thickness button
    - consistent capitalization (just first letters)
    - change placeholder title to crystal thickness
    - remove qsense warning for offset values window

8/10
- now catch errors for if curve fit fails in interactive plot
- bug fix, when entering offset values, works first time, crashes second time. removed index column when reading offset values file
- when inputting offset data in window, make software create file for values (similar to interactive plot stats output) in case file not found for some reason
- refactor, modeling functions no longer receive fig_format variable passed into them from main, they instead call the get_plot_preferences function
- added crystal thickness button to UI modeling window
- added functions for equations for crystal thickness, and the supporting elastic modulus with stiffening
- fit line to above functions
- report r^2 to terminal of fit
- plot fit and resonant frequency values against overtone order
- write plotted data to csv file

8/4 - 8/9
- major restructure for interactive plot functionality with end goal of having interactive plot for raw and clean data
    - moved interactive plot UI specifications to bottom of cleaned data and raw data columns for use of both
    - changed checkbox for interactive plot to radio buttons so users don't select two interactive plots simultaneously
    - added an enable interactive plot option in column 4
    - all variables of class 'Input' pertaining to interactive plots have been adapted for a raw and clean interactive plot
        -i.e. changed input.interactive_plot_overtone = 0 to input.interactive_plot_overtone = {'raw': 0, 'clean': 0} to account for raw and clean separately
    - made interactive plot options frame into a class for easier duplicatability being in both columns
    - changed function that handles interactive plot input to a global function instead of class specific for better reusability of code
    - removed raw interactive plot function (originally used for deprecated method of selecting offset data)
    - changed clean_interactive_plot function to also handle raw data by passing in data_fmt so it knows which sub dictionary to look in in which_plot
    - adjusted function that prepares stats file to check data_fmt
    - changed output file for stats by prepending 'clean' or 'raw' to the file names
    - adjusted stats function for interactive plot to check for what data_fmt it is receiving
    - adjusted all modeling functions to make sure it only grabs from the clean stats file
    - updated clear saved ranges button to clean new file names
- bug fix clear saved ranges did not also clear thin film outputs
- bug fix when selecting overtones to use interactive for either raw or clean data, and then selecting overtones of other column, then clearing overtone selections of first column, says that no overtones were selected
- bug fix in prepare stats file, file IO mode not specified, specified write

7/8
- added functionality to do slope correction of drift in baseline
    - takes slope of baseline data and 'rotates' points based on the angle given by the arctan of that slope
    - added the OPTION for this in UI (since sometimes that drift may be sought after)
    - incorporated this into the interactive plot as well

7/7
- bug fix, some modeling functions looking for wrong column name for calibration values
- all dissipation values for qsense are now multiplied by 10e-6 as per Biolin being ridiculously difficult to work with
- bug fix, qsense offset values were not being added to qsense data, since renaming file for calibration data, and having user paste values into file
- removed 'change in' and 'delta' for frequency and dissipation RAW plots
- added label to calibration values window to indicate scientific notation format accepted
- removed references to old method of attaining calibration data
- removed optimization for formatting file, as it conflicts with qsense calibration data formatting
- changed 'calibration data' to 'offset data' in all user seen areas (file name, UI references, etc)
    - did not change variable names
- changed range saving from interactive plot to include x range selected solely for viewing purposes (has no effect on modeling functionality)
- modeling plots now save transparent backgrounds
- indicated in column headers for overtone selection that raw data plots f and d, shifted data plots Δf and Δd


7/3
- when confirming selections if field is empty, default to whatever was originally in the plot opts json instead of throwing an error
    - add label to notify user of this feature
    - put all widgets into a dictionary with they value as the widget and key is the same key in plot_opts.json
    - function to grid all items handled separately depending on type of widget
    - iterate through all widgets in frame looking for empty strings or empty radio buttons
    - when empty found, warn user once, and set the widget to the value to the corresponding previous opts value
    - set the current opts dict value to the corresponding previous opts value

6/30
- added to UI plot customization options input fields and labels for adjusting the bounds of each axis for visualization (time, freq, disp)
- updated plot opts json file for these new customization options
- adjusted setup_plot function to accommodate this customization
    - function looks at what label is being passed in to determine which bounds to set the axis to
- multi axis now works for the bounds adjustment (needed to independently set axis bounds)
- bug fix, tick direction in and out intvars were backwards

6/23
- added temperature and temp_time columns to qsense file conversion
- qsense data can now plot temperature vs time

- removed button to select calibration file as it will now only reference one file
    - this file can be directly copy pasted to by the user, or fill out entries via a popup window in the UI
- removed file conversion for calibration values, opting for alternate method below
- calibration values now can be copy pasted directly into csv file entitled 'COPY-PASTE_CALIBRATION_VALUES_HERE.csv' in calibration_data folder, OR
- other option to bring up window to enter values into UI
    - UI contains labelled entries for all freq and disp values that are then grabbed and written to a csv file for later use
    - empty or incorrect values are written as a 0 (user is also warned)
    - when selecting calibration data, button to open calibration data shows, as well as label to copy paste values into a csv file directly

6/21
- adjusted theoretical values df to match bratadio format
- adjusted how get_calibration_values() grabs theoretical values to match the file format conversion for calibration data from qsense
- fixed bug in calibration vals where values were not being grabbed and program crashed for thin film models
- fixed bug when not modeling all overtones, first overtone not selected would lead to no overtones after it being analyzed even if they were selected
- 

6/20
- moved file format options to plot customization window
- moved x time scale option to plot customization window
- updated json file for option storage to account for the above changes
- x time scale and file format are now saved options that don't need to be selected every execution of the software
- replaced all references of input.x_timescale and input.fig_format with the appropriate attributes in the plot customs dictionary

- added plot preference to input how many points to plot (default 1 which is every point)
    - i.e. if the data is too crowded, input can determine to plot every 5th point
- updated json file for the above plot preference addition
- updated all plotting in analyze.py to plot points based on the index (except interactive plot)

- removed prompts and selections that followed selecting calibration values
- added calibration data file selection button to col 1 (calibrationValsFrame)
- added warning label regarding needing calibration data for modeling with qsense data
- when formatting file with qsense, now adds calibration values from user spec'd calibration file to the data df

- moved range selection of interactive plot to column 4 out of modeling window
    - put modeling button below the int plot options frame
- multiaxis changed to filled circles and empty circles
- updated y axis label for avgs method of finding Sauerbrey mass to indicate that it is the mass of each overtone
- changed run avg of... to plot avg of in modeling window
- updated temp v time y label, Temperature, t(italic) (degreeC)
- fixed bug that first submission would look for int plot overtone even if int plot checkbox was deselected

6/16
- changed avgs plots in modeling to go to modeling folder, removed equation folder

6/15
- remove saving of Sauerbrey stats/ranges, alt method of sauerbrey will also use rf_stats and multiply C to avg rf of each overtone
- removed C from range statistics, opting for it to be done only in modeling.py
- finished reimplementation of alternate Sauerbrey method
    - main method calculated the mass via the slope of the fit of avgs freq of all overtones
    - alt method plots the mass for each overtone
- Sauerbrey now saves output of both methods to a file
- avgs plotting works with multiple range selections
- thin film air analysis now works for multiple range selections
- optimization input altered flag added, caclculations only rerun if modification made in ui
- added requirements list for packages and install_packages.py was condensed to utilize that txt file
- optimization to check raw_data directory and see if file has already been formatted previously
- bug fix where if selecting a formatted file (specifically the copy that 'format_file.py' makes with 'formatted' prepended to the name), it would still prepend 'formatted' again and look for the wrong file

6/14
- added capability to enter time range selection in interactive plot
    - set TkAgg as backend for span selector window generation to allow for tkinter entry fields
    - text entry has a focus in/out handler for temporary text
    - update_text and onselect communicate with eachother
        - if using span selector, text field is updated with xmin,xmax values
        - if using text field, spans are set to match the entered values
    - added update text function to perform all the same tasks as the onselect function
    - refactored code so the above tasks are done in a separate function that onselect and update text both call
        - split into 2 functions, one to update plot and one to calc and save stat data
- thin film in liquid records output data used for plots into csv file "thin_film_liquid_output.csv"
- thin film in air records output data used for plots into csv file "thin_film_air_output.csv"

- Sauerbrey now has 2 methods of calculations
    - current way takes average Df from rf_stats and fits linear function to those values, multiplying slope by a theoretical or calculated C
    - additional way is being reimplemented where full freq range data is saved and picked up by sauerbrey function, and mass is plotted as a function of time by multiplying each df point by C

- bug fix input file selection not being saved
- updated readme for spyder users to make a modification to code

6/8
- fixed bug where axis weren't being labelled and no formatting was ocurring except for the last generated figure
    - setup_plot() now gets the passed in figure's number and selects it
    - figure saving now occurs outside of setup plot
- fixed bug where plot format options were only grabbed when restarting software
- replaced fundamental with 1st everywhere by altering the ordinal function
- changed color scheme of multiaxis to use the same color mapping of overtones as other plots
    - to help differentiate between freq and dis, freq uses right side up trianges, and dis uses upside down triangles
- modeling window opens from a separate button in column 4 rather than with the int plot checkbox
    - replaced destroy model window with test model window to check if it's already open when clicking button to not open duplicate windows

6/7
- refactor, made plot_customs a global variable since it is called in so many different functions
- refactor, all plots are named figure/axis objects, instead of using plt.figure(#) selecting the figure to modify before modifications are made. This is much more explicit and easy to follow rather than keeping track of which number belongs to which figure
    - adjust setup_plot functions accordingly
- sauerbrey report to 1 decimal


6/6
- fixed bug where if int plot in col 4 was checked, checking and unchecking other items in that column would open the model window 
- fixed bug with temperature plot time scale, changing units of time generated incorrect figures. temp df was in for loop of freq/dis analysis repeatedly subtracting baseline start and divisor
- adjusted multiaxis plot legend to report just the ordinal overtone number
- y axis labels in visualizations now show Df_n instead of just Df
    - adjustment made also to int plot and model plots
- refactored generate_interactive_plot() condensing code that chooses user specified overtone for visualizations
- changed units of dissipation linear fit in int plot to 1/{timescale}
- bug fix where units int plot linear fit were only reporting first letter (i.e. min was only showing m)
    - in main changed radio handler for time scale to set var to s, min, or hr, instead of just s, m, h and adjusting later
    - refactored code to accommodate this change
- raw plots now combined into 1 plot for all freq overtones and one for all dis overtones


6/5
- when selecting file, there is now a button to select which opens windows file explorer for user to select their file
    - removed code that called for separate file name and file path vars, replacing it with input.file which is simply the path/name.ext, vars that need just one of those are split as needed
    - removed file name and directory entries and corresponding handlers for them
    - refactored format_file.py to account for variable restructuring

- visualization plots now show when f is normalized in the axis label
- refactor s.t. normalized freq plot is not a separate chunk of code, rather just choosing labels for regular freq plot

- multiaxis plots now save all plots into one figure instead of separate for each overtone
- bug fix: legend placement was determined before all overtones plotted so it was misplaced
- bug fix: modeling plots were normalized when they shouldn't be
    - added unnormalized_df that is just a copy of the baseline shifted data_df but remultiplying the overtone ordinal value

- plot options put label that states options are saved even when closing software
- change asterisks to a dot
- nDf should be n * Df (dot not asterisk)
- thin film analysis y axis put proper fractions for labels
- hard coded to load qcmi.txt initially to minimize time takes for testing (will be removed on release)
- hard coded baseline time values for same purpose
- dis vs freq plot cleaned up legend
- fixed bug in multiaxis plot, now correctly save figure with user spec'd format
- fixed bug where all options in col 4 were calling destroy model window even when model window wasn't opened

5/26
- began implementation for voinova model in separate script 'voinova.py'
- voinova model runs and produces an accurate plot when compared to the one done manually, however numbers are off
    - need to meet next week to discuss units/orders of magnitude of values

5/25
- bug fix, C calculations for calibration data

5/24
- changed analyze to visualize when selecting overtone for int plots
- created new csv file in 'res' folder with theoretical frequency values
- added std dev to calibration data range selection
- updated calibration_frequencies function to grab frequencies from calibration data file
- adjusted prepare stats file function to have file path in name instead of hardcoding path, so can save calibration ranges to different folder than stats ranges
- bug fix, calibration/theoretical val radio buttons in modeling were not actually being sent properly to modeling functions, now that var is sent directly to function instead of via input object
- added button to clear old frequency data from selections in calibration_data.csv

- theoretical/calibration values option selection moved to column 1
- calibration menu option moved to nested option within column 1
- restructured theoretical/calibration selection as follows:
    - first prompted to use either theoretical or calibration values
        - if using theoretical, input object is updated and user can continue
        - if calibration selected, input object updated and user is then prompted with option to use from file or make selections
            - if file option selected, label informs user to copy values into file in calibration_data folder
            - if selections option selected, calibration menu button made available

- lower case dissipation for equation model plots
- changed modeling plots to black points and err bars
- removed 'analysis' from ov avgs

- added ability to calculate C based on calibration fundamental frequency for Sauerbrey model

5/18
- added thin film in liquid to title of plot
- Added functionality of Thin film in air analysis
    - plot Df/n (Hz) against n^2
        - offset m(sub)f is y intercept of linear fit
        - slope is Jprime
    - plot DGamma against n^2
        - slope is Jdoubleprime
    - see Johannsmann paper fig 17 eqn 46 for details

- added linear fit to interactive plot zoom section to measure drift
- fix bug where previous linear fits remains on screen during new selections
- add legend to report drift value (slope)
- adjusted value reporting to account for user selected time inputs with units in legend

- implemented avg plots for avg dissipation as well
- cite libraries as sources for paper
- make flowchart in inkscape

- added button in raw data column for calibration data window
- new class for calibration data window
- filled calibration data window with entries for constants and button for raw data int plot
- refactor to put all code setting up int plot into its own function
- refactor put clean data int plot into its own function
- added input fields to input which overtone analyzing and which range selecting for raw int plot
- raw_interactive_plot() function acts similarly to clean one but with different data and calculations
- save_calibration_data() function to save the averages of selections in raw int plot in similar fashion to range_statistics
- selections are averaged and saved in calibration_data.csv
- select_calibration_data() function to handle all processes relating to selection of raw data
- move conversion of files to confirm file data button 
- exception to check if selected overtone to analyze in int plot is selected in checkboxes
- interactive plot now open from calibration menu
- set yticks in dissipation plot to be scientific notation to clean it up

5/17
- changed func name avg_Df to avgs_analysis to prepare for adding avg Dd functionality
- bandwidth shift
    - removed 1st and 3rd items from legend
    - removed rsq value from legend
    - changed title to DGamma/-Dfreq ~ J`(sub)f(omega)(eta(sub)bulk)

- avg Df and Sauerbrey
    - changed y axis labels
    - adjusted legend
    - x tick marks show odd numbers (corresponding to the overtone vals)

- fixed modeling options window title
- changed order of modeling buttons
- changed modeling button names
- added button for thin film in air analysis
- changed linear_regression function to thin_film_liquid_analysis to differentiate between the soon added thin_film_air_analysis
- refactored code moving all bandwidth shift calcs from thin_film_liquid_analysis() to new function process_bandwidth_calculations_for_linear_regression() for more reusable code for thin_film_air_analysis

5/16
- modeling options moved from 5th column of main UI to a new window that opens upon selecting the interactive plot
- added functionality to close modeling window when unchecking interactive plot box
- added button to analyze avg change in frequency against overtone numbers
- added functionality to plot average change in frequency against overtone numbers (akin to Sauerbrey equation just without the actual equation)
- fix bug where non selected frequencies that have 0 rows in range data are still plotted
- fixed labels for avg change in frequency plots
- fixed bug in renaming dataframe to bratadio format
- fixed bug when grabbing overtone selection for int plot, was checking if model window is visible when it didn't have that attribute, changed to input.range_frame_flag


5/14
- progress on moving column 5 (modeling) to new window instead

5/6
- change QCM-D -> Open QCM Next
- change linear analysis to Shear dependent compliance analysis
- change corrected data to shifted data
- switch order of buttons in modeling column
- added file checking/creation of sauerbray stats to prepare_stats_file in interactive plot
- added saurbrey statistical calculations to range_statistics() in interactive plot
- added sauerbrey stats file to clear range data function button
- for sauerbrey analysis:
    - for eqn plotting just do the whole range of the overtone
    - similar to linear regression, plot avg Dm values in each overtone for each range selected, with err for std dev
    - 1 plot per range selected, each range analyze all overtones
    - Dm v overtone, n
    - removed code to plot sauerbray range eqn points (opting for averages described above)

4/30
- integrated plot customizations from json file into analyze.py
- added legend text size option
- added inout option to tick directions
- fixed set with copy warning for multiaxis plot
- fixed legend placement for multiaxis plot
- added error checking to ensure all plot opt fields are filled out
- modeling.py functions now utilize plot customizations

4/29
- began plot customizations class and figured out inheritance issue (instantiated in App class)
- added color wheel customization to plot opts window for each overtone
- added json dump function to save plot preferences
- added all other plot customization options to window
- added default values option to set options to default, also means having a default values json file
- fixed bug so plot customizations dictionary is initialized to previously saved values instead of resetting everytime

4/27
- error check for linear regression if different number overtones selected than saved in stats files
- bug fix: plots saved in modeling.py now also utilize user selected figure format
- bug fix: after submitting and running linear regression, would alter keys in which_plot in the double digit overtones, causing the underscore to be removed and not be found in dataframe (i.e. 11th_dis -> 11thdis). Culprit in overtone selection in modeling.py
- started custom Error classes to handle shape mismatch
- remove legend in temp v time
- changed overtone labels to just number of overtone using get_num_from_string() function
- removed Delta from Delta t in time labels
- bug fix normalizing overtone, used num from string function instead of hardcoding

4/22
- removed option for calibration/theoretical vals for Sauerbray, as option currently for Linear Regression will also apply for Sauerbray, so 2 separate options unnecessary

4/18
- updated README
- error check to see if Df already normalized before doing Sauerbray, if it is we don't divide by the overtone as to not do it twice
- updated plot formatting for Sauerbray
- fixed bug legend not showing in Sauerbray plots
- fixed bug when plotting only raw data
- fixed bug in Linear regression model

4/17
- refactored code to clean up analyze.py, moving nested functions outside of analyze() and shortening it. more refactoring of the like needed
- fixed normalization bug, needed to divide baseline df by overtone as well
- fixed bug in naming multiaxis plot, name pulled from wrong list of freqs
- fixed bug when plotting more freq overtones than dis or vice versa
- fixed bug in sauerbray eqn where graph shape was correct but numbers were off, was doing unnecessary unit conversion
- applied color map used in analyze.py to sauerbray eqn plots
- added opt to plot temp as f(time)
- adjusted data formatting section to support above (qsense does not have temperature data)
- added error checking for it data has temperature values
- added error checking for if dataframe empty (if user selects a overtone to plot that doesn't actually have data in it)

4/10
- fixed sauerbray eqn plots. Now will plot all overtones selected with all ranges having selections

4/9
- added option to empty range selection files to clear previous experiment data
- fixed sauerbray ranges writing header twice
- sauerbray analysis function progress, can read in and iterate over data as well as plot, however bug introduces 0 arrays so needs fix

4/6
- adjusted range_statistics() so sauerbray ranges saved to csv file
- begun sauerbray function

4/2
- added options for sauerbray modeling
- added to statistics analysis functions to handle sauerbray range data

3/15-3/16
- linear regression now works with variable number of overtones being used, however needs verification with manually analyzed data
- fixed linear reg bug where freqs that are not being analyed and have 0 values were still being plotted
- major refactoring, putting most of linear regression function into separate functions
- added back end functionality to have different labels dependend on if user indicates if latex is installed
- modified propogation function to account for varying amts of overtone data (accounted for 0 entries)


3/11
- bug fix: 11th and 13th overtones were not working
- flushed out file conversion from qcmd, qcmi, qsense, to bratadio
- coupled span selectors in interactive plot
- refactor: put code from onselect to prepare the saving of statistical data, and the saving/formatting of the data into functions that get called from onselect
- optimize: rather than converting the file format every time submitted, first_run flag added to indicated if file needs conversion or not
- bug fix: when submitting from gui after the first time, would crash unable to open the csv from file
- added this changelog

3/8
- added gui options for different data file formats (qcmd, qcmi, qsense)
- added functionality for new data file formats

2/23
- formatting col5 to make more clean
- bug fix: added overtones
- bug fix: column 5 showing up
- more refactoring in favor of OOP for gui

2/16
- major refactoring-restructuring

1/12
- linear regression plot formatting changes
- linear reg model now averages across mult data sets for each range, added find nearest time

1/11
- can save stats ranges across diff files, avg across them needs work
- int plot saves mult ranges, lin reg uses mult ranges

1/4
- file restructuring
- format changes, updated readme
- adjusted for bandwidth shift, updated readme

1/2
- formatted interactive plot
- plotting statistical data of each frequency
- adjust stat data calcs to include all freqs based off int plot range

12/30
- updated for different format input data
- bug fix int plot overtone selection
- bug fix, selecting rf would alter selection for disp in int plot

12/29
- plot formatting

12/28
- functionality of selecting range to plot

12/16
- added statistical analysis to int plot ranges
- added functionality to save from multiple files in statistical calculations

12/14
- added rf and dis to plot selector

12/8
- changed range selector to text entry

11/30
- added functionality to select-save mult ranges for statistical analysis from interactive plot

12/29
- file structure adjusted
- gui runs async from data, added interactive plot

11/29
- refactor so dont need to close gui to run analysis

10/27
- gui and plotting format changes
- small format changes to ind and qcmd

10/12 
- fixed x time scale bug

10/3
- multi axis plot for dD and dF added

10/1
- added option to plot dD vs dF
- bug fix on which channel plotted, raw data plotting
- func for plotting (refactor)
- overwrite clean data now works
- clean plt - only plots channels selected (not all)
- function to get channels (refactor)

9/30
- add alt opt to gui
- begun error checking function
- system for deleting channels
- ui dev progress

9/28
- updated plot formatting

9/27
- improved backend com,
- backend linked to front. can plot all clean data

9/24
- changed gui labels
