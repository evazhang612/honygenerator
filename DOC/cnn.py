#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#nn.Conv1d

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1i

from collections import namedtuple
import sys
from typing import List, Tuple, Dict, Set, Union
import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F

### YOUR CODE HERE for part 1h
class CNN(nn.Module):
    def __init__(self, e_char, e_word, k=5):
        # xreshaped to x_convout || nn.Conv1d || filter??
        # input is size of embedding for char
        super(CNN, self).__init__()
        self.conv = nn.Conv1d(e_char, e_word, k) # number of output channels is kernel number (# filters)
        # self.dropout = torch.nn.Dropout(p=dropout_rate)


    def forward(self, x_reshaped: torch.Tensor) -> torch.Tensor:
        x_conv = self.conv(x_reshaped) # (batch_size*senLength, e_char, max_word_length) -> batchsize, numberofchannels out = e_word, outputsize=numgreen dots
        x_relu = F.relu(x_conv)
        max_pool = torch.max(x_relu, 2)[0] # should be (mword−k+1) since its number of green dots.. max of the green dots
        return max_pool # shape (batchsize*senlength, e_word)
### END YOUR CODE
