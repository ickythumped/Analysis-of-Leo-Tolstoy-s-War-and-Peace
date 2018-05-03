# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:30:42 2018

@author: Gaurav Roy
"""

#%% Imports
from nest import nested_structure
import re

#%% Function to convert dict to list
def listof_sentences(dict):
    listof_sentn = []
    for chapter in dict.values():
        for para in chapter.values():
            for sentn in para.values():
                for sentence in sentn.values():
                    listof_sentn.append(sentence[0])
    return(listof_sentn)

#%% Calculating Ratio
dict_book = nested_structure()
list_sentences = listof_sentences(dict_book)
material = str(list_sentences)               
regex = r'“(.*?)”'
direct_speech_list = re.findall(regex, material)
direct_speech = len(direct_speech_list)
indirect_speech = len(list_sentences) - direct_speech

ratio = direct_speech/indirect_speech

print("Ratio of direct speech to indirect speech is:")
print("{0:.2f}".format(ratio))
