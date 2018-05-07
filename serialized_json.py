# -*- coding: utf-8 -*-
"""
File contains the following functions:
    serializeData() --> writes OrderedDict to JSON file 'serialized_corpus.json' 
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