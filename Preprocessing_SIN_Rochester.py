# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 16:28:04 2026

@author: tvanneau
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 18:07:41 2025

@author: tvanneau
"""

## This preprocessing script save both a trial-level epoch file (each stimulus is one trial), made for event-related analysis 
## But also one epoch file for which each epoch is a full block of data (300 seconds), made for alpha bursts analysis

### Script to load and preprocess EEG for the speech in noise data recorded in Rochester ###

### @Theo Vanneau - CNL Lab

#loading needed toolboxes 
import mne
import numpy as np
import matplotlib.pyplot as plt
import copy
import pandas as pd
import logging
import scipy.io
import os
import pyxdf
from mne import create_info, Annotations, Epochs
from mne.io import RawArray

subject_root = 'Z://Data_new/Speech_in_Noise_Rochester/Data'
Subjects = sorted([s for s in os.listdir(subject_root) if os.path.isdir(os.path.join(subject_root, s))])

Subject = Subjects[0]   # Choose the subject number based on the list extracted above
subject_path = os.path.join(subject_root, Subject)

xdf_files = sorted([f for f in os.listdir(subject_path) if f.lower().endswith('.xdf')])

#%% Load EEG, stimulus-onset, and button-press streams

eeg_streams = []
stim_onset_streams = []
button_press_streams = []

for file in sorted(xdf_files):
    fpath = os.path.join(subject_path, file)
    print(f"Loading {file}")

    streams, header = pyxdf.load_xdf(fpath)

    eeg = None
    stim = None
    response = None

    for s in streams:
        name = s["info"].get("name", [""])[0]
        stype = s["info"].get("type", [""])[0]
        nchan = int(s["info"].get("channel_count", [0])[0])

        print(f"  Stream: name={name!r}, type={stype!r}, channels={nchan}")

        # EEG stream
        if name == "BioSemi" or (
            stype.lower() == "eeg" and nchan >= 16
        ):
            eeg = s

        # Use exact names to distinguish the two marker streams
        elif name == "StimulusOnset":
            stim = s

        elif name == "ButtonPress":
            response = s

    stream_names = [
        s["info"].get("name", [""])[0]
        for s in streams
    ]

    if eeg is None:
        raise RuntimeError(
            f"[{file}] EEG stream not found. "
            f"Available streams: {stream_names}"
        )

    if stim is None:
        raise RuntimeError(
            f"[{file}] StimulusOnset stream not found. "
            f"Available streams: {stream_names}"
        )

    if response is None:
        raise RuntimeError(
            f"[{file}] ButtonPress stream not found. "
            f"Available streams: {stream_names}"
        )

    eeg_streams.append(eeg)
    stim_onset_streams.append(stim)
    button_press_streams.append(response)

#%% Build one Raw per XDF file

raws = []

bio_mont = mne.channels.make_standard_montage("biosemi128")
bio_names = bio_mont.ch_names

def extract_marker_value(value):
    """Extract a marker string from an XDF time-series entry."""
    while isinstance(value, (list, tuple, np.ndarray)):
        if len(value) == 0:
            return ""
        value = value[0]

    if isinstance(value, bytes):
        value = value.decode("utf-8")

    return str(value)

for file, eeg, stim, response in zip(
    sorted(xdf_files),
    eeg_streams,
    stim_onset_streams,
    button_press_streams
):
    # Keep the 64 EEG channels
    data = np.asarray(eeg["time_series"], dtype=float).T[1:129] * 1e-6

    fs = float(eeg["info"]["nominal_srate"][0])

    info = mne.create_info(
        ch_names=bio_names,
        sfreq=fs,
        ch_types="eeg"
    )

    raw_part = mne.io.RawArray(data, info)

    # Use the EEG stream's first XDF timestamp as the local origin
    t0_eeg = float(eeg["time_stamps"][0])

    # -------------------------
    # Stimulus-onset annotations
    # -------------------------
    stim_onsets = (
        np.asarray(stim["time_stamps"], dtype=float) - t0_eeg
    )

    stim_descriptions = [
        extract_marker_value(value)
        for value in stim["time_series"]
    ]

    # -------------------------
    # Button-press annotations
    # -------------------------
    response_onsets = (
        np.asarray(response["time_stamps"], dtype=float) - t0_eeg
    )

    # Give every response the same event label/code
    response_descriptions = ["ButtonPress"] * len(response_onsets)

    # -------------------------
    # Combine both marker streams
    # -------------------------
    all_onsets = np.concatenate([
        stim_onsets,
        response_onsets
    ])

    all_descriptions = np.concatenate([
        np.asarray(stim_descriptions, dtype=str),
        np.asarray(response_descriptions, dtype=str)
    ])

    # Sort markers chronologically
    order = np.argsort(all_onsets, kind="stable")
    all_onsets = all_onsets[order]
    all_descriptions = all_descriptions[order]

    # Retain only markers that fall within this EEG recording
    valid = (
        (all_onsets >= 0) &
        (all_onsets <= raw_part.times[-1])
    )

    if np.sum(~valid):
        print(
            f"{file}: removing {np.sum(~valid)} marker(s) "
            "outside the EEG interval"
        )

    annotations = mne.Annotations(
        onset=all_onsets[valid],
        duration=np.zeros(np.sum(valid), dtype=float),
        description=all_descriptions[valid]
    )
    
    # New marker: 3 seconds after this recording starts.
    if raw_part.times[-1] < 3.0:
        raise ValueError(f"{file}: recording is shorter than 5 seconds.")
    
    annotations.append(
        onset=3.0,
        duration=0.0,
        description="BlockStart"
    )
    
    raw_part.set_annotations(annotations)

    print(
        f"{file}: {len(stim_onsets)} stimuli, "
        f"{len(response_onsets)} button presses, "
        f"{len(annotations)} retained markers"
    )

    raws.append(raw_part)
    
#%% Concatenate recordings
for i, r in enumerate(raws):
    print(
        f"Recording {i}: "
        f"sfreq={r.info['sfreq']}, "
        f"n_times={r.n_times}, "
        f"duration={r.times[-1]:.3f} s"
    )
    
block_durations_s = np.array([
    r.n_times / r.info["sfreq"]
    for r in raws
])

raw = mne.concatenate_raws(raws, on_mismatch="warn")
raw.set_montage(bio_mont, on_missing="warn")

#%% Convert annotations to one final event vector

event_id = {
    "ButtonPress": 1,

    "StimulusOnset_V_interference_Target": 21,
    "StimulusOnset_V_noninterference_Target": 22,
    "StimulusOnset_V_interference_Nontarget": 23,
    "StimulusOnset_V_noninterference_Nontarget": 24,

    "StimulusOnset_A_interference_Target": 31,
    "StimulusOnset_A_noninterference_Target": 32,
    "StimulusOnset_A_interference_Nontarget": 33,
    "StimulusOnset_A_noninterference_Nontarget": 34,

    "StimulusOnset_AV_interference_Target": 41,
    "StimulusOnset_AV_noninterference_Target": 42,
    "StimulusOnset_AV_interference_Nontarget": 43,
    "StimulusOnset_AV_noninterference_Nontarget": 44
}

events, event_id_found = mne.events_from_annotations(
    raw,
    event_id=event_id,
    use_rounding=True
)

button_code = event_id["ButtonPress"]

# Remove a ButtonPress when the immediately preceding event is also a ButtonPress
consecutive_button = (
    (events[1:, 2] == button_code) &
    (events[:-1, 2] == button_code)
)

keep = np.ones(len(events), dtype=bool)
keep[1:] = ~consecutive_button

n_removed = np.sum(~keep)
events = events[keep]

print(f"Removed {n_removed} consecutive button presses.")
print(f"Final number of events: {len(events)}")

#%%  F-score calculation

import numpy as np
import pandas as pd

# Response window in seconds
min_rt = 0.100
max_rt = 1.500

sfreq = raw.info["sfreq"]

button_code = event_id["ButtonPress"]

condition_info = {
    21: ("V",  "interference",    "Target"),
    22: ("V",  "noninterference", "Target"),
    23: ("V",  "interference",    "Nontarget"),
    24: ("V",  "noninterference", "Nontarget"),

    31: ("A",  "interference",    "Target"),
    32: ("A",  "noninterference", "Target"),
    33: ("A",  "interference",    "Nontarget"),
    34: ("A",  "noninterference", "Nontarget"),

    41: ("AV", "interference",    "Target"),
    42: ("AV", "noninterference", "Target"),
    43: ("AV", "interference",    "Nontarget"),
    44: ("AV", "noninterference", "Nontarget"),
}

stimulus_codes = set(condition_info)

# Separate stimulus and response events
stim_events = events[np.isin(events[:, 2], list(stimulus_codes))]
button_events = events[events[:, 2] == button_code]

trial_rows = []

for trial_number, stim_event in enumerate(stim_events, start=1):

    stim_sample = stim_event[0]
    stim_code = stim_event[2]

    sensory, interference, target_type = condition_info[stim_code]

    # Valid response interval in samples
    response_start = stim_sample + int(np.ceil(min_rt * sfreq))
    response_end = stim_sample + int(np.floor(max_rt * sfreq))

    # Do not associate responses occurring after the next stimulus
    if trial_number < len(stim_events):
        next_stim_sample = stim_events[trial_number, 0]
        response_end = min(response_end, next_stim_sample - 1)

    possible_responses = button_events[
        (button_events[:, 0] >= response_start) &
        (button_events[:, 0] <= response_end)
    ]

    responded = len(possible_responses) > 0

    if responded:
        response_sample = possible_responses[0, 0]
        reaction_time = (response_sample - stim_sample) / sfreq
    else:
        response_sample = np.nan
        reaction_time = np.nan

    if target_type == "Target":
        outcome = "Hit" if responded else "Miss"
        correct = responded
    else:
        outcome = "False alarm" if responded else "Correct rejection"
        correct = not responded

    trial_rows.append({
        "Trial": trial_number,
        "Stimulus_sample": stim_sample,
        "Response_sample": response_sample,
        "Event_code": stim_code,
        "Sensory": sensory,
        "Interference": interference,
        "Target_type": target_type,
        "Responded": responded,
        "Outcome": outcome,
        "Correct": correct,
        "RT": reaction_time
    })

trials_df = pd.DataFrame(trial_rows)

print(trials_df.head())

#%% Summarize behavioral perf

def summarize_performance(df):
    n_trials = len(df)

    hits = np.sum(df["Outcome"] == "Hit")
    misses = np.sum(df["Outcome"] == "Miss")
    false_alarms = np.sum(df["Outcome"] == "False alarm")
    correct_rejections = np.sum(df["Outcome"] == "Correct rejection")

    n_targets = hits + misses
    n_nontargets = false_alarms + correct_rejections

    return pd.Series({
        "Trials": n_trials,
        "Targets": n_targets,
        "Nontargets": n_nontargets,
        "Hits": hits,
        "Misses": misses,
        "False_alarms": false_alarms,
        "Correct_rejections": correct_rejections,

        # Target detection
        "Hit_rate": hits / n_targets if n_targets else np.nan,
        "Miss_rate": misses / n_targets if n_targets else np.nan,

        # Nontarget performance
        "False_alarm_rate": (
            false_alarms / n_nontargets if n_nontargets else np.nan
        ),
        "Correct_rejection_rate": (
            correct_rejections / n_nontargets if n_nontargets else np.nan
        ),

        # Overall accuracy includes targets and nontargets
        "Accuracy": df["Correct"].mean(),

        # RT is calculated for correct target responses only
        "Mean_RT": df.loc[df["Outcome"] == "Hit", "RT"].mean(),
        "Median_RT": df.loc[df["Outcome"] == "Hit", "RT"].median()
    })


condition_summary = (
    trials_df
    .groupby(["Sensory", "Interference"], observed=True)
    .apply(summarize_performance)
    .reset_index()
)

print(condition_summary.round(3))

#%% Calculate sensory interference effects

metrics = [
    "Accuracy",
    "Hit_rate",
    "Miss_rate",
    "False_alarm_rate",
    "Mean_RT",
    "Median_RT"
]

sensory_interference_effects = []

for sensory in ["V", "A", "AV"]:

    temp = condition_summary[
        condition_summary["Sensory"] == sensory
    ].set_index("Interference")

    result = {"Sensory": sensory}

    for metric in metrics:
        result[f"{metric}_effect"] = (
            temp.loc["interference", metric]
            - temp.loc["noninterference", metric]
        )

    sensory_interference_effects.append(result)

sensory_interference_effects = pd.DataFrame(
    sensory_interference_effects
)

print(sensory_interference_effects.round(3))

#%% Test pyprep - Noisy Channels to detect bad channels in raw object

from pyprep.find_noisy_channels import NoisyChannels

raw.notch_filter([60, 120, 180])  # or ZapLine

nd = NoisyChannels(raw, ransac = False) 

nd.find_bad_by_nan_flat(flat_threshold=1e-15)
nd.find_bad_by_deviation(deviation_threshold=5.0)
nd.find_bad_by_hfnoise(HF_zscore_threshold=5.0)
nd.find_bad_by_correlation(correlation_secs=1.0, correlation_threshold=0.4, frac_bad=0.05)
nd.find_bad_by_SNR()
nd.find_bad_by_PSD(zscore_threshold=5.0, fmin=1.0, fmax=45.0)

# Get the list of bad channels
bad_channels = nd.get_bads()

# Calculate the percentage of bad channels
total_channels = 128  
bad_channel_count = len(bad_channels)
bad_channel_percentage = (bad_channel_count / total_channels) * 100

print('Bad channels detected:',nd.get_bads())
print('Percent of bad channels detected:',bad_channel_percentage)


#%% interpolate bad channels

# Check if the percentage of bad channels exceeds 15%
if bad_channel_percentage > 15:
    print(f"Subject should be removed: {bad_channel_count} bad channels detected ({bad_channel_percentage:.2f}% of total channels).")
else:
    # If less than 15%, proceed to interpolate bad channels
    raw.info["bads"] = bad_channels
    raw = raw.interpolate_bads()
    # Fill the interpolated channels (which are the same as detected bad channels in this case)
    
    print(f"Interpolation performed: {bad_channel_count} bad channels detected ({bad_channel_percentage:.2f}% of total channels).")

#%% Filtration

lowpass_epochs = 50
highpass_epochs = 0.01

raw.filter(l_freq=highpass_epochs, h_freq=lowpass_epochs)

#%% Epoching EEG data with all trials after PREP

# Select only relevant events: stimuli (3 = AV, 4 = A, 5 = V) and response (1)
# Remove button-press events
button_code = event_id["ButtonPress"]

stim_events = events[events[:, 2] != button_code].copy()

epoch_event_id = {
    "StimulusOnset_V_interference_Target": 21,
    "StimulusOnset_V_noninterference_Target": 22,
    "StimulusOnset_V_interference_Nontarget": 23,
    "StimulusOnset_V_noninterference_Nontarget": 24,

    "StimulusOnset_A_interference_Target": 31,
    "StimulusOnset_A_noninterference_Target": 32,
    "StimulusOnset_A_interference_Nontarget": 33,
    "StimulusOnset_A_noninterference_Nontarget": 34,

    "StimulusOnset_AV_interference_Target": 41,
    "StimulusOnset_AV_noninterference_Target": 42,
    "StimulusOnset_AV_interference_Nontarget": 43,
    "StimulusOnset_AV_noninterference_Nontarget": 44
}

tmin_epochs = -0.6
tmax_epochs = 1.2

epochs_all = mne.Epochs(raw, stim_events, tmin=tmin_epochs, tmax=tmax_epochs, reject=None, 
                        event_id=epoch_event_id, baseline=None, detrend=1, preload=True, decim=2)

#%%#INDEPENDENT COMPONENTS ANALYSIS (ICA) for PREP epochs files

epochs_ica = epochs_all.filter(l_freq=1., h_freq=None)
# epochs_ica.set_eeg_reference('average')
#ICA est sensible aux dérives basse fréquence donc 1Hz + charge données

#Parameters ICA
n_components = None #0.99 # % de vraiance expliquée ou alors le nombre d'électrodes
max_pca_components = 63 # disparaitra dans une future version de MNE, nombre de PCA a faire avant ICA
random_state = 42 #* pour que l'ICA donne la même chose sur les mêmes données
method = 'fastica' # méthode de l'ICA (si 'picard' nécessite pip install python-picard)
fit_params = None # fastica_it=5 paramètre lié à la methode picard
max_iter = 1000 # nombre d'iterations de l'ICA

ica = mne.preprocessing.ICA(n_components=n_components, method = method, max_iter = max_iter, fit_params= fit_params, random_state=random_state)

ica.fit(epochs_ica)
ica.plot_sources(epochs_all)
ica.plot_components()

#%%APPLICATION ICA COMMUN AVERAGE REFERENCE
ica.apply(epochs_all)

#%% Use of autoreject package after ICA to remove bads epochs for no PREP epochs
import autoreject

ar = autoreject.AutoReject(n_interpolate= [1, 2, 4],
                           thresh_method='bayesian_optimization',
                           n_jobs = 1,
                           verbose = True)

ar.fit(epochs_all)
epochs_ar_all, reject_log_all = ar.transform(epochs_all, return_log=True)

#%% Visualisation tools all no PREP

# All
# Visualize the dropped epochs
epochs_all[reject_log_all.bad_epochs].plot(scalings=dict(eeg=100e-6))

# Visualize the rejected log
reject_log_all.plot('horizontal')

#%% Drop RT corresponding to dropped epoch for PREP

# Save the number of rejected epochs
rejected_epochs_count = len(np.where(reject_log_all.bad_epochs)[0])

# Print to verify the number of rejected epochs
print(f"Number of rejected epochs: {rejected_epochs_count}")

# Remove the corresponding reaction time entries
RT_all = trials_df.copy().drop(np.where(reject_log_all.bad_epochs)[0])

# Reset the index to keep it continuous
RT_all = RT_all.reset_index(drop=True)

# Print the updated Reaction Time file length for verification
print(f"Updated number of reaction time trials: {len(RT_all)}")
print(f"Updated number of epochs: {len(epochs_ar_all)}")

#%% Plot ERP NO PREP

epochs_ar_all.set_eeg_reference(ref_channels='average') # For CAR: ref_channels='average' ; for frontal: ref_channels=['D8']
ERP = epochs_ar_all['StimulusOnset_AV_noninterference_Target'].average()
ERP.plot()

#%%
import json
import os

# Total number of good epochs
total_good_epochs = len(epochs_ar_all)

# Update preprocessing_info dictionary with the values
preprocessing_info = {
    'Subject_ID': Subject,  # The subject ID
    'Bad_Channels_Detected': nd.get_bads(),  # List of bad channels detected
    'Interpolated_Channels': bad_channels,  # List of channels that were interpolated
    'ICA_Components_Removed': ica.exclude,  # List of ICA components removed
    'Bad_Epochs_Rejected': len(np.where(reject_log_all.bad_epochs)[0])}

# Print the updated preprocessing information
print(preprocessing_info)

file_path = 'Z://Analysis/Speech_in_noise_Rochester/'

# Ensure the file path exists, if not, create it
if not os.path.exists(file_path):
    os.makedirs(file_path)

# Epochs file: Save epochs as a .fif file
saving_file_all = file_path + '/' + Subject + '_EEG_epo.fif'
epochs_ar_all.save(saving_file_all)

# Reaction time file: Save RT DataFrame as a .csv file
csv_path_RT = file_path + "/" + Subject + "_ar_RT.csv"
RT_all.to_csv(csv_path_RT, sep='\t', encoding='utf-8')

# Function to convert NumPy data types to native Python types
def convert_to_serializable(d):
    for key, value in d.items():
        if isinstance(value, np.integer):
            d[key] = int(value)
        elif isinstance(value, np.floating):
            d[key] = float(value)
        elif isinstance(value, np.ndarray):
            d[key] = value.tolist()  # Convert arrays to lists if any
    return d

# Convert preprocessing_info dictionary to JSON serializable format
preprocessing_info_serializable = convert_to_serializable(preprocessing_info)

# Save the preprocessing information as a JSON file
json_file_path = file_path + '/' + Subject + '_preprocessing_info.json'
with open(json_file_path, 'w') as json_file:
    json.dump(preprocessing_info_serializable, json_file, indent=4)

print(f"Preprocessing info saved to {json_file_path}")

print("Files saved successfully:")
print(f"Epochs file: {saving_file_all}")
print(f"Reaction time file: {csv_path_RT}")
print(f"Preprocessing info file: {json_file_path}")

#%% save excel sheet for all

import pandas as pd
import os

# File path where the Excel will be saved
excel_file_path = 'Z://Analysis/Speech_in_noise_Rochester/preprocessing_info.xlsx'

# Convert preprocessing info into a DataFrame for the current subject
preprocessing_df = pd.DataFrame([preprocessing_info], index=[Subject])

# If the file exists, load it and append the new data
if os.path.exists(excel_file_path):
    existing_df = pd.read_excel(excel_file_path, index_col=0)
    # Append the new subject's data to the existing DataFrame
    updated_df = pd.concat([existing_df, preprocessing_df])
else:
    # If the file doesn't exist, create a new DataFrame
    updated_df = preprocessing_df

# Save (or overwrite) the Excel file with the updated DataFrame
updated_df.to_excel(excel_file_path)

print(f"Preprocessing information for subject {Subject} saved successfully.")
    
