# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:52:15 2024

@author: tvanneau
"""

#loading needed toolboxes 
import mne
import numpy as np
import pandas as pd
import os
import re
from mne_connectivity import spectral_connectivity_epochs

list_file = os.listdir('Z://Analysis/SFARI_Analysis/AVSRT/Epochs_filter_RT/TD')
file_path = 'Z://Analysis/SFARI_Analysis/AVSRT/Epochs_filter_RT/TD'

list_files_epochs = [s for s in list_file if '_ar_all_EEG_epo' in s]
list_files_RT_TD = [s for s in list_file if '_ar_RT_all' in s]
list_files_ET_TD = [s for s in list_file if '_ar_all_ET' in s]

# Define the time range to crop after computation
crop_tmin = -0.1  # Start time in seconds
crop_tmax = 0.6   # End time in seconds

freqs = np.linspace(3, 13, num=80)  # Range of frequency for the connectivity analysis - Depend on the method you selected (average across frequencies or not)
n_cycles = np.linspace(2, 10, 80) # Number of cycles, to adapt in function of the length of the epoch

condition_connectivities = []

Stimulus_type = 'V'

for i in range(len(list_files_epochs)):
    # Load EEG, RT, and ET files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[i])
    et_epochs = mne.read_epochs(file_path + "/" + list_files_ET_TD[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_TD[i], sep='\t', encoding='utf-8')
    
    # Standardize channel names by removing '_right' and '_left' suffixes
    new_channel_names = {ch_name: re.sub(r'_(right|left)', '', ch_name) for ch_name in et_epochs.ch_names}
    et_epochs.rename_channels(new_channel_names)
    
    # Select visual ('V') and audiovisual ('AV') trials in EEG and ET epochs
    eeg_epochs = eeg_epochs[Stimulus_type]
    et_epochs_v = et_epochs[Stimulus_type]
    rt = rt_data[rt_data['Stimulus']==Stimulus_type]
    
    rt = rt.reset_index(drop=True)
    
    # Find the index of t=0 in the epochs
    time_index = np.where(eeg_epochs.times == 0)[0][0]  # Index of t=0
    
    # Get the gaze data for all trials and times at once
    gaze_x_data = et_epochs_v.get_data(picks='xpos')  # All gaze X data across trials
    gaze_y_data = et_epochs_v.get_data(picks='ypos')  # All gaze Y data across trials
    
    # Initialize a list to store indices of trials without a blink at t=0
    keep_indices = []
    
    # Loop through each trial and check if there is no blink (no NaN) at t=0
    for j in range(gaze_x_data.shape[0]):
        # Extract gaze x and y data at t=0 for the current trial
        gaze_x = gaze_x_data[j, 0, time_index]  # Gaze X at t=0 for trial j
        gaze_y = gaze_y_data[j, 0, time_index]  # Gaze Y at t=0 for trial j
        
        # Check if there is no blink (no NaN values) at t=0
        if not np.isnan(gaze_x) and not np.isnan(gaze_y):
            keep_indices.append(j)  # Keep this trial if there is no blink at t=0
    
    epochs = eeg_epochs[keep_indices]
    df = rt.iloc[keep_indices].reset_index(drop=True)
    
    indices_to_keep = []

    for stim_type in [Stimulus_type]:
        condition_df = df[df['Stimulus'] == stim_type]
        
        # Calculate the 95th percentile for the condition
        lower_bound = condition_df['RT (ms)'].quantile(0.025)
        upper_bound = condition_df['RT (ms)'].quantile(0.975)
        
        # lower_bound = 0.15
        # upper_bound = 0.5
    
        # Filter and retain indices of the trials within the 95th percentile
        filtered_condition_indices = condition_df[
            (condition_df['RT (ms)'] >= lower_bound) & 
            (condition_df['RT (ms)'] <= upper_bound)
            ].index
        indices_to_keep.extend(filtered_condition_indices)

    indices_to_keep.sort()
    # Filter the DataFrame using the retained indices
    filtered_df = df.loc[indices_to_keep].copy()
    filtered_df.sort_index(inplace=True)  # Sort to maintain original order
    filtered_df.index = range(0,len(filtered_df))
    
    # Ensure that epochs are selected based on the DataFrame's index to maintain order
    # This requires that epochs.events[:, 2] (event_id) aligns with the DataFrame's index
    filtered_epochs = epochs[indices_to_keep]
    
    # Apply Laplacian filter
    filtered_epochs.set_eeg_reference('average', projection=True).apply_proj().apply_baseline(baseline=(-0.05,0.02)).pick_types(eeg=True)
    epochs_Cond = mne.preprocessing.compute_current_source_density(filtered_epochs)
    
    # Compute the ERP (evoked response)
    erp = epochs_Cond.average()
    
    # Subtract ERP from each epoch to compute non-phase locked (NPL) activity
    NPL = epochs_Cond.copy()
    for i in range(NPL._data.shape[0]):  # Iterate through each epoch
        NPL._data[i,:64,:] = NPL._data[i,:64,:] - erp._data[:,:]
        
    # Calculate connectivity over trials, best suited for ERP with multiples trials - For Visual condition 
    con = spectral_connectivity_epochs(
        NPL, 
        cwt_freqs=freqs, 
        fmin=3,
        fmax=13,
        tmin=-0.5,
        tmax=0.8,
        faverage=False, # for average between the frequency or not
        method='wpli', 
        mode='cwt_morlet', 
        cwt_n_cycles=n_cycles, 
        n_jobs=1,
    )
    
    # Extract connectivity data
    con_data = con.get_data(output='dense')  # Get dense data
    
    # Convert times to a NumPy array
    times = np.array(con.times)  # Ensure times is a NumPy array
    
    # Create the mask for the desired time range
    time_mask = (times >= crop_tmin) & (times <= crop_tmax)
    
    # Apply the mask to crop the time dimension
    con_data_cropped = con_data[:, :, :, time_mask]  # Crop to the desired time range
    
    # Append the connectivity matrix for the current subject and condition
    condition_connectivities.append(con_data_cropped)
    
#%% save connectivity list file
import pickle 

# Save with a pickle format directly into the current path
with open('wPLI_Visual_Induced_TD.pkl', 'wb') as fp:
    pickle.dump(condition_connectivities, fp)   
    
#%% Same for auditory trials (without ET filtration)

#loading needed toolboxes 
import mne
import numpy as np
import pandas as pd
import os
import re
from mne_connectivity import spectral_connectivity_epochs

list_file = os.listdir('Z://Analysis/SFARI_Analysis/AVSRT/Epochs_filter_RT/TD')
file_path = 'Z://Analysis/SFARI_Analysis/AVSRT/Epochs_filter_RT/TD'

list_files_epochs = [s for s in list_file if '_ar_all_EEG_epo' in s]
list_files_RT_TD = [s for s in list_file if '_ar_RT_all' in s]
list_files_ET_TD = [s for s in list_file if '_ar_all_ET' in s]

# Define the time range to crop after computation
crop_tmin = -0.1  # Start time in seconds
crop_tmax = 0.6   # End time in seconds

freqs = np.linspace(3, 13, num=80)  # Range of frequency for the connectivity analysis - Depend on the method you selected (average across frequencies or not)
n_cycles = np.linspace(2, 10, 80) # Number of cycles, to adapt in function of the length of the epoch

condition_connectivities = []

Stimulus_type = 'A'

for i in range(len(list_files_epochs)):
    # Load EEG, RT, and ET files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[i])
    et_epochs = mne.read_epochs(file_path + "/" + list_files_ET_TD[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_TD[i], sep='\t', encoding='utf-8')
    
    # Standardize channel names by removing '_right' and '_left' suffixes
    new_channel_names = {ch_name: re.sub(r'_(right|left)', '', ch_name) for ch_name in et_epochs.ch_names}
    et_epochs.rename_channels(new_channel_names)
    
    # Select visual ('V') and audiovisual ('AV') trials in EEG and ET epochs
    eeg_epochs = eeg_epochs[Stimulus_type]
    et_epochs_v = et_epochs[Stimulus_type]
    rt = rt_data[rt_data['Stimulus']==Stimulus_type]
    rt = rt.reset_index(drop=True)

    epochs = eeg_epochs
    df = rt

    indices_to_keep = []

    for stim_type in [Stimulus_type]:
        condition_df = df[df['Stimulus'] == stim_type]
        
        # Calculate the 95th percentile for the condition
        lower_bound = condition_df['RT (ms)'].quantile(0.025)
        upper_bound = condition_df['RT (ms)'].quantile(0.975)
        
        # lower_bound = 0.15
        # upper_bound = 0.5
    
        # Filter and retain indices of the trials within the 95th percentile
        filtered_condition_indices = condition_df[
            (condition_df['RT (ms)'] >= lower_bound) & 
            (condition_df['RT (ms)'] <= upper_bound)
            ].index
        indices_to_keep.extend(filtered_condition_indices)

    indices_to_keep.sort()
    # Filter the DataFrame using the retained indices
    filtered_df = df.loc[indices_to_keep].copy()
    filtered_df.sort_index(inplace=True)  # Sort to maintain original order
    filtered_df.index = range(0,len(filtered_df))
    
    # Ensure that epochs are selected based on the DataFrame's index to maintain order
    # This requires that epochs.events[:, 2] (event_id) aligns with the DataFrame's index
    filtered_epochs = epochs[indices_to_keep]
    
    # Apply Laplacian filter
    filtered_epochs.set_eeg_reference('average', projection=True).apply_proj().apply_baseline(baseline=(-0.05,0.02)).pick_types(eeg=True)
    epochs_Cond = mne.preprocessing.compute_current_source_density(filtered_epochs)
    
    # Compute the ERP (evoked response)
    erp = epochs_Cond.average()
    
    # Subtract ERP from each epoch to compute non-phase locked (NPL) activity
    NPL = epochs_Cond.copy()
    for i in range(NPL._data.shape[0]):  # Iterate through each epoch
        NPL._data[i,:64,:] = NPL._data[i,:64,:] - erp._data[:,:]
        
    # Calculate connectivity over trials, best suited for ERP with multiples trials - For Visual condition 
    con = spectral_connectivity_epochs(
        NPL, 
        cwt_freqs=freqs, 
        fmin=3,
        fmax=13,
        tmin=-0.5,
        tmax=0.8,
        faverage=False, # for average between the frequency or not
        method='wpli', 
        mode='cwt_morlet', 
        cwt_n_cycles=n_cycles, 
        n_jobs=1,
    )
    
    # Extract connectivity data
    con_data = con.get_data(output='dense')  # Get dense data
    
    # Convert times to a NumPy array
    times = np.array(con.times)  # Ensure times is a NumPy array
    
    # Create the mask for the desired time range
    time_mask = (times >= crop_tmin) & (times <= crop_tmax)
    
    # Apply the mask to crop the time dimension
    con_data_cropped = con_data[:, :, :, time_mask]  # Crop to the desired time range
    
    # Append the connectivity matrix for the current subject and condition
    condition_connectivities.append(con_data_cropped)
    
#%% save connectivity list file
import pickle 

# Save with a pickle format directly into the current path
with open('wPLI_Auditory_Induced_TD.pkl', 'wb') as fp:
    pickle.dump(condition_connectivities, fp) 