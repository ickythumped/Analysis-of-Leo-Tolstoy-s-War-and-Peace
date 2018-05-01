# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:02:51 2018

@author: Gaurav Roy
"""
import re
from collections import defaultdict
from collections import OrdereDdict

filename = "body_of_text.txt"
pattern_book = "BOOK"
pattern_chapter = "CHAPTER"

dict_book = defaultdict(list)
dict_chap = defaultdict(list)
dict_para = {}
dict_sentence = {}


def read_file(file):
    return [l for l in open(file, "r", encoding="UTF8")]

def main(file):
    for l in read_file(file):
        if re.match(pattern_book, l):
            dict_book = {l: {}}
            if re.match(pattern_chapter, l):
                dict_chap = {l: {}}
                
    print(dict_book)
main(filename)

   