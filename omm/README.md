This the numerical code used to compute the Probability Density Function (PDF)
from the variability observed in measurements (whether synthetic or
experimental).

The code is written in C++ (C++98 standard) and is divided into three files:
* main.cpp
* DE.cpp
* DE.hpp

### Data
We provided a demonstration test case which shows the expected structure of
your data.
The demo/ directory is organized as follows:
* measurements/: in this directory are stored the moments of your measurements
(whether experimental or synthetic). For each mth order moment, there should be
a file named "moment[*m*].txt" of size (nt,1) where nt is the total number of
time steps in your signals. In this demo, the moments have been computed
*after* noise had been added to the synthetic measurements.
* simulations/: in this directory are stored the model outputs "data.bin" and the
collocation points "collocation.bin" (parameter samples used in the OMM
algorithm).
For speed and memory reasons, the program takes these files in binary
format. If you're using your own data, you must convert your ascii files to our
binary format. Simply run:
> python ../compress.py [your_file_in_ascii_format]
The ascii files should have the following formats:
    * data.bin: (numSamples, nT)
    * collocation.bin: (numSamples, p) where p is the number of uncertain parameters

### Compilation
**Make sure you have Eigen 3 and GSL implementation of BLAS installed**

To compile the code, run the following command:
> g++ -O3 -I [path_to_Eigen_include] -I [path_to_gsl_include] main.cpp DE.cpp -o computePDF -lgsl -lgslcblas -lm

### Execution
> computePDF demo [or *your_case_name*]
The output of the program is stored in pdf.txt. This file should have
numSamples lines and (p+1) columns. The parameter samples are replicated in the
first p columns and the PDF values are in the last column.
There are several options to visualize the results:
> python pdfplot.py pdf.txt 
which outputs the point-wise values of the PDF projected onto each parameter
axis.
> python plot_pdf_3d.py 
which makes a surface plot (only works when p=2) of the PDF. This only works
with recent versions of matplotlib.
