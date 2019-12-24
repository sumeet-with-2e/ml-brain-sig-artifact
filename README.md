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

03-12 to 06-12  EEG, BCI, BSS, PCA, ICA(technique and code), Time Series Analysis, Power Spectrum Topographs
https://www.researchgate.net/publication/209153969_Classification_of_Artifactual_ICA_Components

07-12 to 11-12  Fourier transform, frequency domain analysis, Statistical feature of time domain and frequency domain
https://www.researchgate.net/publication/51541331_Automatic_Classification_of_Artifactual_ICA-Components_for_Artifact_Removal_in_EEG_Signals

16-12 to 20-12 SVM and Neural network based classifier(Algorithms, working and code), v1.0
23-12 SVM applied on a sample data available online(accuracy 0.99)
    Results-->
    
(1372, 5)
   Variance  Skewness  Curtosis  Entropy  Class
0   3.62160    8.6661   -2.8073 -0.44699      0
1   4.54590    8.1674   -2.4586 -1.46210      0
2   3.86600   -2.6383    1.9242  0.10645      0
3   3.45660    9.5228   -4.0112 -3.59440      0
4   0.32924   -4.4552    4.5718 -0.98880      0
[[147   2]
 [  1 125]]
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       149
           1       0.98      0.99      0.99       126

    accuracy                           0.99       275
   macro avg       0.99      0.99      0.99       275
weighted avg       0.99      0.99      0.99       275
