"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Select bin for phase based on frequency input"""

    def __init__(self, input_freq=100, point_size=2048, samp_rate=32000):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Bin Select',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.input_freq = input_freq
        self._freq_sink = np.linspace(-samp_rate/2, samp_rate/2, num=point_size)

    def work(self, input_items, output_items):
        """Pick up bin from inputs based on the frequency input"""
        _bin_num = np.searchsorted(self._freq_sink, self.input_freq, side='left')
        if _bin_num == len(self._freq_sink):
            _bin_num = len(self._freq_sink) - 1
        print('input: {:}, output: {:}'.format(input_items[0].shape, output_items[0].shape))
        output_items[0][:] = input_items[0][_bin_num]
        return len(output_items[0])
