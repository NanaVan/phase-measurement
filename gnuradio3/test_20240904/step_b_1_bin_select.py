# this module will be imported in the into your flowgraph
import numpy as np

def select_binNum(samp_rate, point_size, freq):
    freq_range = np.linspace(-samp_rate/2, samp_rate/2, num=point_size)
    bin_num = np.searchsorted(freq_range, freq, side='left')
    if bin_num >= len(freq_range):
        bin_num -= 1
    bin_num = point_size - bin_num
    return bin_num
