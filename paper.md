---
title: 'pyQCM-BraTaDio: A tool for visualization, data mining, and modelling of Quartz crystal microbalance with dissipation data '
tags:
  - Python
  - Quartz Crystal Microbalance with Dissipation
  - QCM-D
  - Sauerbray
  - thin film in liquid
authors:
  - name: Brandon Pardi
    orcid: 0000-0001-6483-9858
    equal-contrib: true
    affiliation: 1
  - name: Syeda Tajin Ahmed
    orcid: 0000-0002-2719-9641
    equal-contrib: true
    affiliation: 1
  - name: Silvia Jonguitud Flores
    orcid: 0009-0005-4841-4901
    affiliation: 3
  - name: Warren Flores
    orcid: 0009-0001-1462-4688
    affiliation: 1
  - name: Jean-Michel Friedt
    orcid: 0000-0003-4888-7133
    affiliation: 5
  - name: Laura L.E. Mears
    orcid: 0000-0001-7558-9399
    affiliation: 2
  - name: Bernardo Yáñez Soto 
    orcid: 0000-0002-4273-6513
    affiliation: 3
  - name: Roberto C. Andresen Eguiluz
    corresponding: true
    affiliation: "1,4"
affiliations:
  - name: Department of Materials Science and Engineering, University of California Merced, Merced, California 95344, United States of America
    index: 1
  - name: Institute of Applied Physics, Technische Universitaet Wien, Vienna 1030, Austria
    index: 2
  - name: Instituto de Física, Universidad Autónoma de San Luis Potosí, San Luis Potosí 78000, Mexico
    index: 3
  - name: Health Sciences Research Institute, University of California Merced, Merced, California 95344, United States of America
    index: 4
  - name: FEMTO-ST Time & Frequency department, 26 Rue de l'Épitaphe, 25000 Besançon, France
    index: 5
date: 19 January 2024
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Here, we present a Python-based software that allows for the rapid visualization, data mining, and basic model applications of quartz crystal microbalance with dissipation data. Our implementation begins with a Tkinter GUI to prompt the user for all required information, such as file name/location, selection of baseline time, and overtones for visualization (with customization capabilities). These inputs are then fed to a workflow that will use the baseline time to scrub and temporally shift data using the Pandas and NumPy libraries and carry out the plot options for visualization. The last stage consists of an interactive plot, that presents the data and allows the user to select ranges in MatPlotLib-generated panels, followed by application of data models, including Sauerbrey, thin films in liquid, among others, that are carried out with NumPy and SciPy. The implementation of this software allows for simple and expedited data visualization and analysis, in lieu of time consuming and labor-intensive spreadsheet analysis.

---

# Statement of need


QCM-D has gained popularity in many different scientific fields due to its experimental simplicity and versatility. QCM-D (or just QCM if not quantifying energy losses) can be combined with a variety of instruments for in situ complementary measurements, such as atomic force microscopy (AFM),[@Friedt:2003] microtribometry,[@Borovsky:2019] surface plasmon resonance (SPR),[@Bailey:2002] or electrochemistry,[@Levi:2016] among others. However, one drawback rests in that any QCM-D experiment, real-time monitoring of sensor surface-environment generates large volumes of data entries, and packages used to collect data do not typically possess straightforward data visualization, data mining capabilities, and basic model applications. Furthermore, programs associated with QCM-D data collection and analysis are often proprietary with limited access. There exists other open-source packages, such as RheoQCM[@Shull:2020] and pyQTM[@Johannsmann:2023], however, they focus on more complex data modeling rather than data mining. `pyQCM-BraTaDio` can serve as a complement to these two packages Here, we present an intuitive Python-based, open-source software that is QCM-D manufacturer agnostic of multi-harmonic collecting systems for (1) simple and fast data visualization and interaction, (2) data mining and reduction, and (3) basic model applications. The supported models include (i) Sauerbrey, for rigid thin films, (ii) viscoelastic thin film in a Newtonian liquid, (iii) viscoelastic thin film in air, and (iv) quartz crystal thickness determination. 

---

# Software interaction


![User interface of pyQCM-BraTaDio. (1) Initialization conditions, (2) selection of frequencies and dissipation for data mining, visualization, and modeling, (3) interactive plotting options for data range selection, and (4) selection of plotting options and modeling.](figs/figure1.png)


The interaction with `pyQCM-BraTaDio` is via a GUI, which allows the user to utilize the software with minimal to no console interaction. It operates following the workflow shown in SI figure 2, The main window is organized into four main regions, shown in Figure 1. These regions are (1) initialization conditions, (2) selection of frequencies and dissipation for data mining, visualization, and model application purposes, (3) interactive plots for data mining, and (4) selection of plotting options and models.

---

# Notable features of `pyQCM-BraTaDio`

### Expedited basic visualizations

![**Raw data plots generated by BraTaDio for film formed from a solution of BSA at 1 mg/mL in PBS adsorbed to an Au-coated quartz crystal.** (a) Absolute frequency fn as a function of time t, (b) corresponding absolute dissipation Dn as a function of time for n = 3, 5, 7, 9, 11, and 13. The peaks seen in panel (b) correspond to transition periods, that is, pumping BSA after the PBS baseline was established (t = 5 min), and the second to a PBS wash (t = 55 min.](figs/figure2.png)

As in any experimentally obtained data, visual inspection is crucial for an initial assessment of baseline stability, anomalies, such as presence of undesired air bubbles, leaks, signal loss, among others. Two basic visualization options are implemented in the `pyQCM-BraTaDio` tool: (i) a full data range visualization referred here as raw data, Figure 2, and (ii) the experimental data, referred here as reference level adjusted data, Figure 3. For these options, the user can select the overtone order(s) to visualize the frequency and dissipation in various plotting formats. Figure 2(a) and (b) show the absolute frequency $f_{n}$ and dissipation $D_{n}$ as a function of time $t$ for $n = 1, 3, 5, 7, 9, 11$ and $13$ for a bovine serum albumin (BSA) solution absorbing to a gold substrate. The relevant experimental data can be visualized by selecting the ‘Plot shifted data’ option. For example, change in frequency as a function of time, ${\Delta}f_n$ vs time $t$, Figure 3(a), change in normalized frequency as a function of time, ${\Delta}f_n/n$ vs time $t$, Figure 3(b), change in dissipation ${\Delta}D_n$ vs time $t$, Figure 3(c), combined change in frequency and change in dissipation as a function of time, ${\Delta}f_n$ and ${\Delta}D_n$ vs time $t$, Figure 3(d), combined change in normalized frequency and change in dissipation as a function of time, ${\Delta}f_n/n$ and ${\Delta}D_n$ vs time t, Figure 3(e), the temperature $T$ as a function of time, $T$ vs $t$, Figure 3(f), which is critical to determine any temperature effects in collected data. Finally, change in dissipation as a function of change in frequency, ${\Delta}D_n$ vs ${\Delta}f_n$, Figure 3(g), and change in dissipation as a function of change in normalized frequency, ${\Delta}D_n$ vs ${\Delta}f_n/n$, Figure 3(h) to obtain qualitative insights of the adsorbed film rigidity. 

![**Plots generated by BraTaDio for a film formed from a solution of BSA at 1 mg/mL in PBS adsorbed to an Au-coated quartz crystal.** (a) Change in frequency Δfn as a function of time t, (b) change in frequency normalized by overtone order, Δfn /n as a function of time t, (c) corresponding change in dissipation ΔDn as a function of time, (d) change in frequency normalized by overtone order, Δfn /n and corresponding change in dissipation ΔDn as a function of time for n = 5 and 7 for clarity, (e) change in dissipation ΔDn as a function of change in frequency normalized by overtone order, Δfn /n, for n = 3, 5, and 7 for clarity,  and (f) temperature T as a function of time. Data collected with a QCM-I system.](figs/figure3.png)


### Data mining via an interactive plot

![(a) Input line for time range selection, (b) change in frequency interactive plot, (c) zoomed-in region from the change in frequency interactive plot and frequency drift, (d) change in dissipation interactive plot, and (e) zoomed-in region from the change in dissipation interactive plot and dissipation drift.](figs/figure4.png)

To facilitate the procedure of data mining, that is, selection of frequency and dissipation ranges for time ranges of interest, it is possible to interact with the data via an interactive plot, Figure 4. `pyQCM-BraTaDio` will compute the average and standard deviation of the data points contained within the selected range for each overtone selected and display the selection with a linear fit, every time a selection is made. Through the use of user dictated range identifiers, multiple selections can be made without overwriting data. Overwriting only occurs when further selections are made without updating the range identifier *ex ante*.

### Applications of models
Matching QCM-D experimental data to models that provide physical interpretation is key for the quantitative characterization of liquids interacting with the quartz crystal surfaces or nanofilms. With `pyQCM-BraTaDio`, it is possible to apply models of steady state (in equilibrium) thin films using one of the following models: (i) the Sauerbrey equation for very thin films,[@Sauerbrey:1959] (ii) shear-dependent compliance of a thin viscoelastic film in a Newtonian liquid,[@Du:2004] and (iii) determination of the quartz crystal thickness.[@Reviakinea:2004] These models are described in the SI, accompanied with experimental examples. 

---

# Conclusions

pyQCM-BraTaDio is a Python software implemented ad hoc to expedite the process of data mining and analysis of QCM-D experimental data. Beginning  with a Tkinter GUI for metadata collection, the inputs and data are fed to several routines to mine and reference level adjust data with the Pandas and NumPy libraries. The user is able to interact with QCM-D data in a novel way via a MatPlotLib interactive plot widget towards the end of the workflow. This interaction offers the user to apply several models such as Sauerbrey, thin film in liquid, thin film in air, and crystal thickness. This tool is key for efficient data analysis in preference over laborious spreadsheet evaluation.

---

# Acknowledgements

R.C.A.E. acknowledges funding from the NSF-CREST: Center for Cellular and Biomolecular Machines through the support of the National Science Foundation (NSF) Grant No. NSF-HRD-1547848. R.C.A.E. and B.P. acknowledge funding from the CAREER grant NSF CMMI Grant No. #2239665 awarded to R.C.A.E. 

---

# Supporting information
The authors have compiled additional supporting information in a separate document containing more details on the software’s execution, as well as demonstrating the efficacy of the software across multiple QCM-D devices.

# References