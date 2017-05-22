This the data for Test Case 4: Experimental dataset of human atrial
cardiomyocyte APs.
These datasets comprise AP biomarkers ordered as follows:
index:       0     1     2    3   4     5     6  
biomarker: APD90 APD50 APD20 APA RMP dVdtMax V20

List of files and description:

- "expData_sr.txt": experimental APs from the Sinus Rythm group
  It is a matrix of size (number_of_samples x num_biomarkers), i.e. (254 x 7)
- "expData_af.txt": experimental APs from the Atrial Fibrillation group
  It is a matrix of size (number_of_samples x num_biomarkers), i.e. (215 x 7)
- "simu_courtemanche_sr.txt": simulated APs using the Courtemanche model
  calibrated for the SR group
  It is a matrix of size (number_of_samples x num_biomarkers), i.e. (16384 x 7)
- "simu_courtemanche_af.txt": simulated APs using the Courtemanche model
  calibrated for the AF group. 
  It is a matrix of size (number_of_samples x num_biomarkers), i.e. (16384 x 7)
