# ml-brain-sig-artifact

Machine Learning model to Classify between Brain Signals and EEG Artifacts

The classification of brain signals and other artifacts is still an authoritarian
problem in the sense that someone with highly experienced in looking at the brain
signals can classify what is brain signal and what is brain artifacts. There is a need
to create a machine learning based tool which can classify between the brain
signals and brain artifacts.

The objective of this project is to create a machine learning based framework
which takes independent components as inputs and classify them in the brain
signals and brain artifacts.

Tools and technique used
1. Time and frequency domain statistical features.
2. SVM or neural network based classifiers.

WEEK 1

03-12 to 06-12  EEG, BCI, BSS, PCA, ICA(technique and code), Time Series Analysis, Power Spectrum Topographs
https://www.researchgate.net/publication/209153969_Classification_of_Artifactual_ICA_Components

WEEK 2

07-12 to 11-12  Fourier transform, frequency domain analysis, Statistical feature of time domain and frequency domain
https://www.researchgate.net/publication/51541331_Automatic_Classification_of_Artifactual_ICA-Components_for_Artifact_Removal_in_EEG_Signals

WEEK 3

16-12 to 20-12 SVM and Neural network based classifier(Algorithms, working and code), v1.0

WEEK 4

23-12 SVM applied on a sample data available online(accuracy 0.99)

   Results-->
    
[[147   2]
 [  1 125]]
 
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       149
           1       0.98      0.99      0.99       126

    accuracy                           0.99       275
   macro avg       0.99      0.99      0.99       275
weighted avg       0.99      0.99      0.99       275

24-12 Code to extract features from available EEG data changed to load all files present in current directory.
Started off with transferring extracted data into one file 

25-12 
Studied SVM concepts

New Release! Code was updated to extract frequency domain features and convert time series data to frequency domain data.
Working to create single .npy file containg whole data
