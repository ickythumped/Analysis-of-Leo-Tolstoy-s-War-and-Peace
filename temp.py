# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:43:20 2018

@author: Gaurav Roy
"""


filename = "body_of_text.txt"
pattern_book = "BOOK"
pattern_chapter = "CHAPTER"
regex_book = r'(.*)'
regex_chapter = r'CHAPTER (.*)  '

list_words = []
list_books = []
list_chapters = []



def read_file(file):
    return [l for l in open(file, "r", encoding="UTF8")]

def main(file):
    for l in read_file(file):
        if re.match(pattern_book, l):
            list_books.append(l.strip('\n'))

    with open(filename, "r", encoding="UTF8") as file:
        for line in file:
            for x in range(0,len(list_books)-1):           
                regex = re.compile(list_books[x] + regex_book + list_books[x+1])
                content = re.findall(regex, line)
                print(content)
                break
#            list_chapters = re.findall(re.compile(regex_chapter), content)
                
main(filename)