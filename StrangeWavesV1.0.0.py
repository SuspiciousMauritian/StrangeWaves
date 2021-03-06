from asyncio import events
from itertools import count
import os
from pickle import APPEND
from tracemalloc import start
import numpy as np
import mne
import matplotlib.pyplot as plt
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)

print('POST ---------------------------------------------')
#load_data
sample = 'test_ music_503c88ae-321c-49e5-a45f-3a212a409116.edf'
raw = mne.io.read_raw_edf(sample, infer_types= True, preload=True, exclude =('ROC','LOC','L Del','R Del','27','28','29','30','31','32','DC', 'OSAT', 'PR', 'ECG') )
mne.io.Raw.set_montage(raw, 'standard_1020', match_alias = True)
length_sec = raw.__len__()
print('length sec', length_sec)
start_time = 459
end_time = 3789
experimental_duration = end_time - start_time

print('DATA LOADED ------------------------=--------------')
print(raw)
print(raw.info)

print('raw -----------------------------------------------')
# raw_second grid intervals 
one_sec_array_prenp = ([[0,0,0]])
count = start_time
relative_stamp = 0
while relative_stamp < experimental_duration:
    second_mark = count * 500
    list_adition = [second_mark, 0, relative_stamp]
    one_sec_array_prenp.append(list_adition)
    relative_stamp = relative_stamp + 1 
    count = count + 1    
one_sec_grid_line_array = np.array(one_sec_array_prenp)

# raw_highlight_Annotations
event_durations = [10,
    57.14,
    10.05,
    56.89,
    9.85,
    20.08,
    10.1,
    14.9,
    9.97,
    15.17,
    9.98,
    15.83,
    10.09,
    60.14,
    10,
    60.9,
    9.97,
    13.88,
    9.15,
    61.07,
    9.86,
    57.04,
    9.91,
    15.22,
    8.99,
    3.84,
    10.02,
    60.93,
    10.09,
    56.08,
    10.79,
    21.07,
    9.04,
    3.05,
    9.91,
    60.95,
    10,
    57,
    9.8,
    17.09,
    9.13,
    3.05,
    10.13,
    60.05,
    9.97,
    56.97,
    9.04,
    20.95,
    10.19,
    14.84,
    9.1,
    14.98,
    9.86,
    61,
    10.21,
    600.94,
    9.86,
    601.17,
    9.8,
    593.96,
    9.95,
    600.99,
    55.21,
    10.72,
    52.09 ]
pre_event_start = [0,
10,
67.14,
77.19,
134.18,
144.03,
164.11,
174.21,
189.11,
199.08,
214.25,
224.23,
240.06,
250.15,
310.29,
320.29,
381.19,
391.16,
405.04,
414.19,
475.26,
485.12,
542.16,
552.07,
567.29,
576.28,
580.12,
590.14,
651.07,
661.16,
717.24,
728.03,
749.1,
758.14,
761.19,
771.1,
832.2,
842.2,
899.2,
909,
926.09,
935.22,
939.1,
949.23,
1009.28,
1019.25,
1076.22,
1086.13,
1107.08,
1117.27,
1132.11,
1141.21,
1156.19,
1166.05,
1227.05,
1237.26,
1838.2,
1848.06,
2449.23,
2466.18,
3060.14,
3070.09,
3671.08,
3726.29,
3737.01
]
event_names = ['Tuning fork',
'Scilence',
'Tuning fork', 
'White noise',
'Tuning fork',
'Black Bird', 
'Tuning fork', 
'5 note Clarinet',
'Tuning fork', 
'Iphone Ring tone',
'Tuning fork', 
'Skype Ring tone',
'Tuning fork', 
'Blinding lights F minor',
'Tuning fork', 
'Dua lipa 0.75x speed',
'Tuning fork', 
'Ambulance too',
'Tuning fork', 
'1 min Low key gliding', 
'Tuning fork', 
'White noise', 
'Tuning fork', 
'Iphone Alarm',
'Tuning fork', 
'Scream man', 
'Tuning fork', 
'Blinding lights G minor',
'Tuning fork', 
'Scilence',
'Tuning fork',
'European GoldFinch',
'Tuning fork', 
'Scream Woman 1',
'Tuning fork', 
'Dua lipa 1x speed',
'Tuning fork', 
'White noise', 
'Tuning fork',
'5 note flute',
'Tuning fork', 
'Scream Woman 2',
'Tuning fork', 
'Blinding lights D# minor', 
'Tuning fork', 
'Scilence',
'Tuning fork', 
'European Robin',
'Tuning fork', 
'Trumpet', 
'Tuning fork', 
'Ambulance leave',
'Tuning fork', 
'Dua lipa 1.25x speed',
'Tuning fork', 
'Hal walker 10 mins',
'Tuning fork', 
'Yanni Live',
'Tuning fork', 
'Counterpoint 1 fast',
'Tuning fork', 
'K448',
'scilence', 
'Tuning fork', 
'White noise'
]

# start_adjust
event_start= []
for i in pre_event_start:
    adjusted_start_time = i + start_time
    event_start.append(adjusted_start_time)
    
# Plot_annotations
all_annotations = mne.Annotations(onset = event_start, duration = event_durations, description = event_names)
print (all_annotations)
raw = raw.set_annotations(all_annotations)
raw.crop(tmin = start_time, tmax = end_time)

# raw plot
# raw.plot_psd(fmax=50)
# raw.plot(duration=10, n_channels= 21, verbose = True, block = True, events = one_sec_grid_line_array, event_color = 'red', title = sample, theme = "dark", show_options = True)

print('preprocessing ------------------------------------')

# Low-frequency drift filtering
filt_raw = raw.copy().filter(l_freq=1., h_freq=None)

#Power spectral analysis
# filt_raw.plot_psd(fmax=70) #plot PSD

# Independent component analysis 
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=1000)
ica.fit(filt_raw) 
# ica.plot_sources(filt_raw, show_scrollbars=True, block = True) # plot ICA time course
# ica.plot_components() # plot all ICA scalp topogrophy
# ica.plot_properties(filt_raw) # Print first 5 ICA properties
# ica.plot_overlay(raw, exclude = [0, 1], title = 'sample excluding ICA - 0, 1')


# Applying ICA

ica.exclude = [0, 1]
clean_00 = raw.copy()
ica.apply(clean_00)

# clean_00.plot(title = 'clean_00', show_scrollbars=True, duration=10, n_channels= 21, verbose = True, block = True, events = one_sec_grid_line_array, event_color = 'red', theme = "dark", show_options = True)
# clean_00.plot_psd(fmax=70)


#Epoching

def ev(event_time, event_id):
    event_start_sample = round((start_time + event_time) * 500)
    
    array = [event_start_sample, 0, event_id ]
    return array
events_array = np.array([ev(10, 2), 
                         ev(661, 2), 
                         ev(1020, 2),
                         ev(0, 1),
                         ev(134.18, 1),
                         ev(189.11, 1), 
                         ev(214.25, 1), 
                         ev(240.06, 1),
                         ev(310.29, 1),
                         ev(381.19, 1),
                         ev(405.04, 1),
                         ev(475.26, 1),
                         ev(542.16, 1),
                         ev(567.29, 1),
                         ev(580.12, 1),
                         ev(651.07, 1),
                         ev(717.24, 1), 
                         ev(749.1, 1), 
                         ev(761.19, 1),
                         ev(832.21, 1),
                         ev(899.2, 1),
                         ev(1009.28, 1),
                         ev(1107.08, 1),
                         ev(1132.11, 1),
                         ev(1156.19, 1),
                         ev(175.22, 4),
                         ev(177.12, 4),
                         ev(178.21, 4),
                         ev(180.07, 4),
                         ev(181.21, 4),
                         ev(183.05, 4),
                         ev(184.17, 4),
                         ev(186.02, 4),
                         ev(187.14, 4),
                         
                         ])

event_dict = {'tuning_fork': 1, 
              'Scilence': 2, 
              'white_noise': 3, 
              'clarinet_notes': 4, 
              'flute_notes': 5, 
              'trumpet_notes': 6,
            }

location_index = [['Fp1', 'Fp2'] , ['T4', 'T3']]

epochs = mne.Epochs(clean_00, events_array, tmin=-0.2, tmax=0.06,)
epochs.event_id = event_dict
# epochs.plot(block = True)

# Plot mean across epochs 

# for i in raw.info['ch_names']:
epochs['clarinet_notes'].plot_image(combine='std', 
                                    picks = location_index[1],
                                    sigma = 2,
                                    vmin = -20,
                                    vmax = 20,
                                    evoked = True
                                    )


evoked = epochs['clarinet_notes'].average(['T4', 'T3'])

evoked.plot()

# evoked.plot_joint()






# CODE BASE

# raw plot
# raw.plot_psd(fmax=50)
# filt_raw.plot(duration=10, n_channels= 21, verbose = True, block = True, events = one_sec_grid_line_array, event_color = 'red', title = sample, theme = "dark", show_options = True)

# #data_selection
# sampling_freq = raw.info['sfreq']
# start_stop_seconds = np.array([11, 12])
# start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
# channel_index = 24
# raw_selection = raw[channel_index, start_sample:stop_sample]
# print(raw_selection)

# event_array = np.array([[500, 0, 1], [1000, 0, 2], [1500,0,3]])
# scilence_annotations = mne.Annotations(onset = final_scilence_list, duration = 60, description = 'scilence')

# # #plot_data
# x = raw_selection[1]
# y = raw_selection[0].T
# plt.plot(x, y)
# plt.show()

# ica = mne.preprocessing.ICA(n_components=7, random_state=97, max_iter=1000)
# ica.fit(raw)
# ica.exclude = [1, 2]  # details on how we picked these are omitted here
# ica.plot_properties(raw, picks=ica.exclude)

# ica = ICA(n_components=21, max_iter='auto', random_state=97)
# ica.fit(filt_raw)

# print(filt_raw.info)

# ica.plot_sources(filt_raw, show_scrollbars=False, block = True)
# # ica.plot_components()
# ica.plot_overlay(raw, exclude=[0], picks='eeg')
# ica.plot_properties(raw, picks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# exclusion_matrix 
# while exclusion_matrix_stop < 1: 
#     list_of_exclusions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,  13, 14, 15, 16, 17, 18, 19]
#     list_of_exclusion_lists.append(list_of_exclusions)
#     list_of_exclusions.pop(0)
    
#     if iteration == 19:
#         list_of_exclusions = list_of_exclusions.pop(iteration)
#         iteration
        