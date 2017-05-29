# omm_jrsi

### Welcome to our omm_jrsi project !

![Front page illustration](./images/omm.png "Is this a log-normal distribution?")

### What is this?

In this repository, you will find the data and codes corresponding to our submission to the
Journal of the Royal Society Interface. The repository is organized as follows:

* Codes

  * ./omm: OMM stands for Observable Moment Matching. This method estimates the PDF of hidden parameters from the statistical moments of dome observable quantities. Try our demo test case and learn more about it by reading ./omm/README.md. 
  * ./time_step_selection: OMM on its own might become computationally challenging when confronted to high-dimensional observables. You will find in this directory a program that selects a subset of the available time steps of your signal to be fed to OMM. Read ./time_step_selection/README.md further instructions.

* Data

  * ./test_case_1: This is a synthetic data set consisting of Action Potential (AP) traces generated with the model by Decker [1].
  * ./test_case_2: This is a synthetic data set consisting of AP biomarkers generated with the model by Courtemanche [1].
  * ./test_case_3: This is an experimental data set consisting of AP biomarkers from canine ventricular myocytes.  
  * ./test_case_4: This is an experimental data set consisting of AP biomarkers from human atrial cardiomyocytes.

*[1] For details about AP models and data, we refer to the following paper: (submitted)*
