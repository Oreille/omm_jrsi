# Time Step Selection procedure

### This the numerical code used to select the time steps subset to be used in OMM

The code is written in Python (required version: 3.4) and is divided into three files:
* computeDerivatives.py
* activeClustering.py
* extractSelection.py

### Data

* All data required for the OMM procedure (see OMM/README.md) 

* "TSS.log" log file: you need to set some parameters of the method in
this file. 

It is read line by line and organized as follows:

    * caseName (string): your case name (e.g. demo)
    * numProcs (int): number of procs to be used in computeDerivatives.py
    * N (int): number of parameter samples in computeDerivatives.py
    * neighbour_regularization (int): see [1]
    * maxK (int): maximum number of clusters you may need.
    * ev_threshold: threshold on the eigenvalues (see [1])
    * vol: stochastic volume
    * glob_iter: global iteration between OMM and TSS

*[1] https://hal.archives-ouvertes.fr/hal-01391254 for implementation
 details*

### Execution

> python computeDerivatives.py TSS.log

> python activeClustering.py TSS.log

> python extractSelection [caseName] [glob_iter]
  [number_of_selected_time_steps]

** For the demo > python extractSelection demo 0 20

### Execute OMM

You can now move the "selectedTimeSteps.txt" file to your case folder in the ../OMM/
directory and execute the inverse procedure.
