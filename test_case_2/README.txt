This the data for Test Case 2: Synthetic dataset simulated using the Courtemanche
human atrial model.
These datasets comprise AP biomarkers ordered as follows:
index:       0     1     2    3   4     5     6    7     8 
biomarker: APD90 APD50 APD30 APA RMP dVdtMax V20 Vnotch AUC

List of files and description:

- "simu_courtemanche_control.txt": simulated APs in control conditions
  (stimulation frequency f = 1Hz). It is a matrix of size (number_of_samples x num_biomarkers)
  i.e. (32768 x 9)
- "synth_courtemanche_control.txt": synthetic APs in control conditions
  (stimulation frequency f = 1Hz). It is a matrix of size (number_of_samples x num_biomarkers)
  i.e. (10000 x 9)
- "simu_courtemanche_2Hz.txt": simulated APs in fast pacing conditions
  (stimulation frequency f = 2Hz). It is a matrix of size (number_of_samples x num_biomarkers)
  i.e. (32768 x 9)
- "synth_courtemanche_control.txt": synthetic APs in fast pacing conditions
  (stimulation frequency f = 2Hz). It is a matrix of size (number_of_samples x num_biomarkers)
  i.e. (10000 x 9)

