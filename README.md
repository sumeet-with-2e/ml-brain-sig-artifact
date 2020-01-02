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

## WEEK 1

03-12 to 06-12    
Introduction to EEG  
BCI, BSS, PCA, ICA(technique and code)  
Time Series Analysis, Power Spectrum Topographs
https://www.researchgate.net/publication/209153969_Classification_of_Artifactual_ICA_Components

## WEEK 2

07-12 to 11-12    
Fourier transform, frequency domain analysis  
Statistical feature of time domain and frequency domain
https://www.researchgate.net/publication/51541331_Automatic_Classification_of_Artifactual_ICA-Components_for_Artifact_Removal_in_EEG_Signals

## WEEK 3

16-12 to 20-12 SVM and Neural network based classifier(Algorithms, working and code), v1.0

## WEEK 4

### 23-12 

SVM applied on a sample data available online(accuracy 0.99)

   Results-->
    
[[147   2]
 [  1 125]]
 
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       149
           1       0.98      0.99      0.99       126

    accuracy                           0.99       275
   macro avg       0.99      0.99      0.99       275
weighted avg       0.99      0.99      0.99       275

### 24-12   
Code to extract features from available EEG data changed to load all files present in current directory.
Started off with transferring extracted data into one file 

### 25-12   
Studied SVM concepts

New Release! Code was updated to extract frequency domain features and convert time series data to frequency domain data.
Working to create single .npy file containg whole data

### 26-12

Read the structure of recieved training data, 
Wrote Python code to extract data from mat file and create a Pandas DataFrame

2 separate dataframes were made: X which contains the statistical features of time series data

and y which contains 1 or 0 values depicting whether its a brain signal or not respectively.

### 27-12

Linear SVM applied to achive binary classification into brain signals and artifacts

Following results were obtained:

[[219   0]
 [ 17   0]]
 
              precision    recall  f1-score   support

           0       0.93      1.00      0.96       219
           1       0.00      0.00      0.00        17

    accuracy                           0.93       236
   macro avg       0.46      0.50      0.48       236  
weighted avg       0.86      0.93      0.89       236

### 28-12

Changing the aim from making a binary classifier to a multi class classifier 
which can clssify obtained data into following 7 classes:

Brain, Muscle, Eye, Heart, Line Noise, Channel noise, Other

### 29-12

Learned how to manually classify and tell components apart i.e labelling the given Independent Components.

Read the online IC label repository available here
https://gin.g-node.org/doi/ICLabel-Dataset

### 30-12

Removed the biased nature of data

Python Code to count number of brain signals in given data and make another dataset of randomly selected non-brain signals 
and create a single dataframe containing both type of signals in equal numbers.

Results:

[[18  2]  
 [11  4]]
              precision    recall  f1-score   support

         0.0       0.62      0.90      0.73        20
         1.0       0.67      0.27      0.38        15

    accuracy                           0.63        35
   macro avg       0.64      0.58      0.56        35  
weighted avg       0.64      0.63      0.58        35  

### 31-12

Train, test split changed to 20% for testing set

New EEG files added, size of dataset increased

Results:

[[39 14]  
 [24 33]]
              precision    recall  f1-score   support

         0.0       0.62      0.74      0.67        53
         1.0       0.70      0.58      0.63        57

    accuracy                           0.65       110
   macro avg       0.66      0.66      0.65       110  
weighted avg       0.66      0.65      0.65       110  

### 1-1

Trying to add Frequency features 
Same Results obtained
