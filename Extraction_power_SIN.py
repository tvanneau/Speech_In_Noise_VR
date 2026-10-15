# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:46:24 2026

@author: tvanneau
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:54:28 2026

@author: tvanneau
"""

import matplotlib as mpl

new_rc_params = {'text.usetex': False,
"svg.fonttype": 'none'
}
mpl.rcParams.update(new_rc_params)

#============================================
#     AVSRT Analysis - Visual Stimulation
#============================================

#loading needed toolboxes 
import mne
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import tkinter
import pandas as pd
from os.path import isfile
from tkinter import filedialog
import os
from pyprep.find_noisy_channels import NoisyChannels
from pyprep.prep_pipeline import PrepPipeline
import re

list_file = os.listdir('Z://Analysis/Speech_in_noise_Rochester')
file_path = 'Z://Analysis/Speech_in_noise_Rochester'

list_files_epochs = [s for s in list_file if '_EEG_epo' in s]
list_files_RT_TD = [s for s in list_file if '_ar_RT' in s]

list_files_epochs.sort()

Power = []
Power_NPL = []
ITPC = []

# event_id = {
#     "ButtonPress": 1,

#     "StimulusOnset_V_interference_Target": 21,
#     "StimulusOnset_V_noninterference_Target": 22,
#     "StimulusOnset_V_interference_Nontarget": 23,
#     "StimulusOnset_V_noninterference_Nontarget": 24,

#     "StimulusOnset_A_interference_Target": 31,
#     "StimulusOnset_A_noninterference_Target": 32,
#     "StimulusOnset_A_interference_Nontarget": 33,
#     "StimulusOnset_A_noninterference_Nontarget": 34,

#     "StimulusOnset_AV_interference_Target": 41,
#     "StimulusOnset_AV_noninterference_Target": 42,
#     "StimulusOnset_AV_interference_Nontarget": 43,
#     "StimulusOnset_AV_noninterference_Nontarget": 44
# }

Stimulus_type = 'StimulusOnset_A_noninterference_Target'

for i in range(len(list_files_epochs)):
    # Load EEG, ET, and RT files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[i])
    
    eeg_epochs.set_eeg_reference('average')
    
    # Time-frequency analysis for each quartile 
    freqs = np.linspace(*np.array([3, 40]), num=100) #num = step / bin allows a precision of the frequency resolution
    n_cycles = np.linspace(*np.array([2, 8]), num=100)  # different number of cycle per frequency
    
    # Total power for each quartile
    power, itc = mne.time_frequency.tfr_morlet(eeg_epochs[Stimulus_type], freqs=freqs, n_cycles=n_cycles, use_fft=True,
                            return_itc=True, decim=4, n_jobs=1, average=True)
    
    ITPC.append(itc)
    Power.append(power)
    
    # Compute the ERP (evoked response)
    erp = eeg_epochs[Stimulus_type].average()
    
    # Subtract ERP from each epoch to compute non-phase locked (NPL) activity
    NPL = eeg_epochs[Stimulus_type].copy()
    for i in range(NPL._data.shape[0]):  # Iterate through each epoch
        NPL._data[i,:128,:] = NPL._data[i,:128,:] - erp._data[:,:]
        
    # Compute time-frequency for non-phase locked power
    power_NPL = mne.time_frequency.tfr_morlet(NPL, freqs=freqs, n_cycles=n_cycles, use_fft=True,
                            return_itc=False, decim=4, n_jobs=1, average=True)
    
    Power_NPL.append(power_NPL)
    
#%% save file

import pickle

with open('Power_StimulusOnset_A_noninterference_Target.pkl','wb') as fp:
    pickle.dump([Power,Power_NPL,ITPC], fp)