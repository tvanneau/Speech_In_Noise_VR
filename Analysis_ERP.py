# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:26:40 2024

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
import pandas as pd
import os
import seaborn as sns
from scipy.stats import sem

list_file = os.listdir('Z://Analysis/Speech_in_noise_Rochester')
file_path = 'Z://Analysis/Speech_in_noise_Rochester'

list_files_epochs = [s for s in list_file if '_EEG_epo' in s]
list_files_RT_TD = [s for s in list_file if '_ar_RT' in s]

# Initialize lists to store concatenated EEG epochs and RTs per participant
RT_lst = []
epochs_lst = []

for i in range(len(list_files_epochs)):
    # Load EEG, ET, and RT files
    eeg_epochs = mne.read_epochs(file_path + "/" + list_files_epochs[i])
    rt_data = pd.read_csv(file_path + "/" + list_files_RT_TD[i], sep='\t', encoding='utf-8')
    eeg_epochs.filter(
    l_freq=None,
    h_freq=40.0,
    picks="eeg",
    method="fir",
    phase="zero"
    )
    eeg_epochs.set_eeg_reference(ref_channels='average')
    eeg_epochs.apply_baseline((-0.1, 0.0))
    # We might have to filter the trial based on the response, let's discuss it for later, for now, we take all trials
    epochs_lst.append(eeg_epochs)
    RT_lst.append(rt_data)
    
#%%
# Assuming you have 3 lists: filtered_RT_lst_ASD, filtered_RT_lst_TD, filtered_RT_lst_SIB

# For ASD group
for i, df in enumerate(RT_lst):
    df['Subject'] = list_files_epochs[i][:4]  # Assign real subject number (first 5 characters) directly

#%%
# Concatenate all dataframes into one
df_combined = pd.concat(RT_lst)

# Check the combined dataframe
df_combined.head()

#%%

# Step 1: Calculate the number of trials for each type of stimulus for each subject
trials_per_subject = df_combined.groupby(['Subject', 'Sensory','Target_type','Interference']).size().unstack(fill_value=1)

# Step 3: Calculate the average number of trials per stimulus type for each group
average_trials_per_group = trials_per_subject.groupby('Subject').mean()

# Display the result
print(average_trials_per_group)

RT_COL = "RT"                  # Replace with your reaction-time column
RESPONSE_COL = "Responded"     # Replace with your response column (True/False or 1/0)

# Keep target trials and ensure the response indicator is numeric (0 or 1)
targets = df_combined.loc[
    df_combined["Target_type"].eq("Target")
].copy()

targets["hit"] = targets[RESPONSE_COL].astype(int)

# RT is calculated for hits only
targets["hit_RT"] = targets[RT_COL].where(targets["hit"].eq(1))

summary = (
    targets
    .groupby(["Subject", "Sensory", "Interference"], observed=True)
    .agg(
        mean_RT=("hit_RT", "mean"),
        hit_rate=("hit", "mean"),
        n_targets=("hit", "size"),
        n_hits=("hit", "sum"),
    )
    .reset_index()
)

summary["hit_rate"] *= 100  # Percentage
print(summary)

sensory_order = ["A", "V", "AV"]
interference_order = ["noninterference", "interference"]

def plot_rain(summary, value_col, ylabel, title):
    fig, axes = plt.subplots(1, 3, figsize=(13, 5), sharey=True)

    for ax, sensory in zip(axes, sensory_order):
        data = summary.loc[summary["Sensory"].eq(sensory)]

        sns.violinplot(
            data=data, x="Interference", y=value_col,
            order=interference_order, ax=ax,
            color="#8DB9C9", inner=None, cut=0,
            density_norm="width"
        )

        # Show only the left half of each violin
        for violin in ax.collections:
            if hasattr(violin, "get_paths"):
                for path in violin.get_paths():
                    vertices = path.vertices
                    center = np.mean(vertices[:, 0])
                    vertices[:, 0] = np.minimum(vertices[:, 0], center)

        sns.boxplot(
            data=data, x="Interference", y=value_col,
            order=interference_order, ax=ax,
            width=0.18, showfliers=False,
            boxprops={"facecolor": "white", "alpha": 0.85},
        )

        sns.stripplot(
            data=data, x="Interference", y=value_col,
            order=interference_order, ax=ax,
            color="#24465B", size=5, alpha=0.75,
            jitter=0.12
        )

        ax.set_title(sensory)
        ax.set_xlabel("")
        ax.set_ylabel(ylabel if ax is axes[0] else "")
        ax.tick_params(axis="x", rotation=15)

    fig.suptitle(title)
    fig.tight_layout()
    return fig, axes


plot_rain(summary, "mean_RT", "Mean RT", "Reaction time for target hits")
plot_rain(summary, "hit_rate", "Hit rate (%)", "Target hit rate")
plt.show()
#%% Calculate ERP for each type of preceding stimuli

# Adjust the calculate_erp function to include the new baseline correction
def calculate_erp_with_new_baseline(filtered_epochs_lst, stim_type):
    erp_list = []
    # Loop through each subject's epochs
    for epochs in filtered_epochs_lst:
        # Select epochs based on stimulation type
        epochs_stim = epochs[stim_type]
        # Calculate the ERP (mean across epochs)
        erp = epochs_stim.average()
        erp_list.append(erp)
    
    return erp_list

# Visual stimulation
erp_v_int_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_V_interference_Target')
erp_v_nint_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_V_noninterference_Target')
erp_v_int_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_V_interference_Nontarget')
erp_v_nint_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_V_noninterference_Nontarget')

# Auditory stimulation
erp_a_int_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_A_interference_Target')
erp_a_nint_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_A_noninterference_Target')
erp_a_int_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_A_interference_Nontarget')
erp_a_nint_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_A_noninterference_Nontarget')

# Audiovisual stimulation
erp_av_int_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_AV_interference_Target')
erp_av_nint_tar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_AV_noninterference_Target')
erp_av_int_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_AV_interference_Nontarget')
erp_av_nint_ntar = calculate_erp_with_new_baseline(epochs_lst, 'StimulusOnset_AV_noninterference_Nontarget')

#%% Plot topomaps - AV

evokeds = [
    mne.grand_average(erp_av_int_tar),
    mne.grand_average(erp_av_nint_tar),
    mne.grand_average(erp_av_int_ntar),
    mne.grand_average(erp_av_nint_ntar),
]

row_labels = [
    "Interference · Target",
    "Noninterference · Target",
    "Interference · Nontarget",
    "Noninterference · Nontarget",
]

times = [-0.1, 0.15, 0.3, 0.61, 0.8, 1.0, 1.2]  # seconds

fig, axes = plt.subplots(4, 7, figsize=(13, 10))

for row, (evoked, label) in enumerate(zip(evokeds, row_labels)):
    evoked.plot_topomap(
        times=times,
        axes=axes[row, :].tolist(),
        ch_type="eeg",
        vlim=(-4, 4),       # µV for EEG with MNE's default scaling
        cmap="RdBu_r",
        colorbar=False,
        show=False,
    )
    axes[row, 0].set_ylabel(label, fontsize=11, labelpad=25)

# One shared colorbar; all maps use the same limits.
sm = plt.cm.ScalarMappable(
    norm=plt.Normalize(vmin=-4, vmax=4),
    cmap="RdBu_r",
)
fig.colorbar(sm, ax=axes, label="Amplitude (µV)", shrink=0.45, pad=0.1)

fig.suptitle("AV ERP scalp topographies", fontsize=14)
fig.subplots_adjust(left=0.16, right=0.88, top=0.92, hspace=0.35)
plt.show()

#%% Plot ERP

visual_channels = ["A11", "A14", 'A24', 'A27', 'B8',
                   'A15','A23','A28']

conditions = {
    "Interference · Target": erp_av_int_tar,
    "Noninterference · Target": erp_av_nint_tar,
    "Interference · Nontarget": erp_av_int_ntar,
    "Noninterference · Nontarget": erp_av_nint_ntar,
}

colors = {
    "Interference · Target": "#D55E00",
    "Noninterference · Target": "#E69F00",
    "Interference · Nontarget": "#0072B2",
    "Noninterference · Nontarget": "#56B4E9",
}

fig, ax = plt.subplots(figsize=(10, 5))

for label, participant_evokeds in conditions.items():
    if len(participant_evokeds) < 2:
        raise ValueError(f"{label}: at least two participants are needed for SEM.")

    # Shape: participants × time points; EEG amplitudes converted to µV.
    participant_erps = []
    for evoked in participant_evokeds:
        missing = set(visual_channels) - set(evoked.ch_names)
        if missing:
            raise ValueError(f"{label}: missing channels {sorted(missing)}")

        picks = [evoked.ch_names.index(ch) for ch in visual_channels]
        participant_erps.append(evoked.data[picks].mean(axis=0) * 1e6)

    participant_erps = np.stack(participant_erps)

    mean_erp = participant_erps.mean(axis=0)
    sem_erp = sem(participant_erps, axis=0)
    times_ms = participant_evokeds[0].times * 1000

    ax.plot(times_ms, mean_erp, color=colors[label], lw=2, label=label)
    ax.fill_between(
        times_ms,
        mean_erp - sem_erp,
        mean_erp + sem_erp,
        color=colors[label],
        alpha=0.20,
        linewidth=0,
    )

ax.axvline(0, color="black", linestyle="--", lw=1)
ax.axhline(0, color="gray", lw=0.8)
ax.set(
    xlabel="Time (ms)",
    ylabel="Amplitude (µV)",
    title="AV ERP — visual channel cluster (mean ± SEM)",
)
ax.legend(frameon=False)
sns.despine()
plt.tight_layout()
plt.show()
plt.xlim([-100,1200])

#%% Plot topomaps - A


evokeds = [
    mne.grand_average(erp_a_int_tar),
    mne.grand_average(erp_a_nint_tar),
    mne.grand_average(erp_a_int_ntar),
    mne.grand_average(erp_a_nint_ntar),
]

row_labels = [
    "Interference · Target",
    "Noninterference · Target",
    "Interference · Nontarget",
    "Noninterference · Nontarget",
]

times = [-0.1, 0.15, 0.3, 0.61, 0.8, 1.0, 1.2]  # seconds

fig, axes = plt.subplots(4, 7, figsize=(13, 10))

for row, (evoked, label) in enumerate(zip(evokeds, row_labels)):
    evoked.plot_topomap(
        times=times,
        axes=axes[row, :].tolist(),
        ch_type="eeg",
        vlim=(-4, 4),       # µV for EEG with MNE's default scaling
        cmap="RdBu_r",
        colorbar=False,
        show=False,
    )
    axes[row, 0].set_ylabel(label, fontsize=11, labelpad=25)

# One shared colorbar; all maps use the same limits.
sm = plt.cm.ScalarMappable(
    norm=plt.Normalize(vmin=-4, vmax=4),
    cmap="RdBu_r",
)
fig.colorbar(sm, ax=axes, label="Amplitude (µV)", shrink=0.45, pad=0.1)

fig.suptitle("A ERP scalp topographies", fontsize=14)
fig.subplots_adjust(left=0.16, right=0.88, top=0.92, hspace=0.35)
plt.show()

#%% Plot ERP

visual_channels = ['A1', 'D1', 'C1', 'D15', 'B1', 'D2', 'C23', 'C2']

conditions = {
    "Interference · Target": erp_a_int_tar,
    "Noninterference · Target": erp_a_nint_tar,
    "Interference · Nontarget": erp_a_int_ntar,
    "Noninterference · Nontarget": erp_a_nint_ntar,
}

colors = {
    "Interference · Target": "#D55E00",
    "Noninterference · Target": "#E69F00",
    "Interference · Nontarget": "#0072B2",
    "Noninterference · Nontarget": "#56B4E9",
}

fig, ax = plt.subplots(figsize=(10, 5))

for label, participant_evokeds in conditions.items():
    if len(participant_evokeds) < 2:
        raise ValueError(f"{label}: at least two participants are needed for SEM.")

    # Shape: participants × time points; EEG amplitudes converted to µV.
    participant_erps = []
    for evoked in participant_evokeds:
        missing = set(visual_channels) - set(evoked.ch_names)
        if missing:
            raise ValueError(f"{label}: missing channels {sorted(missing)}")

        picks = [evoked.ch_names.index(ch) for ch in visual_channels]
        participant_erps.append(evoked.data[picks].mean(axis=0) * 1e6)

    participant_erps = np.stack(participant_erps)

    mean_erp = participant_erps.mean(axis=0)
    sem_erp = sem(participant_erps, axis=0)
    times_ms = participant_evokeds[0].times * 1000

    ax.plot(times_ms, mean_erp, color=colors[label], lw=2, label=label)
    ax.fill_between(
        times_ms,
        mean_erp - sem_erp,
        mean_erp + sem_erp,
        color=colors[label],
        alpha=0.20,
        linewidth=0,
    )

ax.axvline(0, color="black", linestyle="--", lw=1)
ax.axhline(0, color="gray", lw=0.8)
ax.set(
    xlabel="Time (ms)",
    ylabel="Amplitude (µV)",
    title="A ERP — central channel cluster (mean ± SEM)",
)
ax.legend(frameon=False)
sns.despine()
plt.tight_layout()
plt.show()
plt.xlim([-100,1200])

#%% Plot topomaps - V

evokeds = [
    mne.grand_average(erp_v_int_tar),
    mne.grand_average(erp_v_nint_tar),
    mne.grand_average(erp_v_int_ntar),
    mne.grand_average(erp_v_nint_ntar),
]

row_labels = [
    "Interference · Target",
    "Noninterference · Target",
    "Interference · Nontarget",
    "Noninterference · Nontarget",
]

times = [-0.1, 0.15, 0.3, 0.61, 0.8, 1.0, 1.2]  # seconds

fig, axes = plt.subplots(4, 7, figsize=(13, 10))

for row, (evoked, label) in enumerate(zip(evokeds, row_labels)):
    evoked.plot_topomap(
        times=times,
        axes=axes[row, :].tolist(),
        ch_type="eeg",
        vlim=(-4, 4),       # µV for EEG with MNE's default scaling
        cmap="RdBu_r",
        colorbar=False,
        show=False,
    )
    axes[row, 0].set_ylabel(label, fontsize=11, labelpad=25)

# One shared colorbar; all maps use the same limits.
sm = plt.cm.ScalarMappable(
    norm=plt.Normalize(vmin=-4, vmax=4),
    cmap="RdBu_r",
)
fig.colorbar(sm, ax=axes, label="Amplitude (µV)", shrink=0.45, pad=0.1)

fig.suptitle("A ERP scalp topographies", fontsize=14)
fig.subplots_adjust(left=0.16, right=0.88, top=0.92, hspace=0.35)
plt.show()

#%% Plot ERP

visual_channels = ["A11", "A14", 'A24', 'A27', 'B8',
                   'A15','A23','A28']

conditions = {
    "Interference · Target": erp_v_int_tar,
    "Noninterference · Target": erp_v_nint_tar,
    "Interference · Nontarget": erp_v_int_ntar,
    "Noninterference · Nontarget": erp_v_nint_ntar,
}

colors = {
    "Interference · Target": "#D55E00",
    "Noninterference · Target": "#E69F00",
    "Interference · Nontarget": "#0072B2",
    "Noninterference · Nontarget": "#56B4E9",
}

fig, ax = plt.subplots(figsize=(10, 5))

for label, participant_evokeds in conditions.items():
    if len(participant_evokeds) < 2:
        raise ValueError(f"{label}: at least two participants are needed for SEM.")

    # Shape: participants × time points; EEG amplitudes converted to µV.
    participant_erps = []
    for evoked in participant_evokeds:
        missing = set(visual_channels) - set(evoked.ch_names)
        if missing:
            raise ValueError(f"{label}: missing channels {sorted(missing)}")

        picks = [evoked.ch_names.index(ch) for ch in visual_channels]
        participant_erps.append(evoked.data[picks].mean(axis=0) * 1e6)

    participant_erps = np.stack(participant_erps)

    mean_erp = participant_erps.mean(axis=0)
    sem_erp = sem(participant_erps, axis=0)
    times_ms = participant_evokeds[0].times * 1000

    ax.plot(times_ms, mean_erp, color=colors[label], lw=2, label=label)
    ax.fill_between(
        times_ms,
        mean_erp - sem_erp,
        mean_erp + sem_erp,
        color=colors[label],
        alpha=0.20,
        linewidth=0,
    )

ax.axvline(0, color="black", linestyle="--", lw=1)
ax.axhline(0, color="gray", lw=0.8)
ax.set(
    xlabel="Time (ms)",
    ylabel="Amplitude (µV)",
    title="A ERP — central channel cluster (mean ± SEM)",
)
ax.legend(frameon=False)
sns.despine()
plt.tight_layout()
plt.show()
plt.xlim([-100,1200])