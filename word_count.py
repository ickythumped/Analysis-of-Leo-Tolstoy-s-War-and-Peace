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

wordonly_tokenizer = RegexpTokenizer(r'\w+')
words_sentences = [wordonly_tokenizer.tokenize(sentence) for sentence in list_sentences]

words_list = [word for element in words_sentences for word in element]

stopWords = set(stopwords.words('english'))   
words_filtered = [w for w in words_list if w not in stopWords]     

words_alpha = [wa for wa in words_filtered if not any(c.isdigit() for c in wa)]
     
lemmatizer = WordNetLemmatizer()
words_lemmatized = [lemmatizer.lemmatize(wf) for wf in words_alpha]
    
table_wordcount = FreqDist(wl.lower() for wl in words_lemmatized)
    


    