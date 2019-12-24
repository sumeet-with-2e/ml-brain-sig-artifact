#!/usr/bin/env python
# coding: utf-8

# In[1]:


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



fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 18
fig_size[1] = 4
plt.rcParams["figure.figsize"] = fig_size


# In[3]:


for filename in os.listdir(os.getcwd()):
    mat=spio.loadmat(filename)
    data=mat['EEG'][0][0][16]
    mn=spio.mean(data, axis=1)
    mdn=spio.median(data, axis=1)
    sd=spio.std(data, axis=1)
    krts=stats.kurtosis(data, axis=1)
    qntle=np.quantile(data, 0.75, axis=1)
    skw=stats.skew(data, axis=1)


# In[11]:


np.shape(data)[1]


# In[33]:


plt.plot(data[4])


# In[13]:


plt.ylabel('Mean')
plt.xlabel('Channels')
plt.plot(mn)


# In[14]:


plt.ylabel('Median')
plt.xlabel('Channels')
plt.plot(mdn)


# In[15]:


plt.ylabel('Standard Deviation')
plt.xlabel('Channels')
plt.plot(sd)


# In[16]:


plt.ylabel('Kurtosis')
plt.xlabel('Channels')
plt.plot(krts)


# In[17]:


plt.ylabel('Quantile')
plt.xlabel('Channels')
plt.plot(qntle)


# In[18]:


plt.ylabel('Skewness')
plt.xlabel('Channels')
plt.plot(skw)


# In[19]:


dataf=data
dataf=np.abs(sft.fft(dataf))


# In[20]:


mnf=spio.mean(dataf, axis=1)


# In[21]:


mdnf=spio.median(dataf, axis=1)


# In[22]:


sdf=spio.std(dataf, axis=1)


# In[23]:


krtsf=stats.kurtosis(dataf, axis=1)


# In[24]:


qntlef=np.quantile(dataf, 0.75, axis=1)


# In[25]:


skwf=stats.skew(dataf, axis=1)


# In[26]:


plt.ylabel('Meanf')
plt.xlabel('Channels')
plt.plot(mnf)


# In[27]:


plt.ylabel('Medianf')
plt.xlabel('Channels')
plt.plot(mdnf)


# In[28]:


plt.ylabel('Standard Deviationf')
plt.xlabel('Channels')
plt.plot(sdf)


# In[29]:


plt.ylabel('Kurtosisf')
plt.xlabel('Channels')
plt.plot(krtsf)


# In[30]:


plt.ylabel('Quantilef')
plt.xlabel('Channels')
plt.plot(qntlef)


# In[31]:


plt.ylabel('Skewnessf')
plt.xlabel('Channels')
plt.plot(skwf)


# In[ ]:




