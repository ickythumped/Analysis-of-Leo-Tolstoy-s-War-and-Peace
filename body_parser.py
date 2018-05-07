# -*- coding: utf-8 -*-
"""
File contains the following functions: 
    parseBody() --> 1. Parses the Original text file and retains only the Body
                    2. Writes retained Body to a text file 'body_of_text.txt'

"""
import sys
def parseBody(original, parsed):
    filename = original
    body = parsed
    parser_start = "BOOK ONE: 1805\n"
    parser_end = "End of the Project Gutenberg EBook of War and Peace, by Leo Tolstoy\n"
    flag = 0
    
    try:
        with open(filename, "r", encoding="UTF8") as file1, open(body, "w", encoding="UTF8") as file2:
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
        print (filename, "file doesn't exist")
        print("\n -----------------------------------------------\n")
        sys.exit(1)