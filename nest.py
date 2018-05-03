# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:05:06 2018

@author: Gaurav Roy
"""
#%% Imports

import re
#from collections import defaultdict
#from collections import OrderedDict
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from itertools import count
#import pandas as pd

#%% FUNCTION
def nested_structure():
    #%% Strings
    
    filename = "body_of_text.txt"
    pattern_book = "BOOK"
    pattern_epilogue1 = "FIRST EPILOGUE"
    pattern_epilogue2 = "SECOND EPILOGUE"
    pattern_chapter = "CHAPTER"
    
    regex_book = r'\s+(.*?)\s+'
    regex_chapter = r'\s+(.*?)\s+'
    regex_lastitem = r'\s+(.*)$'
    
    #%% List Declarations
    
    book_content = []
    chapter_content = []
    chapter_paras = []
    para_sentences = []
    sentence_words = []
    list_books = []
    list_chapters = []
    chapter_count = []
        
    #%% Reading File / list of book titles / list of chapter titles
    
    with open(filename, "r", encoding="UTF8") as file:
        data = file.read().replace('\n', ' ')
                
                
    with open(filename, "r", encoding="UTF8") as file:
        for l in file:
            if re.match(pattern_book, l):
                list_books.append(l.strip('\n'))
            if re.match(pattern_epilogue1, l):
                list_books.append(l.strip('\n'))
            if re.match(pattern_epilogue2, l):
                list_books.append(l.strip('\n'))    
            if re.match(pattern_chapter, l):
                list_chapters.append(l.strip('\n'))
    
    #%%  Creating content lists of books, chapters
    counter = 0
    for x in range(0,len(list_books)-1):           
        regex1 = re.compile(list_books[x] + regex_book + list_books[x+1])
        book_content.append(re.findall(regex1, data))
        current_count = book_content[x][0].count("CHAPTER")
        chapter_count.append(current_count)
        for y in range(counter, counter + current_count-1):        
            regex2 = re.compile(list_chapters[y] + regex_chapter + list_chapters[y+1])
            chapter_content.append(re.findall(regex2, book_content[x][0]))
    
    ## Last chapters
        regex3 = re.compile(list_chapters[y+1] + regex_lastitem)
        chapter_content.append(re.findall(regex3, book_content[x][0]))    
        counter = counter + current_count
    
    #%% Creating content for last book
        
    regex4 = re.compile(list_books[x+1] + regex_lastitem)
    book_content.append(re.findall(regex4, data))
    current_count = book_content[x+1][0].count("CHAPTER")
    chapter_count.append(current_count)    
    for y in range(counter, counter + current_count-1):        
        regex2 = re.compile(list_chapters[y] + regex_chapter + list_chapters[y+1])
        chapter_content.append(re.findall(regex2, book_content[x+1][0]))
    
    ## Last Chapter
    regex3 = re.compile(list_chapters[y+1] + regex_lastitem)
    chapter_content.append(re.findall(regex3, book_content[x+1][0]))    
    counter = counter + current_count
      
    #%% Creating paras, sentences and words lists
    
    ## Creating chapter of paras list
    for w in range(0, len(chapter_content)):
        chapter_paras.append(chapter_content[w][0].split("  "))
    
    ## Creating para of sentences list 
    for s in range(0, len(chapter_paras)):
        for t in range(0, len(chapter_paras[s])):
            para_sentences.append(sent_tokenize(chapter_paras[s][t]))
    
    ## Creating sentence of words list
    wordonly_tokenizer = RegexpTokenizer(r'\w+')        
    for u in para_sentences:
        for v in range(0, len(u)):
            sentence_words.append(wordonly_tokenizer.tokenize(u[v]))
            
    #%% Creating dictionaries
    
    ## Creating word dictionary
    word_dict = {}  
    for i, sen in enumerate(sentence_words):
        tempdict1 = {}
        for j in range(0, len(sen)):
            tempdict1[j+1] = sen[j]
        
        word_dict[i+1] = tempdict1   
    
    ## Creating sentence and para dictionaries
    para_dict = {}
    sequence1 = count(start = 1, step = 1)
    for k in range(0, len(para_sentences)):
        sentence_dict= {}
        for m in range(0, len(para_sentences[k])):
            sentence_dict.setdefault(m+1, []).append(para_sentences[k][m])
            sentence_dict.setdefault(m+1, []).append(word_dict[next(sequence1)])
        para_dict[k+1] = sentence_dict
    
    ## Creating chapter dictionaries
    chapter_dict = {}
    sequence2 = count(start = 1, step = 1)
    for n in range(0, len(chapter_paras)):
        tempdict2 = {}
        for p in range(0, len(chapter_paras[n])):
            tempdict2[p+1] = para_dict[next(sequence2)]
        chapter_dict[n+1] =  tempdict2
        
    
    #%% FINAL NESTED STRUCTURE
    
    ## Creating dictionary of books
    dictionary_books = {}
    sequence3 = count(start = 1, step = 1)
    for q in range(0, len(list_books)):
        tempdict3 = {}
        for r in range(0, chapter_count[q]):
            tempdict3[r+1] = chapter_dict[next(sequence3)]
        dictionary_books[q+1] = tempdict3

    #%% RETURN
    return(dictionary_books)
    