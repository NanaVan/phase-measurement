"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from scipy.signal import correlate


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Calculate cross-correlation of two time series"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Cross Correlation',   # will show up in GRC
            in_sig=[np.complex64, np.complex64],
            out_sig=[np.complex64]
        )
        

    def work(self, input_items, output_items):
        """Using numpy cross-correlation function"""
        output_items[0][:] = correlate(input_items[0], input_items[1], 'same')
        return len(output_items[0])
