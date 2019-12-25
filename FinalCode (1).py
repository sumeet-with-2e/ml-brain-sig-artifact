#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[3]:


cwd=os.getcwd()
print(cwd)

#loading all mat files of current directory
for filename in os.listdir(os.getcwd()): 

    if filename.endswith(".mat"):
        #loading mat file
        mat=sio.loadmat(filename)
        #Extracting ICA values stored at 16th index
        data=mat['EEG'][0][0][16]
        #data contains time series values
        
        mn=spio.mean(data, axis=1)
        
        mdn=spio.median(data, axis=1)
        
        sd=spio.std(data, axis=1)
        
        krts=stats.kurtosis(data, axis=1)
        
        qntle=np.quantile(data, 0.75, axis=1)
        
        skw=stats.skew(data, axis=1)


# In[30]:


dataf=data
dataf=np.abs(sft.fft(dataf))
freqs=sft.fftfreq(len(dataf[0]))*250
plt.plot(freqs, dataf[0])


# In[11]:


mnf=spio.mean(dataf, axis=1)


# In[12]:


mdnf=spio.median(dataf, axis=1)


# In[13]:


sdf=spio.std(dataf, axis=1)


# In[14]:


krtsf=stats.kurtosis(dataf, axis=1)


# In[15]:


qntlef=np.quantile(dataf, 0.75, axis=1)


# In[16]:


skwf=stats.skew(dataf, axis=1)


# In[4]:


plt.ylabel('Mean')
plt.xlabel('Channels')
plt.plot(mn)


# In[5]:


plt.ylabel('Median')
plt.xlabel('Channels')
plt.plot(mdn)


# In[6]:


plt.ylabel('Standard Deviation')
plt.xlabel('Channels')
plt.plot(sd)


# In[7]:


plt.ylabel('Kurtosis')
plt.xlabel('Channels')
plt.plot(krts)


# In[8]:


plt.ylabel('Quantile')
plt.xlabel('Channels')
plt.plot(qntle)


# In[9]:


plt.ylabel('Skewness')
plt.xlabel('Channels')
plt.plot(skw)


# In[17]:


plt.ylabel('Meanf')
plt.xlabel('Channels')
plt.plot(mnf)


# In[18]:


plt.ylabel('Medianf')
plt.xlabel('Channels')
plt.plot(mdnf)


# In[19]:


plt.ylabel('Standard Deviationf')
plt.xlabel('Channels')
plt.plot(sdf)


# In[20]:


plt.ylabel('Kurtosisf')
plt.xlabel('Channels')
plt.plot(krtsf)


# In[21]:


plt.ylabel('Quantilef')
plt.xlabel('Channels')
plt.plot(qntlef)


# In[22]:


plt.ylabel('Skewnessf')
plt.xlabel('Channels')
plt.plot(skwf)


# In[ ]:




