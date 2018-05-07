# -*- coding: utf-8 -*-
"""
File contains the following functions:
    
    listof_sentences() --> Converts OrderedDict() to a whole list of sentences
    
    listof_chapsent() --> Converts OrderedDict() to a list of sentences book-wise
    
    ratioSpeech() --> 1. Calculates ratio of direct to indirect speech of each book
                      2. Calulcates overall ratio of direct to indirect speech in corpus
                      3. Plots the ratios in a bar plot

@author: Gaurav Roy
"""

#%% Imports
import re
import matplotlib.pyplot as plt
import numpy as np

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
    
    
    book_names = [1, 2, 3, 4, 5, 6, 7, 8, \
                  9, 10, 11, 12, 13, 14, 15,\
                  16, 17]
    
    fig, ax = plt.subplots(figsize = (40, 20))
    plt.bar(book_names, ratios, width = 0.3)
    ax.set_title("Ratios of Direct to Indirect Speech for all Books", fontsize = 65)
    ax.set_xlabel("Book Number", fontsize = 40, style = "oblique")
    ax.set_ylabel("Ratio", fontsize = 40, style = "oblique")
    ax.set_yticklabels(ax.get_yticks() ,fontdict = {'fontsize' : 30})
    plt.xticks(np.arange(min(book_names), max(book_names)+1, 1.0))
    ax.tick_params('x', labelsize = 25)
    ax.axhline(total_ratio, color="black")
    ax.text(0.71, 0.67, " Overall ratio = 0.43", fontsize = 30, fontweight = 'bold',\
            va='center', ha="left",\
            bbox=dict(facecolor="w",alpha=0.5), transform=ax.transAxes)
    

    
    
