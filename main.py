# -*- coding: utf-8 -*-
"""
Created on Tue May  1 02:37:13 2018

@author: Gaurav Roy
"""
import pandas as pd
import nltk

filename = "apple_file.txt"
body = "body_of_text.txt"
parser_start = "BOOK ONE: 1805\n"
parser_end = "End of the Project Gutenberg EBook of War and Peace, by Leo Tolstoy\n"
flag = 0

with open(filename, "r", encoding="UTF8") as file1, open(body, "x", encoding="UTF8") as file2:
    for line in file1:
        if line == parser_start:
            flag = 1
        if line == parser_end:
            break
        if flag == 1:
            file2.write(line)