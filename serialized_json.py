# -*- coding: utf-8 -*-
"""
Created on Thu May  3 00:09:58 2018

@author: Gaurav Roy
"""
#%% Imports
import json

#%% Creating serialized JSON file
def serializeData(dict_book):
    file_json = 'serialized_corpus.json'
    try:
        with open(file_json, 'x') as fp:
            json.dump(dict_book, fp)
            
        print(file_json, "file is created")
        print("\n -----------------------------------------------\n")
    
    except IOError:
        print(file_json, "file already exists")
        print("\n -----------------------------------------------\n")