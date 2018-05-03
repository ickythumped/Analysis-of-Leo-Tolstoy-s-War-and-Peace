# -*- coding: utf-8 -*-
"""
Created on Thu May  3 00:09:58 2018

@author: Gaurav Roy
"""
#%%
from nest import nested_structure
import json

#%% Creating serialized JSON file
dict_book = nested_structure()
file = 'serialized_corpus.json'
try:
    with open(file, 'x') as fp:
        json.dump(dict_book, fp)
except IOError:
    print (file, "File already exists")