#This the data for Test Case 1: Synthetic dataset simulated using the Decker
canine model.
To deflate the files with ".bin" extensions (in binary formats), run the
following command:
> python ../deflate.py [fileName]

List of files and description:

* "time_grid.txt": a vector of size 449 whose values are the time steps on which
  the simulated APs are interpolated.
* "simu_decker_control.txt": simulated APs in control conditions (no drug
  block). It is a matrix of size (number_of_samples x num_time_steps)
  i.e. (32768 x 449). Github reduces the upload size to a limit of 50MB so the
  file has been splitted in two: [..]_a.txt and [..]_b.txt
* "synth_decker_control.txt": synthetic APs in control conditions (no drug
  block). It is a matrix of size (number_of_samples x num_time_steps)
  i.e. (10000 x 449)
* "simu_decker_drug_block.txt": simulated APs in drug block conditions. It is a matrix of size (number_of_samples x num_time_steps)
  i.e. (4096 x 449)
* "synth_decker_drug_block.txt": synthetic APs in drug block conditions. It is a matrix of size (number_of_samples x num_time_steps)
  i.e. (10000 x 449)
* "selectedTimeSteps.txt": Indices time steps selected using the time step selection algorithm

