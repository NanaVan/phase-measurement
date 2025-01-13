"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Python Block to change signal 0 to signal 1 based on the pulse"""

    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Signal Switch',   # will show up in GRC
            in_sig=[np.complex64,np.complex64,np.int32],
            out_sig=[np.complex64]
        )
        

    def work(self, input_items, output_items):
        """pulse 1: signal 0 on, signal 1 off; pulse -1: signal 0 off, signal 1 off"""
        if input_item[0][2] == 1:
            output_items[0][:] = input_items[0][1]
        else:
            output_items[0][:] = input_items[0][2]
        return len(output_items[0])
