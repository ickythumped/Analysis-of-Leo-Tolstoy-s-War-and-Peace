# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:05:06 2018

@author: Gaurav Roy
"""

import re
from collections import defaultdict
from collections import OrderedDict
from nltk.tokenize import sent_tokenize, word_tokenize

filename = "body_of_text.txt"
pattern_book = "BOOK"
pattern_chapter = "CHAPTER"

regex_book = r'(.*?)'
regex_chapter = r'(.*?)'
#regex_para = r'()

book_content = []
chapter_content = []
chapter_paras = []
para_sentences = []
para_content = []
list_words = []
list_books = []
list_chapters = []
          
with open(filename, "r", encoding="UTF8") as file:
    data = file.read().replace('\n', ' ')
            
            
with open(filename, "r", encoding="UTF8") as file:
    for l in file:
        if re.match(pattern_book, l):
            list_books.append(l.strip('\n'))
        if re.match(pattern_chapter, l):
            list_chapters.append(l.strip('\n'))
            
count = 0
for x in range(0,len(list_books)-1):           
    regex1 = re.compile(list_books[x] + regex_book + list_books[x+1])
    #print(regex1)
    book_content.append(re.findall(regex1, data))
    current_count = book_content[x][0].count("CHAPTER")
    print(current_count)
    
    for y in range(count, count + current_count-1):
        #print (list_chapters[y+1])
        
        regex2 = re.compile(list_chapters[y] + regex_chapter + list_chapters[y+1])
        #print(regex2)
        chapter_content.append(re.findall(regex2, book_content[x][0]))

    regex3 = re.compile(list_chapters[y+1] + regex_chapter) #need to change regular expression
    chapter_content.append(re.findall(regex3, book_content[x][0]))    
    count = count + current_count
    print(count)
    
for w in range(0, len(chapter_content)):
    chapter_paras.append(chapter_content[w][0].split("  "))

    
for s in range(0, len(chapter_paras)):
    print(chapter_paras[s])
    for t in range(0, len(chapter_paras[s])):
        print(chapter_paras[s][t])
#        for u in range(t.count('.')):
        #para_sentences.append(sent_tokenize(chapter_paras[s][t][0]))
        
    