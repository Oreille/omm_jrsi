# OMM: Observable Moment Matching

### This the numerical code used to compute the Probability Density Function (PDF) from the variability observed in measurements (whether synthetic or experimental). You will find below details about how to set up a demo test case.

The code is written in C++ (C++98 standard) and is divided into three files:
* main.cpp
* DE.cpp
* DE.hpp

### Data
We provided a demonstration test case which shows the expected structure of
your data.
The demo/ directory is organized as follows:
* "measurements/": in this directory are stored the moments of your measurements
(whether experimental or synthetic). For each mth order moment, there should be
a file named "moment[*m*].txt" of size (*nt*,1) (*i.e.* nt rows and 1 column) where *nt* is the total number of
time steps in your signals. In this demo, the moments have been computed
*after* noise had been added to the synthetic measurements.
* "simulations/": in this directory are stored the model outputs "data.bin" and the
collocation points "collocation.bin" (parameter samples used in the OMM
algorithm).
For speed and memory reasons, the program takes these files in binary
format. If you're using your own data, you must convert your ascii files to our
binary format. Simply run:
> python ../../../utils/compress.py
[your_file_in_ascii_format_with_txt_extension]

Conversely, if you want to convert the binary files in the demo directory to
ascci files, execute the following command:
> python ../../../utils/deflate.py [file_in_binary_format_with_bin_extension]

The corresponding ascii files should have the following formats:

    * data.txt: (numSamples, nt) where numSamples is the total number of samples in the simulation data set.
    * collocation.txt: (numSamples, p) where p is the number of uncertain
    parameters

* "DE.log" log file: you need to set some parameters of the method in
this file. 

It is read line by line and organized as follows:

    * p: number of parameters (int)
    * Nc: number of samples (int). Must be <= numSamples
    * Nm: number of moments (int)
    * Directory of your simulations set (string)
    * Directory of your measurements set (string)
    * File prefix of your measurements moments (string)
    * Maximum iterations of the Newton method (int)
    * Tolerance on the representation error (double) (see [1])
    * Tolerance on the pseudo-inverse calculation (double)

* "selectedTimeSteps.txt": Subset of the available time steps where the moments
  are to be matched. Should be a list of indices (without repetition) between 0
  and nt-1. If this files does not exist, the inverse procedure will
  be executed by default on the **whole time grid**. This is not recommended in practice (see *[1]*): if you exceed a couple of
hundreds time steps, you may soon run out of memory and the computational time
may go through the roof.

*[1] https://hal.archives-ouvertes.fr/hal-01391254 for implementation
 details*

### Compilation
**Make sure you have Eigen 3 and GSL implementation of BLAS installed**

To compile the code, run the following command:
> g++ -O3 -I [path_to_Eigen_include] -I [path_to_gsl_include] main.cpp DE.cpp
-o computePDF -L [path_to_gsl_lib] -lgsl -lgslcblas -lm

### Execution

> computePDF demo [OR *your_case_name*]

### Visualization 

The output of the program is stored in an ascii file named "pdf.txt". This file should have
Nc lines and (p+1) columns. The parameter samples are replicated in the
first p columns and the PDF values are in the last column.
There are several options to visualize the results:
> python pdfplot.py pdf.txt 

which outputs the point-wise values of the PDF projected onto each parameter
axis.
> python plot_pdf_3d.py pdf.txt

which makes a surface plot (only works when p=2) of the PDF. This only works
with recent versions of matplotlib.
