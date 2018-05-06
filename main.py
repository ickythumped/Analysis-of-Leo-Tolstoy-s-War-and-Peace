# -*- coding: utf-8 -*-
"""
Created on Tue May  1 02:37:13 2018

@author: Gaurav Roy
"""
from body_parser import parseBody
from nest import nestedStructure
from serialized_json import serializeData
from ratio import ratioSpeech
from length_chap_books import bookLength
from word_count import wordFreqAnalysis

file1 = 'apple_file.txt'
file2 = 'body_of_text.txt'
parseBody(file1, file2)

#%% Creating nested structure
dict_books = nestedStructure(file2)

#%% Creating serialized file
serializeData(dict_books)

#%% Calculating ratio of direct to indirect speech
ratioSpeech(dict_books)

#%% Visualizing books and chapters length
bookLength(dict_books)

#%% Performing Word Freq Analysis
wordFreqAnalysis(dict_books)
