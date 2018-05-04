# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:09:56 2018

@author: Gaurav Roy
"""
#%% Run for first time
#import nltk
#nltk.download('wordnet')

#%% Imports
from nest import nested_structure
from ratio import listof_sentences
from nltk.tokenize import  RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist

#%% Retrieving data
dict_books = nested_structure()
list_sentences = listof_sentences(dict_books)

#%% NLP
# Only words - no digits or special characters
wordonly_tokenizer = RegexpTokenizer(r'\w+')
words_sentences = [wordonly_tokenizer.tokenize(sentence) for sentence in list_sentences]

# List of list of words
words_list = [word for element in words_sentences for word in element]

# Removing stopwords
stopWords = set(stopwords.words('english'))   
words_filtered = [w for w in words_list if w not in stopWords]

# Removing single letter words
words_letter = [wle for wle in words_filtered if len(wle) > 1]     

# Removing a2, c45 etc
words_alpha = [wa for wa in words_letter if not any(c.isdigit() for c in wa)]

# Lemmatizations     
lemmatizer = WordNetLemmatizer()
#verb lemmatization
words_lemmatized_verb = [lemmatizer.lemmatize(wv, 'v') for wv in words_alpha]
#adjective lemmatization
words_lemmatized_adj = [lemmatizer.lemmatize(wadj, 'a') for wadj in words_lemmatized_verb]
#adverb lemmatization
words_lemmatized_adv = [lemmatizer.lemmatize(wadv, 'r') for wadv in words_lemmatized_adj]
#noun lemmatization
words_lemmatized = [lemmatizer.lemmatize(wl) for wl in words_lemmatized_adv]
 
# Dictionary of word count   
table_wordcount = FreqDist(wl.lower() for wl in words_lemmatized)
    


    