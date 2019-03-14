#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""
from collections import namedtuple
import sys
from typing import List, Tuple, Dict, Set, Union
import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F

### YOUR CODE HERE for part 1h
class Highway(nn.Module):
    def __init__(self, e_word):
        super(Highway, self).__init__()
        self.embed_size = e_word
        self.w_proj = nn.Linear(self.embed_size, self.embed_size, bias=True) # BIAS??
        self.w_gate = nn.Linear(self.embed_size, self.embed_size, bias=True)


    def forward(self, x_convout: torch.Tensor) -> torch.Tensor:
        x_proj = F.relu(self.w_proj(x_convout))
        sig = nn.Sigmoid()
        x_gate = sig(self.w_gate(x_convout))
        x_highway = x_gate*x_proj + (1-x_gate)*x_convout # (b n m) x (b m p) = (b n p) # TESTS??????
        return x_highway
### END YOUR CODE
