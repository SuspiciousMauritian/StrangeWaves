import os
from pickle import TRUE
import numpy as np
import mne


sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                    'sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)


print(raw)
print(raw.info)


raw.plot_psd(fmax=50)
raw.plot(duration=5, n_channels=30, theme = 'light', verbose = True, block = True)
