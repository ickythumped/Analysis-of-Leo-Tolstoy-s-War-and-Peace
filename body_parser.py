# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:57:20 2018

@author: Gaurav Roy
"""

def parseBody(original, parsed):
    filename = original
    body = parsed
    parser_start = "BOOK ONE: 1805\n"
    parser_end = "End of the Project Gutenberg EBook of War and Peace, by Leo Tolstoy\n"
    flag = 0
    
    try:
        with open(filename, "r", encoding="UTF8") as file1, open(body, "x", encoding="UTF8") as file2:
            for line in file1:
                if line == parser_start:
                    flag = 1
                if line == parser_end:
                    break
                if flag == 1:
                    file2.write(line) 
                    
        print(body, "file is created")
        print("\n -----------------------------------------------\n")
        
    except IOError:
        print (body, "file already exists")
        print("\n -----------------------------------------------\n")