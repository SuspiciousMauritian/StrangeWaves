import os
from pickle import TRUE
import numpy as np
import mne

sample = 'Event11.edf'

raw = mne.io.read_raw_edf(sample, infer_types= True)
print(raw.info)
raw.plot_psd(fmax=70)
ica = mne.preprocessing.ICA(n_components=7, random_state=97, max_iter=1000)
ica.fit(raw)
ica.exclude = [1, 2]  
ica.plot_properties(raw, picks=ica.exclude)



