# -*- coding: utf-8 -*-
"""
RUN THIS FILE

CHANGE FILENAME OF INPUT TEXT FILE TO 'apple_file.txt'

---------------------------
File contains the following functions:
    1. parseBody()        -->  1. Parses the Original text file and retains only the Body
                               2. Writes retained Body to a text file 'body_of_text.txt
    
    2. nestedStructure()  -->  Parses and stores the text in a OrderedDict in an organized structure.
    
    3. serializeData()    -->  Writes OrderedDict to JSON file 'serialized_corpus.json'

    4. ratioSpeech()      -->  1. Calculates ratio of direct to indirect speech of each book
                               2. Calulcates overall ratio of direct to indirect speech in corpus
                               3. Plots the ratios in a bar plot

    5. bookLength()       -->  Returns a stacked horizontal bar plot of the length of Books and
                               Chapters according to word count
 
    6. wordFreqAnalysis() -->  1. Generates a frequency count of words present in the text.
                               2. Writes table of frequency count to csv file 'word_freq.csv'
                               3. Generates a Freq Dist plot of the top 50 common words
                               4. Generates a Word Cloud of the top 500 words
                      
"""
from body_parser import parseBody
from nest import nestedStructure
from serialized_json import serializeData
from ratio import ratioSpeech
from length_chap_books import bookLength
from word_count import wordFreqAnalysis

file1 = 'apple_file.txt'
file2 = 'body_of_text.txt'

#%% Body parser
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
