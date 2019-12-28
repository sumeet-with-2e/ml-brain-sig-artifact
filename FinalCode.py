#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Getting the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy as spio
import scipy.stats as stats
import sunpy.timeseries
import scipy.fftpack as sft
import scipy.io as sio
import pandas as pd
import pdb 
import os


# In[2]:


#adjusting plot size to be viewed
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 18
fig_size[1] = 4
plt.rcParams["figure.figsize"] = fig_size


# In[32]:


cwd=os.getcwd()
print(cwd)
df=pd.DataFrame()
dfc=pd.DataFrame()
dfc['Classes']=0
#loading all mat files of current directory
for filename in os.listdir(os.getcwd()): 
    if filename.endswith(".mat"):
        #loading mat file
        mat=sio.loadmat(filename)
        #Extracting ICA values stored at 16th index
        data=mat['EEG'][0][0][16]
        #data contains time series values
        datacls=mat['EEG'][0][0][39][0][0][4][0][0][0][0][0][1]
        #datacls contains the data of probability of respective signal
        #belonging to either of the 7 classes where first is brain
        c=0
        for i in datacls:
            mx1=max(datacls[c])
            if datacls[c][0]==mx1:
                t=1
            else:
                t=0
            dfc=dfc.append({"Classes":t}, ignore_index=True)
            c=c+1
        #NOW dfc is a dataframe which contains 1 for brain signals and 0 for the 
        #signals which are not from brain
        mn=spio.mean(data, axis=1)
        dft=pd.DataFrame(mn, columns=['Mean'])
        mdn=spio.median(data, axis=1)
        dft['Medain']=mdn
        sd=spio.std(data, axis=1)
        dft['Std Deviation']=sd
        krts=stats.kurtosis(data, axis=1)
        dft['Kurtosis']=krts
        qntle=np.quantile(data, 0.75, axis=1)
        dft['Quantile']=qntle
        skw=stats.skew(data, axis=1)  
        dft['Skewness']=skw
        df=df.append(dft, ignore_index=True)
        #df DataFrame holds 6 columns(statistical features of the signals)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(dfc)


# In[69]:


X=df
conv_arr= dfc.values
y=np.delete(conv_arr,[1,2],axis=1)
y=y.ravel()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[73]:


#dataf=data
#dataf=np.abs(sft.fft(dataf))
#freqs=sft.fftfreq(len(dataf[0]))*250
#plt.plot(freqs, dataf[0])
datacls1=mat['EEG'][0][0][39][0][0][4][0][0][0][0][0][0]
print(datacls1)


# In[47]:


#mnf=spio.mean(dataf, axis=1)

#mdnf=spio.median(dataf, axis=1)

#sdf=spio.std(dataf, axis=1)

#krtsf=stats.kurtosis(dataf, axis=1)

#qntlef=np.quantile(dataf, 0.75, axis=1)

#skwf=stats.skew(dataf, axis=1)


# In[ ]:



