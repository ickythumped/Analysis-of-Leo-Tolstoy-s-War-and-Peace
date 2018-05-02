# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:02:51 2018

@author: Gaurav Roy
"""
import re
from collections import defaultdict
from collections import OrderedDict

filename = "body_of_text.txt"
pattern_book = "BOOK"
pattern_chapter = "CHAPTER"
regex_book = r'(.*)'
regex_chapter = r'(.*?)'

list_words = []
list_books = []
list_chapters = []
#count=0

#            
with open(filename, "r", encoding="UTF8") as file:
    data = file.read().replace('\n', ' ')
            
            
with open(filename, "r", encoding="UTF8") as file:
    for l in file:
        if re.match(pattern_book, l):
            list_books.append(l.strip('\n'))
        if re.match(pattern_chapter, l):
            list_chapters.append(l.strip('\n'))
            
count=0
for x in range(0,len(list_books)-1):           
    regex = re.compile(list_books[x] + regex_book + list_books[x+1])
    print(regex)
    content = re.findall(regex, data)
    current_count=content[0].count("CHAPTER")
    print(current_count)
    break
    for y in range(count,count+current_count-1):
        #print (list_chapters[y+1])
        regex = re.compile(list_chapters[y]+regex_chapter+list_chapters[y+1])
        para = re.findall(regex, content[0])
        #print(para)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    count=count+current_count
    print(count)      
                
             

   