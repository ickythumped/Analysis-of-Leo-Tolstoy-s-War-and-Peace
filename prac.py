# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:43:34 2018

@author: Gaurav Roy
"""
from nest import nestedStructure

listof_sentn = [] 
listof_chdicts = []
listof_s = []
#listof_s = [[] for _ in range(17)]

file2 = 'body_of_text.txt'
dict_books = nestedStructure(file2)
listof_chdicts = [[] for _ in range(0, len(dict_books))]
for book_ix, chapter in enumerate(dict_books.values()):
    for para in chapter.values():
        for sentn in para.values():
            for sentence in sentn.values():
                listof_sentn.append(sentence[0])
                listof_chdicts[book_ix].append(sentence[0])
    
listof_s = [listof_sentn] + listof_chdicts