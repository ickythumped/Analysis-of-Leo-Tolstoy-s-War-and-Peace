# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:09:56 2018

@author: Gaurav Roy
"""

from nest import nested_structure
from ratio import listof_sentences
from nltk.tokenize import  RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

dict_books = nested_structure()
list_sentences = listof_sentences(dict_books)
words_sentences = []
words_list = []
words_filtered = []
words_lemmatized = []



wordonly_tokenizer = RegexpTokenizer(r'\w+')
for sentence in list_sentences:
    words_sentences.append(wordonly_tokenizer.tokenize(sentence))

for element in words_sentences:
    for word in element:
        words_list.append(word)

stopWords = set(stopwords.words('english'))        
for w in words_list:
    if w not in stopWords:
        words_filtered.append(w)
        
words_alpha = [wa for wa in words_filtered if not any(c.isdigit() for c in wa)]
     
lemmatizer = WordNetLemmatizer()
for wf in words_alpha:
    words_lemmatized.append(lemmatizer.lemmatize(wf))
    
fdist = FreqDist(wl.lower() for wl in words_lemmatized)
    


    