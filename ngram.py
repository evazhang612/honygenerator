#!usr/local/bin/

import pandas as pd 
import re
import nltk.tokenize 
import markovify
from nltk.util import ngrams 

import subprocess
import sys
import markovify


#CONSTANTS 
N = 5 

corpus = pd.read_csv('corpus2.txt', sep = '\n', header = None, error_bad_lines=False)
corpus_list = corpus.values.tolist()

word_tokens = new_corpus = []
n_grams = corpus_grams = []
long_string = ''

for list_i in corpus_list:
	list_n = [] 
	list_grams = []
	for s in list_i: 
		news = nltk.tokenize.wordpunct_tokenize(s.lower())
		grams = list(ngrams(news, N))
		long_string += s 
		list_grams.append(grams)
		list_n.append(news)
	new_corpus.append(list_n)
	corpus_grams.append(list_grams)
 


text_model = markovify.Text(long_string)

for i in range(len(new_corpus)): 
	print(text_model.make_sentence())