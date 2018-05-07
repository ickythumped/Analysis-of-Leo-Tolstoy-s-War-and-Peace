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
    list_chapsentences = listof_chapsent(dict_books)
    ratios = []
    direct_speech = []
    indirect_speech = []
    for index, element in enumerate(list_chapsentences):
        material = str(element)               
        regex = r'“(.*?)”'
        direct_speech_list = re.findall(regex, material)
        direct_speech.append(len(direct_speech_list))
        indirect_speech.append(len(element) - direct_speech[index])
        ratio = direct_speech[index]/indirect_speech[index]
        ratios.append(ratio)
    
    for ix, elem in enumerate(ratios):
            print("Number of direct speech sentences in Book" ,str(ix+1), "is", direct_speech[ix])
            #print(direct_speech)
            print("Number of indirect speech sentences in Book" ,str(ix+1), "is", indirect_speech[ix])
            print("Ratio of direct speech to indirect speech in Book", str(ix+1), "is:", "{0:.2f}".format\
                  (elem))
            #print("{0:.2f}".format(ratio))
    
            print("\n -----------------------------------------------\n")
    
    list_sentences = listof_sentences(dict_books)
    material = str(list_sentences)               
    regex = r'“(.*?)”'
    direct_speech_list = re.findall(regex, material)
    direct_speech = len(direct_speech_list)
    indirect_speech = len(list_sentences) - direct_speech
    total_ratio = direct_speech/indirect_speech
    
    
    print("Number of direct speech sentences in entire corpus is", direct_speech)
    print("Number of indirect speech sentences in entire corpus is", indirect_speech)
    print("Ratio of direct speech to indirect speech in entire corpus is:", "{0:.2f}".format\
          (total_ratio))
    print("\n -----------------------------------------------\n")
    
    ratios_list = ratios
    ratios_list.append(total_ratio)
    
    
    return(ratios_list)
    
    
