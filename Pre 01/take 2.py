import os
import numpy as np
import mne
import matplotlib.pyplot as plt

#load_data
sample = 'Event11.edf'
raw = mne.io.read_raw_edf(sample, infer_types= True, preload=True)
# raw.crop(tmax = 120).load_data()
print(raw)
raw.__len__()
print(raw.info)

#total_Plot
raw.plot_psd(fmax=50)
raw.plot(duration=5, n_channels=30, verbose = True, block = True)


# #data_selection
sampling_freq = raw.info['sfreq']
start_stop_seconds = np.array([11, 21])
start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
channel_index = 24
raw_selection = raw[channel_index, start_sample:stop_sample]
print(raw_selection)

# #plot_data
x = raw_selection[1]
y = raw_selection[0].T
plt.plot(x, y)
plt.show()






# ica = mne.preprocessing.ICA(n_components=7, random_state=97, max_iter=1000)
# ica.fit(raw)
# ica.exclude = [1, 2]  # details on how we picked these are omitted here
# ica.plot_properties(raw, picks=ica.exclude)