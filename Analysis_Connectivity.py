# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 13:37:28 2025

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

eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[0])
#%% load picke file into the current path
import pickle 

with open('wPLI_Audiovisual_TD.pkl', 'rb') as f:
    condition_connectivities_TD  = pickle.load(f) 
    
with open('wPLI_Audiovisual_ASD.pkl', 'rb') as f:
    condition_connectivities_ASD  = pickle.load(f) 
    
with open('wPLI_Audiovisual_SIB.pkl', 'rb') as f:
    condition_connectivities_SIB  = pickle.load(f) 
    
# with open('wPLI_visual_TD.pkl', 'rb') as f:
#     condition_connectivities_TD  = pickle.load(f) 
    
# with open('wPLI_visual_ASD.pkl', 'rb') as f:
#     condition_connectivities_ASD  = pickle.load(f) 
    
# with open('wPLI_visual_SIB.pkl', 'rb') as f:
#     condition_connectivities_SIB  = pickle.load(f) 
    
# with open('wPLI_Auditory_TD.pkl', 'rb') as f:
#     condition_connectivities_TD  = pickle.load(f) 
    
# with open('wPLI_Auditory_ASD.pkl', 'rb') as f:
#     condition_connectivities_ASD  = pickle.load(f) 
    
# with open('wPLI_Auditory_SIB.pkl', 'rb') as f:
#     condition_connectivities_SIB  = pickle.load(f) 

#%% Analysis for method 2: Plot a time-frequency map of the wPLI values (one per frequency and per time-points)
import matplotlib.pyplot as plt

freqs = np.linspace(3, 13, num=80)  # Range of frequency for the connectivity analysis - Depend on the method you selected (average across frequencies or not)

# Example region 1 - Fronto-central cluster
# Region_1 = ['T8','TP8']
# Region_1 = ['O1','PO3','PO7']
# Region_1 = ['O1','PO3','PO7','O2','PO4','PO8','Oz','POz','Iz']
Region_1 = ['O1','PO3','PO7','O2','PO4','PO8']

# Region_1 = ['T8','TP8','TP7','T7']

# Example region 2 - Auditory temporal cortices wide version
# Region_2 = ['O2','PO4','PO8']
# Region_2 = ['TP7','T7','T8','TP8']
# Region_2 = ['TP7','T7']
# Region_2 = ['FC1','FCz','FC2','F1','Fz','F2']

# Region_2 = ['F3','F1','Fz','F2','F4','AF3', 'AFz', 'AF4']
# Region_2 = ['F1','Fz','F2']

Region_2 = ['AF3', 'AF4', 'F3', 'F4']


# Region_2 = ['AF7','AF3','FP1','F7']

# Extract channel names
ch_names = eeg_epochs.ch_names  # Need to load an epoch file with the corresponding channels 

# Extract time points from the epochs (using any loaded epochs object)
times = np.linspace(-0.1,0.6,359) # Depend on the length of the epoch

# Find indices for the regions of interest
indices_region_1 = [ch_names.index(ch) for ch in Region_1 if ch in ch_names]
indices_region_2 = [ch_names.index(ch) for ch in Region_2 if ch in ch_names]

def calculate_avg_connectivity_tf(condition_connectivities, indices_region_1, indices_region_2):
    avg_connectivity_values = []
    for con_data in condition_connectivities:
        connectivity_values = []
        for i in indices_region_1:
            for j in indices_region_2:
                if i > j:
                    connectivity_values.append(con_data[i, j, :, :])
                elif i < j:
                    connectivity_values.append(con_data[j, i, :, :])
        avg_connectivity_values.append(np.mean(connectivity_values, axis=0))
    return avg_connectivity_values

#%% For TD

# Average the time-frequency connectivity matrices across subjects for each condition
avg_connectivity_tf_TD = calculate_avg_connectivity_tf(condition_connectivities_TD, indices_region_1, indices_region_2)
# Average across all subjects
avg_connectivity_tf_TD_all = np.mean(avg_connectivity_tf_TD, axis=0)
# Plot time-frequency maps
plt.figure(figsize=(10, 5))
plt.imshow(avg_connectivity_tf_TD_all, aspect='auto', origin='lower', extent=[times[0], times[-1], freqs[0], freqs[-1]], cmap='viridis',
           vmin=0.14,vmax=0.20)
plt.colorbar(label='wPLI')
plt.title('Time-Frequency Connectivity (Condition A)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

#%% For ASD

# Average the time-frequency connectivity matrices across subjects for each condition
avg_connectivity_tf_ASD = calculate_avg_connectivity_tf(condition_connectivities_ASD, indices_region_1, indices_region_2)
# Average across all subjects
avg_connectivity_tf_ASD_all = np.mean(avg_connectivity_tf_ASD, axis=0)
# Plot time-frequency maps
plt.figure(figsize=(10, 5))
plt.imshow(avg_connectivity_tf_ASD_all, aspect='auto', origin='lower', extent=[times[0], times[-1], freqs[0], freqs[-1]], cmap='viridis',
           vmin=0.14,vmax=0.20)
plt.colorbar(label='wPLI')
plt.title('Time-Frequency Connectivity (Condition A)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

#%% For SIB

# Average the time-frequency connectivity matrices across subjects for each condition
avg_connectivity_tf_SIB = calculate_avg_connectivity_tf(condition_connectivities_SIB, indices_region_1, indices_region_2)
# Average across all subjects
avg_connectivity_tf_SIB_all = np.mean(avg_connectivity_tf_SIB, axis=0)
# Plot time-frequency maps
plt.figure(figsize=(10, 5))
plt.imshow(avg_connectivity_tf_SIB_all, aspect='auto', origin='lower', extent=[times[0], times[-1], freqs[0], freqs[-1]], cmap='viridis',
           vmin=0.14,vmax=0.20)
plt.colorbar(label='wPLI')
plt.title('Time-Frequency Connectivity (Condition A)')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()


#%% Plot the average curve for a specific frequency band for ASD and TD group 

import numpy as np
import matplotlib.pyplot as plt

# Define frequency band of interest
freq_band = (4, 7)
freq_indices = np.where((freqs >= freq_band[0]) & (freqs <= freq_band[1]))[0]

# Convert lists to arrays for easier handling
avg_tf_TD = np.array(avg_connectivity_tf_TD)  # Shape: (n_subjects, n_freqs, n_times)
avg_tf_ASD = np.array(avg_connectivity_tf_ASD)
avg_tf_SIB = np.array(avg_connectivity_tf_SIB)

# Average across frequency band for each subject
avg_band_TD = np.mean(avg_tf_TD[:, freq_indices, :], axis=1)  # Shape: (n_subjects, n_times)
avg_band_ASD = np.mean(avg_tf_ASD[:, freq_indices, :], axis=1)
avg_band_SIB = np.mean(avg_tf_SIB[:, freq_indices, :], axis=1)

# --- Plot raw values ---
plt.figure(figsize=(10, 5))
for data, color, label in zip([avg_band_TD, avg_band_ASD, avg_band_SIB], ['blue', 'orange', 'purple'], ['TD', 'ASD', 'SIB']):
    mean_vals = np.mean(data, axis=0)
    sem_vals = np.std(data, axis=0) / np.sqrt(data.shape[0])
    plt.plot(times, mean_vals, label=label, color=color)
    plt.fill_between(times, mean_vals - sem_vals, mean_vals + sem_vals, color=color, alpha=0.3)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.title('Raw Connectivity in 3–7 Hz Band')
plt.xlabel('Time (s)')
plt.ylabel('wPLI')
plt.legend()
plt.tight_layout()
plt.show()

# --- Baseline normalization ---
baseline_period = (-0.05, 0.0)
baseline_indices = np.where((times >= baseline_period[0]) & (times <= baseline_period[1]))[0]

def normalize_band_data(band_data):
    normalized = []
    for subj_data in band_data:
        baseline = np.mean(subj_data[baseline_indices])
        norm = (subj_data - baseline) / baseline * 100  # % change
        normalized.append(norm)
    return np.array(normalized)

norm_band_TD = normalize_band_data(avg_band_TD)
norm_band_ASD = normalize_band_data(avg_band_ASD)
norm_band_SIB = normalize_band_data(avg_band_SIB)

# --- Plot normalized values ---
plt.figure(figsize=(10, 5))
for data, color, label in zip([norm_band_TD, norm_band_ASD, norm_band_SIB], ['blue', 'orange', 'purple'], ['TD', 'ASD', 'SIB']):
    mean_vals = np.mean(data, axis=0)
    sem_vals = np.std(data, axis=0) / np.sqrt(data.shape[0])
    plt.plot(times, mean_vals, label=label, color=color)
    plt.fill_between(times, mean_vals - sem_vals, mean_vals + sem_vals, color=color, alpha=0.3)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.title('Baseline-Normalized Connectivity (3–7 Hz Band)')
plt.xlabel('Time (s)')
plt.ylabel('Change from Baseline (%)')
plt.legend()
plt.tight_layout()
plt.show()
plt.ylim([-10,150])

#%% permutation between TD and ASD norm_band 

from mne.stats import permutation_cluster_test
import matplotlib.pyplot as plt

# Inputs: shape (n_subjects, n_times)
X = [norm_band_TD, norm_band_ASD]

# Run cluster-based permutation test
T_obs, clusters, cluster_p_values, H0 = permutation_cluster_test(
    X, n_permutations=1000, tail=0, threshold=None, out_type='mask', seed=42
)

# Plot result with clusters
plt.figure(figsize=(10, 5))
plt.plot(times, np.mean(norm_band_TD, axis=0), label='TD', color='blue')
plt.plot(times, np.mean(norm_band_ASD, axis=0), label='ASD', color='red')

# Highlight significant clusters
for i_c, c in enumerate(clusters):
    if cluster_p_values[i_c] < 0.05:
        h = np.max([np.max(np.mean(norm_band_TD, axis=0)),
                    np.max(np.mean(norm_band_ASD, axis=0))]) + 5
        plt.axvspan(times[c][0], times[c][-1], color='gray', alpha=0.3, label='p < 0.05' if i_c == 0 else None)

plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.title('Cluster-Based Permutation Test (3–7 Hz, % Change)')
plt.xlabel('Time (s)')
plt.ylabel('Normalized Connectivity (% from baseline)')
plt.legend()
plt.tight_layout()
plt.show()

#%%

def extract_peak_info(normalized_data, times):
    normalized_data = normalized_data[:,153:190]
    peak_vals = np.max(normalized_data, axis=1)  # peak amplitude per subject
    peak_latencies = times[np.argmax(normalized_data, axis=1)]  # latency of peak
    return peak_vals, peak_latencies

# Extract peak values and latencies
peak_vals_TD, peak_lat_TD = extract_peak_info(norm_band_TD, times)
peak_vals_ASD, peak_lat_ASD = extract_peak_info(norm_band_ASD, times)
peak_vals_SIB, peak_lat_SIB = extract_peak_info(norm_band_SIB, times)

import pandas as pd

df_peaks = pd.DataFrame({
    'Group': ['TD'] * len(peak_vals_TD) + ['ASD'] * len(peak_vals_ASD) + ['SIB'] * len(peak_vals_SIB),
    'Peak_Amplitude': np.concatenate([peak_vals_TD, peak_vals_ASD, peak_vals_SIB]),
    'Peak_Latency': np.concatenate([peak_lat_TD, peak_lat_ASD, peak_lat_SIB])
})


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.boxplot(data=df_peaks, x='Group', y='Peak_Amplitude', palette='Set2')
sns.stripplot(data=df_peaks, x='Group', y='Peak_Amplitude', color='black', alpha=0.5, jitter=0.2)
plt.ylabel('Peak wPLI Change from Baseline (%)')
plt.title('Peak Baseline-Normalized wPLI (3–7 Hz Band)')
plt.tight_layout()
plt.show()

import statsmodels.api as sm
from statsmodels.formula.api import ols

# Run ANOVA
model = ols('Peak_Amplitude ~ Group', data=df_peaks).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#%%

def extract_mean_in_window(normalized_data, times, tmin=0.15, tmax=0.3):
    idx = np.where((times >= tmin) & (times <= tmax))[0]
    mean_vals = np.mean(normalized_data[:, idx], axis=1)
    return mean_vals

mean_vals_TD = extract_mean_in_window(norm_band_TD, times)
mean_vals_ASD = extract_mean_in_window(norm_band_ASD, times)
mean_vals_SIB = extract_mean_in_window(norm_band_SIB, times)

df_means = pd.DataFrame({
    'Group': ['TD'] * len(mean_vals_TD) + ['ASD'] * len(mean_vals_ASD) + ['SIB'] * len(mean_vals_SIB),
    'Mean_Amplitude': np.concatenate([mean_vals_TD, mean_vals_ASD, mean_vals_SIB])
})

plt.figure(figsize=(8, 6))
sns.boxplot(data=df_means, x='Group', y='Mean_Amplitude', palette='Set2')
sns.stripplot(data=df_means, x='Group', y='Mean_Amplitude', color='black', alpha=0.5, jitter=0.2)
plt.ylabel('wPLI Change from Baseline (%)')
plt.title('Mean wPLI (100–300 ms, 3–7 Hz)')
plt.tight_layout()
plt.show()

model = ols('Mean_Amplitude ~ Group', data=df_means).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#%%
# Save results to a CSV file
df_means.to_csv("wPLI_Average_150_300ms_Audiovisual_Frontal_Parocc.csv", index=False)
