This the data for Test Case 3: Experimental measurements of canine ventricular
cardiomyocyte APs.

List of files and description:

- directory "experimental_data_from_johnstone_jmcc/": In this directory are
  the experimental AP traces studied in the article. They are a subset of
  experimental data available online (see link in our manuscript).
- "simu_davies.txt": simulated APs using the Davies canine model
  (stimulation frequency f = 1Hz). It is a matrix of size (number_of_samples x num_biomarkers)
  i.e. (8192 x 3). Each column corresponds to a biomarker in the following
  order: APD90, APD50, Vnotch
