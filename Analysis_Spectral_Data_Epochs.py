# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:27:42 2024

@author: tvanneau
"""

#%% Analysis of power for epochs cognition - Flow and No Flow conditions

# Load pickle file with corresponding power data 
import os
import pickle
import mne
import matplotlib.pyplot as plt

# Define baseline range (in seconds)
baseline = (-0.2, 0.0)

#%% Audiovisual stim

# AV interference target
with open('Power_StimulusOnset_AV_interference_Target.pkl', 'rb') as f:
    [Power_AV_Inf_Tar,Power_NPL_AV_Inf_Tar,ITPC_AV_Inf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_AV_Inf_Tar)):
    Power_NPL_AV_Inf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_AV_Inf_Tar = mne.grand_average(Power_NPL_AV_Inf_Tar)
M_ITPC_AV_Inf_Tar = mne.grand_average(ITPC_AV_Inf_Tar)


# AV non-interference target
with open('Power_StimulusOnset_AV_noninterference_Target.pkl', 'rb') as f:
    [Power_AV_NInf_Tar,Power_NPL_AV_NInf_Tar,ITPC_AV_NInf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_AV_NInf_Tar)):
    Power_NPL_AV_NInf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_AV_NInf_Tar = mne.grand_average(Power_NPL_AV_NInf_Tar)
M_ITPC_AV_NInf_Tar = mne.grand_average(ITPC_AV_NInf_Tar)


# AV interference non-target
with open('Power_StimulusOnset_AV_interference_Nontarget.pkl', 'rb') as f:
    [Power_AV_Inf_NTar,Power_NPL_AV_Inf_NTar,ITPC_AV_Inf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_AV_Inf_NTar)):
    Power_NPL_AV_Inf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_AV_Inf_NTar = mne.grand_average(Power_NPL_AV_Inf_NTar)
M_ITPC_AV_Inf_NTar = mne.grand_average(ITPC_AV_Inf_NTar)


# AV non-interference non-target
with open('Power_StimulusOnset_AV_noninterference_Nontarget.pkl', 'rb') as f:
    [Power_AV_NInf_NTar,Power_NPL_AV_NInf_NTar,ITPC_AV_NInf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_AV_NInf_NTar)):
    Power_NPL_AV_NInf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_AV_NInf_NTar = mne.grand_average(Power_NPL_AV_NInf_NTar)
M_ITPC_AV_NInf_NTar = mne.grand_average(ITPC_AV_NInf_NTar)

#%% Visual stim

# V interference target
with open('Power_StimulusOnset_V_interference_Target.pkl', 'rb') as f:
    [Power_V_Inf_Tar,Power_NPL_V_Inf_Tar,ITPC_V_Inf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_V_Inf_Tar)):
    Power_NPL_V_Inf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_V_Inf_Tar = mne.grand_average(Power_NPL_V_Inf_Tar)
M_ITPC_V_Inf_Tar = mne.grand_average(ITPC_V_Inf_Tar)


# V non-interference target
with open('Power_StimulusOnset_V_noninterference_Target.pkl', 'rb') as f:
    [Power_V_NInf_Tar,Power_NPL_V_NInf_Tar,ITPC_V_NInf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_V_NInf_Tar)):
    Power_NPL_V_NInf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_V_NInf_Tar = mne.grand_average(Power_NPL_V_NInf_Tar)
M_ITPC_V_NInf_Tar = mne.grand_average(ITPC_V_NInf_Tar)


# V interference non-target
with open('Power_StimulusOnset_V_interference_Nontarget.pkl', 'rb') as f:
    [Power_V_Inf_NTar,Power_NPL_V_Inf_NTar,ITPC_V_Inf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_V_Inf_NTar)):
    Power_NPL_V_Inf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_V_Inf_NTar = mne.grand_average(Power_NPL_V_Inf_NTar)
M_ITPC_V_Inf_NTar = mne.grand_average(ITPC_V_Inf_NTar)


# V non-interference non-target
with open('Power_StimulusOnset_V_noninterference_Nontarget.pkl', 'rb') as f:
    [Power_V_NInf_NTar,Power_NPL_V_NInf_NTar,ITPC_V_NInf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_V_NInf_NTar)):
    Power_NPL_V_NInf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_V_NInf_NTar = mne.grand_average(Power_NPL_V_NInf_NTar)
M_ITPC_V_NInf_NTar = mne.grand_average(ITPC_V_NInf_NTar)


#%% Auditory stim

# A interference target
with open('Power_StimulusOnset_A_interference_Target.pkl', 'rb') as f:
    [Power_A_Inf_Tar,Power_NPL_A_Inf_Tar,ITPC_A_Inf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_A_Inf_Tar)):
    Power_NPL_A_Inf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_A_Inf_Tar = mne.grand_average(Power_NPL_A_Inf_Tar)
M_ITPC_A_Inf_Tar = mne.grand_average(ITPC_A_Inf_Tar)


# A non-interference target
with open('Power_StimulusOnset_A_noninterference_Target.pkl', 'rb') as f:
    [Power_A_NInf_Tar,Power_NPL_A_NInf_Tar,ITPC_A_NInf_Tar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_A_NInf_Tar)):
    Power_NPL_A_NInf_Tar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_A_NInf_Tar = mne.grand_average(Power_NPL_A_NInf_Tar)
M_ITPC_A_NInf_Tar = mne.grand_average(ITPC_A_NInf_Tar)


# A interference non-target
with open('Power_StimulusOnset_A_interference_Nontarget.pkl', 'rb') as f:
    [Power_A_Inf_NTar,Power_NPL_A_Inf_NTar,ITPC_A_Inf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_A_Inf_NTar)):
    Power_NPL_A_Inf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_A_Inf_NTar = mne.grand_average(Power_NPL_A_Inf_NTar)
M_ITPC_A_Inf_NTar = mne.grand_average(ITPC_A_Inf_NTar)


# A non-interference non-target
with open('Power_StimulusOnset_A_noninterference_Nontarget.pkl', 'rb') as f:
    [Power_A_NInf_NTar,Power_NPL_A_NInf_NTar,ITPC_A_NInf_NTar] = pickle.load(f)

# Apply baseline correction to each subject's power
for i in range(len(Power_NPL_A_NInf_NTar)):
    Power_NPL_A_NInf_NTar[i].apply_baseline(baseline=baseline, mode='percent')

M_Power_NPL_A_NInf_NTar = mne.grand_average(Power_NPL_A_NInf_NTar)
M_ITPC_A_NInf_NTar = mne.grand_average(ITPC_A_NInf_NTar)

#%% Plot topomap of specific frequencies at specific time points - Non-interference with targets

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(3, 4, figsize=(10, 8))

# fig, axes = plt.subplots(1, 4, figsize=(10, 8))


# Theta
fmin=3
fmax=7

tmin1, tmin2, tmin3, tmin4 = 0.0, 0.25, 0.5, 0.75
tmax1, tmax2, tmax3, tmax4 = 0.25, 0.5, 0.75, 1.0

# Theta

#Audiovisual scale
vlim1 = -0.2
vlim2= 0.2

M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0, 0], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0,1], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0,2], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0, 3], show=False)

M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1, 0], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1,1], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1,2], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1, 3], show=False)

M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2, 0], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2,1], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2,2], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2, 3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%% Plot topomap of specific frequencies at specific time points - Non-interference with targets

# Theta activity for total and non-phase locked power at specific time points

# Create a figure with a grid of subplots (4 rows, 2 columns)
fig, axes = plt.subplots(3, 4, figsize=(10, 8))

# Alpha
fmin=7
fmax=13

tmin1, tmin2, tmin3, tmin4 = 0.0, 0.25, 0.5, 0.75
tmax1, tmax2, tmax3, tmax4 = 0.25, 0.5, 0.75, 1.0

# Theta

#Audiovisual scale
vlim1 = -0.2
vlim2= 0.2

M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0, 0], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0,1], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0,2], show=False)
M_Power_NPL_AV_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[0, 3], show=False)

M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1, 0], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1,1], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1,2], show=False)
M_Power_NPL_V_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[1, 3], show=False)

M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin1, tmax=tmax1, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2, 0], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin2, tmax=tmax2, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2,1], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin3, tmax=tmax3, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2,2], show=False)
M_Power_NPL_A_NInf_Tar.plot_topomap(tmin=tmin4, tmax=tmax4, fmin=fmin, fmax=fmax, baseline=None, cmap='jet', vlim=(vlim1, vlim2), axes=axes[2, 3], show=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

#%% Time-frequency maps

# Centro-frontal - Auditory stimulation

# Parieto-occipital cluster
Electrodes = ['A1']

# Fronto-central cluster
# Electrodes = ['FC1','FCz','FC2','F1','Fz','F2']

# TD flow and no flow
M_Power_NPL_AV_NInf_Tar.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=1.2,vlim=(-0.2,0.2),fmin=3,fmax=40)
plt.grid(False)

# TD flow and no flow
M_Power_NPL_A_NInf_Tar.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.1, tmax=1.2,vlim=(-0.2,0.2),fmin=3,fmax=40)
plt.grid(False)


#%% Time-frequency maps

# Centro-frontal - Auditory stimulation

# Parieto-occipital cluster
Electrodes = ['C3','C1','CP3','CP1']

# Fronto-central cluster
# Electrodes = ['FC1','FCz','FC2','F1','Fz','F2']

# TD flow and no flow
M_Power_NPL_NT.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.05, tmax=0.35,vlim=(-0.2,0.2),fmin=7,fmax=35)
plt.grid(False)

M_Power_NPL_Dev_NT.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.05, tmax=0.35,vlim=(-0.2,0.2),fmin=7,fmax=35)
plt.grid(False)

M_Power_NPL_AU.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.05, tmax=0.35,vlim=(-0.2,0.2),fmin=7,fmax=35)
plt.grid(False)

M_Power_NPL_Dev_AU.plot(Electrodes,baseline=None,  cmap='jet',combine='mean', tmin=-0.05, tmax=0.35,vlim=(-0.2,0.2),fmin=7,fmax=35)
plt.grid(False)

#%% Alpha suppression for Total power
import numpy as np

freqs = np.linspace(*np.array([7, 40]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['C3','C1','CP3','CP1']

tmin = -0.05
tmax = 0.35

# Alpha_min = 0 # 7Hz
# Alpha_max = 18 # 13Hz

Alpha_min = 19 # 7Hz
Alpha_max = 54 # 13Hz

Fq_NT = []
Fq_AU = []

Fq_Dev_NT = []
Fq_Dev_AU = []


for i in range(0,len(Power_NPL_NT),1):
    Aph_NT = Power_NPL_NT[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_NT = np.mean(np.mean(Aph_NT, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Fq_NT.append(Fa_NT)
    
for i in range(0,len(Power_NPL_Dev_NT),1):
    Aph_Dev_NT = Power_NPL_Dev_NT[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_Dev_NT = np.mean(np.mean(Aph_Dev_NT, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Fq_Dev_NT.append(Fa_Dev_NT)
    
for i in range(0,len(Power_NPL_AU),1):
    Aph_AU = Power_NPL_AU[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_AU = np.mean(np.mean(Aph_AU, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Fq_AU.append(Fa_AU)
    
for i in range(0,len(Power_NPL_Dev_AU),1):
    Aph_Dev_AU = Power_NPL_Dev_AU[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_Dev_AU = np.mean(np.mean(Aph_Dev_AU, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Fq_Dev_AU.append(Fa_Dev_AU)
    
fig, ax = plt.subplots()

Mean_NT = np.mean(np.array( Fq_NT),axis=0)
Mean_Dev_NT = np.mean(np.array( Fq_Dev_NT),axis=0)

Mean_AU = np.mean(np.array( Fq_AU),axis=0)
Mean_Dev_AU = np.mean(np.array( Fq_Dev_AU),axis=0)

SEM_NT = np.std(np.array(Fq_NT), axis=0) / np.sqrt(len(Fq_NT))
SEM_Dev_NT = np.std(np.array(Fq_Dev_NT), axis=0) / np.sqrt(len(Fq_Dev_NT))

SEM_AU = np.std(np.array(Fq_AU), axis=0) / np.sqrt(len(Fq_AU))
SEM_Dev_AU = np.std(np.array(Fq_Dev_AU), axis=0) / np.sqrt(len(Fq_Dev_AU))


x = np.linspace(-0.05,0.35,52)

ax.plot(x, Mean_NT, label = 'Std_NT')
ax.fill_between(x, Mean_NT - SEM_NT, Mean_NT + SEM_NT, alpha=0.2)

ax.plot(x, Mean_Dev_NT, label = 'Dev_NT')
ax.fill_between(x, Mean_Dev_NT - SEM_Dev_NT, Mean_Dev_NT + SEM_Dev_NT, alpha=0.2)

ax.plot(x, Mean_AU, label = 'Std_AU')
ax.fill_between(x, Mean_AU - SEM_AU, Mean_AU + SEM_AU, alpha=0.2)

ax.plot(x, Mean_Dev_AU, label = 'Dev_AU')
ax.fill_between(x, Mean_Dev_AU - SEM_Dev_AU, Mean_Dev_AU + SEM_Dev_AU, alpha=0.2)

ax.legend()


#%% Alpha suppression for Total power
import numpy as np

freqs = np.linspace(*np.array([4, 35]), num=60) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']

tmin = -0.1
tmax = 0.6

Alpha_min = 6 # 7Hz
Alpha_max = 17 # 13Hz

Alpha_suppresion_flow_TD = []
Alpha_suppresion_no_flow_TD = []


for i in range(0,len(Power_NPL_flow_TD),1):
     
    Aph_flow = Power_NPL_flow_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_flow_TD = np.mean(np.mean(Aph_flow, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_flow_TD.append(Fa_flow_TD)
    
for i in range(0,len(Power_NPL_no_flow_TD),1):
     
    Aph_no_flow = Power_NPL_no_flow_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_no_flow_TD = np.mean(np.mean(Aph_no_flow, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_no_flow_TD.append(Fa_no_flow_TD)
    

fig, ax = plt.subplots()

Mean_flow_TD = np.mean(np.array( Alpha_suppresion_flow_TD),axis=0)
Mean_no_flow_TD = np.mean(np.array( Alpha_suppresion_no_flow_TD),axis=0)

SEM_flow_TD = np.std(np.array(Alpha_suppresion_flow_TD), axis=0) / np.sqrt(len(Alpha_suppresion_flow_TD))
SEM_no_flow_TD = np.std(np.array(Alpha_suppresion_no_flow_TD), axis=0) / np.sqrt(len(Alpha_suppresion_no_flow_TD))

x = np.linspace(-0.1,0.6,181)

ax.plot(x, Mean_flow_TD, label = 'Flow TD')
ax.fill_between(x, Mean_flow_TD - SEM_flow_TD, Mean_flow_TD + SEM_flow_TD, alpha=0.2)

ax.plot(x, Mean_no_flow_TD, label = 'No Flow TD')
ax.fill_between(x, Mean_no_flow_TD - SEM_no_flow_TD, Mean_no_flow_TD + SEM_no_flow_TD, alpha=0.2)

ax.legend()







#%% Peak to Peak
import numpy as np

freqs = np.linspace(*np.array([3, 40]), num=200) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
# channels = ['T7','TP7','T8','TP8']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.05
tmax = 0.6

# Alpha_min = 0 # 3Hz
# Alpha_max = 21 # 7Hz

Alpha_min = 22 # 7Hz
Alpha_max = 53 # 13Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

times_idx = np.linspace(-0.05,0.6,334)

# To find maximal peak
# for i in range(0,len(Power_V_all_TD),1):
     
#     Aph_TD = Power_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_TD = np.max(Fa_TD)
#     peak_latency_TD = times_idx[np.argmax(Fa_TD)]
#     Alpha_suppresion_TD.append((peak_amplitude_TD, peak_latency_TD))
    
# for i in range(0,len(Power_V_all_SIB),1):
     
#     Aph_SIB = Power_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_SIB = np.max(Fa_SIB)
#     peak_latency_SIB = times_idx[np.argmax(Fa_SIB)]
#     Alpha_suppresion_SIB.append((peak_amplitude_SIB, peak_latency_SIB))
    
# for i in range(0,len(Power_V_all_ASD),1):
     
#     Aph_ASD = Power_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_ASD = np.max(Fa_ASD)
#     peak_latency_ASD = times_idx[np.argmax(Fa_ASD)]
#     Alpha_suppresion_ASD.append((peak_amplitude_ASD, peak_latency_ASD))
    
# To find minimun peak
for i in range(0,len(Power_V_all_TD),1):
     
    Aph_TD = Power_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_TD = np.min(Fa_TD)
    peak_latency_TD = times_idx[np.argmin(Fa_TD)]
    Alpha_suppresion_TD.append((peak_amplitude_TD, peak_latency_TD))
    
for i in range(0,len(Power_V_all_SIB),1):
     
    Aph_SIB = Power_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_SIB = np.min(Fa_SIB)
    peak_latency_SIB = times_idx[np.argmin(Fa_SIB)]
    Alpha_suppresion_SIB.append((peak_amplitude_SIB, peak_latency_SIB))
    
for i in range(0,len(Power_V_all_ASD),1):
     
    Aph_ASD = Power_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_ASD = np.min(Fa_ASD)
    peak_latency_ASD = times_idx[np.argmin(Fa_ASD)]
    Alpha_suppresion_ASD.append((peak_amplitude_ASD, peak_latency_ASD))

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[0] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[0] for x in Alpha_suppresion_SIB]
peak_amplitudes_2 = [x[0] for x in Alpha_suppresion_ASD]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[1] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[1] for x in Alpha_suppresion_SIB]
peak_amplitudes_2 = [x[1] for x in Alpha_suppresion_ASD]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%% Alpha suppression for Induced power
import numpy as np

freqs = np.linspace(*np.array([3, 20]), num=100) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
# channels = ['T7','T8','FT7','FT8','FC5','C5','FC6','C6']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2','C1','Cz','C2']
# channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.1
tmax = 0.6

# Alpha_min = 0 # 3Hz
# Alpha_max = 21 # 7Hz

Alpha_min = 24 # 7Hz
Alpha_max = 59 # 13Hz

# Alpha_min = 58 # 13Hz
# Alpha_max = 147 # 30Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

for i in range(0,len(Power_V_all_TD),1):
     
    Aph_TD = Power_NPL_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_TD.append(Fa_TD)
    
for i in range(0,len(Power_V_all_SIB),1):
     
    Aph_SIB = Power_NPL_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_SIB.append(Fa_SIB)
    
for i in range(0,len(Power_V_all_ASD),1):
     
    Aph_ASD = Power_NPL_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_ASD.append(Fa_ASD)

fig, ax = plt.subplots()

Mean_TD = np.mean(np.array( Alpha_suppresion_TD),axis=0)
Mean_SIB = np.mean(np.array( Alpha_suppresion_SIB),axis=0)
Mean_ASD = np.mean(np.array( Alpha_suppresion_ASD),axis=0)

SEM_TD = np.std(np.array(Alpha_suppresion_TD), axis=0) / np.sqrt(len(Alpha_suppresion_TD))
SEM_SIB = np.std(np.array(Alpha_suppresion_SIB), axis=0) / np.sqrt(len(Alpha_suppresion_SIB))
SEM_ASD = np.std(np.array(Alpha_suppresion_ASD), axis=0) / np.sqrt(len(Alpha_suppresion_ASD))

x = np.linspace(-0.1,0.6,359)

ax.plot(x, Mean_TD, label = 'TD')
ax.fill_between(x, Mean_TD - SEM_TD, Mean_TD + SEM_TD, alpha=0.2)

ax.plot(x, Mean_SIB, label = 'SIB')
ax.fill_between(x, Mean_SIB - SEM_SIB, Mean_SIB + SEM_SIB, alpha=0.2)

ax.plot(x, Mean_ASD, label = 'ASD')
ax.fill_between(x, Mean_ASD - SEM_ASD, Mean_ASD + SEM_ASD, alpha=0.2)
# ax.set_ylim(-0.02,0.18) # For theta power
ax.set_ylim(-0.1,0.02)
ax.legend()

#%% Theta frontal for Induced power
import numpy as np

freqs = np.linspace(*np.array([3, 40]), num=200) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
# channels = ['T7','T8','FT7','FT8','FC5','C5','FC6','C6']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2','C1','Cz','C2']
channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.1
tmax = 0.6

Alpha_min = 0 # 3Hz
Alpha_max = 21 # 7Hz

# Alpha_min = 22 # 7Hz
# Alpha_max = 53 # 13Hz

# Alpha_min = 58 # 13Hz
# Alpha_max = 147 # 30Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

for i in range(0,len(Power_V_all_TD),1):
     
    Aph_TD = Power_NPL_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_TD.append(Fa_TD)
    
for i in range(0,len(Power_V_all_SIB),1):
     
    Aph_SIB = Power_NPL_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_SIB.append(Fa_SIB)
    
for i in range(0,len(Power_V_all_ASD),1):
     
    Aph_ASD = Power_NPL_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_ASD.append(Fa_ASD)

fig, ax = plt.subplots()

Mean_TD = np.mean(np.array( Alpha_suppresion_TD),axis=0)
Mean_SIB = np.mean(np.array( Alpha_suppresion_SIB),axis=0)
Mean_ASD = np.mean(np.array( Alpha_suppresion_ASD),axis=0)

SEM_TD = np.std(np.array(Alpha_suppresion_TD), axis=0) / np.sqrt(len(Alpha_suppresion_TD))
SEM_SIB = np.std(np.array(Alpha_suppresion_SIB), axis=0) / np.sqrt(len(Alpha_suppresion_SIB))
SEM_ASD = np.std(np.array(Alpha_suppresion_ASD), axis=0) / np.sqrt(len(Alpha_suppresion_ASD))

x = np.linspace(-0.1,0.6,359)

ax.plot(x, Mean_TD, label = 'TD')
ax.fill_between(x, Mean_TD - SEM_TD, Mean_TD + SEM_TD, alpha=0.2)

ax.plot(x, Mean_SIB, label = 'SIB')
ax.fill_between(x, Mean_SIB - SEM_SIB, Mean_SIB + SEM_SIB, alpha=0.2)

ax.plot(x, Mean_ASD, label = 'ASD')
ax.fill_between(x, Mean_ASD - SEM_ASD, Mean_ASD + SEM_ASD, alpha=0.2)

ax.legend()

#%% Permutation test between averaged ERP curves

import numpy as np
import matplotlib.pyplot as plt
import mne
from scipy.stats import t
from mne.stats import permutation_cluster_test, ttest_ind_no_p

# visual_channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# visual_channels = ['FC1','FCz','FC2','F1','Fz','F2']
visual_channels = ['T7','T8','FT7','FT8']

# Function to average ERP over specific channels
def average_erp_channels(erp, channel_list):
    # Select the specified channels and average the ERP over these channels
    selected_channels = erp.copy().pick_channels(channel_list)
    avg_erp = np.mean(selected_channels.data, axis=0)  # Average over channels
    return avg_erp

alpha_suppression_td = np.array(Alpha_suppresion_Auditory_TD)
alpha_suppression_asd = np.array(Alpha_suppresion_Auditory_SIB)

# Determine the cluster-forming threshold based on a critical t-value
n_participants = 38  # Assume equal sample size for simplicity
alpha_level = 0.05  # Desired significance level for the threshold
df = n_participants - 1  # Degrees of freedom for each group
t_threshold = abs(t.ppf(alpha_level / 2, df))  # Two-tailed t-value for alpha level

# Run the cluster-based permutation test with the t-test function
n_permutations = 2000
data = [alpha_suppression_td, alpha_suppression_asd]
T_obs, clusters, cluster_p_values, _ = permutation_cluster_test(
    data, n_permutations=n_permutations, threshold=t_threshold, tail=0, n_jobs=1, stat_fun=ttest_ind_no_p
)

# Identify significant clusters (p < 0.05)
significant_clusters = np.where(cluster_p_values < 0.05)[0]

# Calculate the mean and SEM for plotting
mean_alpha_td = np.mean(alpha_suppression_td, axis=0)
mean_alpha_asd = np.mean(alpha_suppression_asd, axis=0)
sem_td = np.std(alpha_suppression_td, axis=0) / np.sqrt(len(alpha_suppression_td))
sem_asd = np.std(alpha_suppression_asd, axis=0) / np.sqrt(len(alpha_suppression_asd))

# Define time vector (adjust if needed)

# Plot the results
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, mean_alpha_td, label='TD', color='blue')
ax.fill_between(x, mean_alpha_td - sem_td, mean_alpha_td + sem_td, color='blue', alpha=0.2)
ax.plot(x, mean_alpha_asd, label='ASD', color='orange')
ax.fill_between(x, mean_alpha_asd - sem_asd, mean_alpha_asd + sem_asd, color='orange', alpha=0.2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Alpha Suppression')
ax.legend()
ax.set_title('Alpha Suppression with Significant Clusters Highlighted')

# Highlight significant clusters
for cluster_idx in significant_clusters:
    cluster_times = clusters[cluster_idx][0]  # Boolean array for this cluster
    cluster_start = x[cluster_times[0]]  # Start time of cluster
    cluster_end = x[cluster_times[-1]]   # End time of cluster
    ax.axvspan(cluster_start, cluster_end, color='red', alpha=0.3)

plt.tight_layout()
plt.show()

#%% Peak to Peak
import numpy as np

freqs = np.linspace(*np.array([3, 40]), num=200) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
channels = ['T7','T8','FT7','FT8','FC5','C5','FC6','C6']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2','C1','Cz','C2']
# channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.05
tmax = 0.6

# Alpha_min = 0 # 3Hz
# Alpha_max = 21 # 7Hz

Alpha_min = 22 # 7Hz
Alpha_max = 53 # 13Hz

# Alpha_min = 58 # 13Hz
# Alpha_max = 147 # 30Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

times_idx = np.linspace(-0.05,0.6,334)

# To find minimun peak
for i in range(0,len(Power_NPL_V_all_TD),1):
     
    Aph_TD = Power_NPL_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_TD = np.min(Fa_TD)
    peak_latency_TD = times_idx[np.argmin(Fa_TD)]
    Alpha_suppresion_TD.append((peak_amplitude_TD, peak_latency_TD))
    
for i in range(0,len(Power_NPL_V_all_SIB),1):
     
    Aph_SIB = Power_NPL_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_SIB = np.min(Fa_SIB)
    peak_latency_SIB = times_idx[np.argmin(Fa_SIB)]
    Alpha_suppresion_SIB.append((peak_amplitude_SIB, peak_latency_SIB))
    
for i in range(0,len(Power_NPL_V_all_ASD),1):
     
    Aph_ASD = Power_NPL_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_ASD = np.min(Fa_ASD)
    peak_latency_ASD = times_idx[np.argmin(Fa_ASD)]
    Alpha_suppresion_ASD.append((peak_amplitude_ASD, peak_latency_ASD))
    
# # To find maximum peak
# for i in range(0,len(Power_NPL_V_all_TD),1):
     
#     Aph_TD = Power_NPL_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_TD = np.max(Fa_TD)
#     peak_latency_TD = times_idx[np.argmax(Fa_TD)]
#     Alpha_suppresion_TD.append((peak_amplitude_TD, peak_latency_TD))
    
# for i in range(0,len(Power_NPL_V_all_SIB),1):
     
#     Aph_SIB = Power_NPL_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_SIB = np.max(Fa_SIB)
#     peak_latency_SIB = times_idx[np.argmax(Fa_SIB)]
#     Alpha_suppresion_SIB.append((peak_amplitude_SIB, peak_latency_SIB))
    
# for i in range(0,len(Power_NPL_V_all_ASD),1):
     
#     Aph_ASD = Power_NPL_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
#     Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
#     # Find the peak amplitude and its latency within the time window
#     peak_amplitude_ASD = np.max(Fa_ASD)
#     peak_latency_ASD = times_idx[np.argmax(Fa_ASD)]
#     Alpha_suppresion_ASD.append((peak_amplitude_ASD, peak_latency_ASD))

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[0] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[0] for x in Alpha_suppresion_SIB]
peak_amplitudes_2 = [x[0] for x in Alpha_suppresion_ASD]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[1] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[1] for x in Alpha_suppresion_SIB]
peak_amplitudes_2 = [x[1] for x in Alpha_suppresion_ASD]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%% Average amplitude over window of time

import numpy as np

freqs = np.linspace(*np.array([3, 40]), num=200)  # Frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
# channels = ['T7','T8','FT7','FT8','FC5','C5','FC6','C6']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2','C1','Cz','C2']
# channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.05
tmax = 0.6

# Frequency indices for alpha range
Alpha_min = 22  # Corresponds to 7 Hz
Alpha_max = 53  # Corresponds to 13 Hz

# Time indices for the averaging range
times_idx = np.linspace(-0.05, 0.6, 334)  # Adjust to match your data's time resolution
avg_tmin = 0.1
avg_tmax = 0.3

# Find the indices for the averaging time range
avg_mask = (times_idx >= avg_tmin) & (times_idx <= avg_tmax)

# Initialize lists to store results
Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

# TD Group
for i in range(len(Power_NPL_V_all_TD)):
    Aph_TD = Power_NPL_V_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max, :], axis=0)
    # Calculate the average amplitude in the time window
    avg_amplitude_TD = np.mean(Fa_TD[avg_mask])
    Alpha_suppresion_TD.append(avg_amplitude_TD)

# SIB Group
for i in range(len(Power_NPL_V_all_SIB)):
    Aph_SIB = Power_NPL_V_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max, :], axis=0)
    # Calculate the average amplitude in the time window
    avg_amplitude_SIB = np.mean(Fa_SIB[avg_mask])
    Alpha_suppresion_SIB.append(avg_amplitude_SIB)

# ASD Group
for i in range(len(Power_NPL_V_all_ASD)):
    Aph_ASD = Power_NPL_V_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max, :], axis=0)
    # Calculate the average amplitude in the time window
    avg_amplitude_ASD = np.mean(Fa_ASD[avg_mask])
    Alpha_suppresion_ASD.append(avg_amplitude_ASD)
    
#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = Alpha_suppresion_TD
peak_amplitudes_1 = Alpha_suppresion_SIB
peak_amplitudes_2 = Alpha_suppresion_ASD

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%% ITPC
import numpy as np

freqs = np.linspace(*np.array([3, 40]), num=200) #num = step / bin allows a precision of the frequency resolution

# Occipital - Visual stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8','P9','P7','P5','P3','P1','P2','P4','P6','P8','P10']

# Temporal - Auditory stimulation
# channels = ['T7','T8','FT7','FT8','FC5','C5','FC6','C6']

# Frontal for theta activity
# channels = ['FC1','FCz','FC2','F1','Fz','F2','C1','Cz','C2']
# channels = ['FC1','FCz','FC2','F1','Fz','F2']

tmin = -0.1
tmax = 0.6

# Alpha_min = 0 # 3Hz
# Alpha_max = 21 # 7Hz

Alpha_min = 22 # 7Hz
Alpha_max = 53 # 13Hz

# Alpha_min = 58 # 13Hz
# Alpha_max = 147 # 30Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

for i in range(0,len(Power_V_all_TD),1):
     
    Aph_TD = ITPC_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_TD.append(Fa_TD)
    
for i in range(0,len(Power_V_all_SIB),1):
     
    Aph_SIB = ITPC_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_SIB.append(Fa_SIB)
    
for i in range(0,len(Power_V_all_ASD),1):
     
    Aph_ASD = ITPC_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    Alpha_suppresion_ASD.append(Fa_ASD)

fig, ax = plt.subplots()

Mean_TD = np.mean(np.array( Alpha_suppresion_TD),axis=0)
Mean_SIB = np.mean(np.array( Alpha_suppresion_SIB),axis=0)
Mean_ASD = np.mean(np.array( Alpha_suppresion_ASD),axis=0)

SEM_TD = np.std(np.array(Alpha_suppresion_TD), axis=0) / np.sqrt(len(Alpha_suppresion_TD))
SEM_SIB = np.std(np.array(Alpha_suppresion_SIB), axis=0) / np.sqrt(len(Alpha_suppresion_SIB))
SEM_ASD = np.std(np.array(Alpha_suppresion_ASD), axis=0) / np.sqrt(len(Alpha_suppresion_ASD))

x = np.linspace(-0.1,0.6,359)

ax.plot(x, Mean_TD, label = 'TD')
ax.fill_between(x, Mean_TD - SEM_TD, Mean_TD + SEM_TD, alpha=0.2)

ax.plot(x, Mean_SIB, label = 'SIB')
ax.fill_between(x, Mean_SIB - SEM_SIB, Mean_SIB + SEM_SIB, alpha=0.2)

ax.plot(x, Mean_ASD, label = 'ASD')
ax.fill_between(x, Mean_ASD - SEM_ASD, Mean_ASD + SEM_ASD, alpha=0.2)

ax.legend()

#%% Peak to Peak
import numpy as np

freqs = np.linspace(*np.array([2, 40]), num=200) #num = step / bin allows a precision of the frequency resolution

# FCz channels
# channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']

# Temporal - Auditory stimulation
channels = ['O1', 'O2', 'PO7', 'PO3', 'PO4', 'PO8']

tmin = -0.05
tmax = 0.6

# Alpha_min = 0 # 3Hz
# Alpha_max = 21 # 7Hz

Alpha_min = 22 # 7Hz
Alpha_max = 53 # 13Hz

Alpha_suppresion_TD = []
Alpha_suppresion_SIB = []
Alpha_suppresion_ASD = []

times_idx = np.linspace(-0.05,0.6,334)

for i in range(0,len(Power_NPL_V_all_TD),1):
     
    Aph_TD = ITPC_all_TD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_TD = np.mean(np.mean(Aph_TD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_TD = np.max(Fa_TD)
    peak_latency_TD = times_idx[np.argmax(Fa_TD)]
    Alpha_suppresion_TD.append((peak_amplitude_TD, peak_latency_TD))
    
for i in range(0,len(Power_NPL_V_all_SIB),1):
     
    Aph_SIB = ITPC_all_SIB[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_SIB = np.mean(np.mean(Aph_SIB, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_SIB = np.max(Fa_SIB)
    peak_latency_SIB = times_idx[np.argmax(Fa_SIB)]
    Alpha_suppresion_SIB.append((peak_amplitude_SIB, peak_latency_SIB))
    
for i in range(0,len(Power_NPL_V_all_ASD),1):
     
    Aph_ASD = ITPC_all_ASD[i].copy().pick(channels).crop(tmin=tmin, tmax=tmax).data
    Fa_ASD = np.mean(np.mean(Aph_ASD, axis=0)[Alpha_min:Alpha_max,:],axis=0)
    # Find the peak amplitude and its latency within the time window
    peak_amplitude_ASD = np.max(Fa_ASD)
    peak_latency_ASD = times_idx[np.argmax(Fa_ASD)]
    Alpha_suppresion_ASD.append((peak_amplitude_ASD, peak_latency_ASD))

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[0] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[0] for x in Alpha_suppresion_ASD]
peak_amplitudes_2 = [x[0] for x in Alpha_suppresion_SIB]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'ASD','SIB'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_ASD)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_SIB))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD','ASD', 'SIB'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()

#%%
# Extract peak amplitudes for plotting
peak_amplitudes_0 = [x[1] for x in Alpha_suppresion_TD]
peak_amplitudes_1 = [x[1] for x in Alpha_suppresion_SIB]
peak_amplitudes_2 = [x[1] for x in Alpha_suppresion_ASD]

# Create the bar plot
plt.bar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
        tick_label=['TD', 'SIB','ASD'])

# Add error bars
plt.errorbar([1, 2,3], [np.mean(peak_amplitudes_0), np.mean(peak_amplitudes_1), np.mean(peak_amplitudes_2)], 
             yerr=[np.std(peak_amplitudes_0)/np.sqrt(len(Alpha_suppresion_TD)), 
                   np.std(peak_amplitudes_1)/np.sqrt(len(Alpha_suppresion_SIB)),
                   np.std(peak_amplitudes_2)/np.sqrt(len(Alpha_suppresion_ASD))], 
             fmt='o', color='black', capsize=5)

# Set the legend
plt.legend(['TD', 'SIB','ASD'])

# Add labels and title
plt.xlabel('Type of Stimulation')
plt.ylabel('Peak Amplitude')
plt.title('Peak Amplitude with Error Bars')
# plt.ylim([0.22,0.29])

# Show the plot
plt.show()