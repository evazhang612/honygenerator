#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
model_embeddings.py: Embeddings for the NMT model
Pencheng Yin <pcyin@cs.cmu.edu>
Sahil Chopra <schopra8@stanford.edu>
Anand Dhoot <anandd@stanford.edu>
Michael Hahn <mhahn2@stanford.edu>
"""
import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F
from cnn import CNN
from highway import Highway
# Do not change these imports; your module names should be
#   `CNN` in the file `cnn.py`
#   `Highway` in the file `highway.py`
# Uncomment the following two imports once you're ready to run part 1(j)

# from cnn import CNN
# from highway import Highway

# End "do not change"

class ModelEmbeddings(nn.Module):
    """
    Class that converts input words to their CNN-based embeddings.
    """
    def __init__(self, embed_size, vocab):
        """
        Init the Embedding layer for one language
        @param embed_size (int): Embedding size (dimensionality) for the output
        @param vocab (VocabEntry): VocabEntry object. See vocab.py for documentation.
        """
        super(ModelEmbeddings, self).__init__()


        # pad token is 0

        ## A4 code
        self.e_char = 50
        self.e_word = embed_size
        pad_token_idx = vocab.char2id['<pad>']
        self.embeddings = nn.Embedding(len(vocab.char2id), self.e_char, padding_idx=pad_token_idx)
        ## End A4 code

        ### YOUR CODE HERE for part 1j
        self.embed_size = embed_size
        self.dropout = nn.Dropout(p=0.3)
        self.cnn = CNN(self.e_char, self.e_word) # (batchsize N, numchannels C, length of signal sequance) to (N, cout, Lout)
        self.highway = Highway(self.e_word)
        ### END YOUR CODE

    def forward(self, input):
        """
        Looks up character-based CNN embeddings for the words in a batch of sentences.
        @param input: Tensor of integers of shape (sentence_length, batch_size, max_word_length) where
            each integer is an index into the character vocabulary

        @param output: Tensor of shape (sentence_length, batch_size, embed_size), containing the
            CNN-based embeddings for each word of the sentences in the batch
        """
        ## A4 code
        #
        # return output
        ## End A4 code

        ### YOUR CODE HERE for part 1j
        #print(input.size()) # 10 5 21
        sentence_length = input.size()[0]
        batch_size = input.size()[1]
        x_emb = self.embeddings(input) # (sentence_length, batch_size, max_word_length, e_char)
        x_reshape = torch.reshape(x_emb, (x_emb.size()[0]*x_emb.size()[1], x_emb.size()[2], x_emb.size()[3])) # (batch_size*sentence_length, max_word_length, e_char) ????????????? |
        x_permuted = x_reshape.permute(0,2,1) # (batch_size*senLength, e_char, max_word_length)
        # print(x_permuted.size())
        x_cnnout = self.cnn(x_permuted) # shape (batchsize*senlength, e_word)
        # print(x_cnnout.size()) #
        x_highway = self.highway(x_cnnout) # input (batchsize*senlength, e_word)
        x_wordemb = self.dropout(x_highway) # output (batchsize*senlength, e_word)
        return x_wordemb.reshape(sentence_length, batch_size, self.embed_size)

        #CharEmbedding



        ### END YOUR CODE
