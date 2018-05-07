# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:30:42 2018

@author: Gaurav Roy
"""

#%% Imports
import re

#%% Function to convert dict to list of sentences
def listof_sentences(dict_books):
    
    listof_s = [sentence[0] for chapter in dict_books.values() for para in chapter.values() for sentn \
                in para.values() for sentence in sentn.values()]
    
    return(listof_s)
  
#%% Function to group sentences by books    
def listof_chapsent(dict_books): 
    listof_chdicts = [[] for _ in range(0, len(dict_books))]
    for book_ix, chapter in enumerate(dict_books.values()):
        for para in chapter.values():
            for sentn in para.values():
                for sentence in sentn.values():
                    listof_chdicts[book_ix].append(sentence[0])
    
       
    return(listof_chdicts)

        
#%% Function for calculating Ratio of Direct speech to Indirect speech
def ratioSpeech(dict_books):
    list_sentences = listof_sentences(dict_books)
    ratios = []
    for index, element in enumerate(list_sentences):
        material = str(element)               
        regex = r'“(.*?)”'
        direct_speech_list = re.findall(regex, material)
        direct_speech = len(direct_speech_list)
        indirect_speech = len(list_sentences) - direct_speech
        ratio = direct_speech/indirect_speech
        ratios.append(ratio)

        if index == 0:
            print("Number of direct speech sentences in total is: %s", direct_speech)
            #print(direct_speech)
            print("Ratio of direct speech to indirect speech in total is: ", "{0:.2f}".format(ratios[index]))
            #print("{0:.2f}".format(ratio))
    
            print("\n -----------------------------------------------\n")            
        else:
            print("Number of direct speech sentences in Chapter %s is: %s", str(index), direct_speech)
            #print(direct_speech)
            print("Ratio of direct speech to indirect speech in Chapter %s is: ", str(index), "{0:.2f}".format(ratios[index]))
            #print("{0:.2f}".format(ratio))
    
            print("\n -----------------------------------------------\n")
    
    
    return(ratios)
