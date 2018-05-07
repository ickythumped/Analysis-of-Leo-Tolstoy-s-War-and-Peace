# -*- coding: utf-8 -*-
"""
File contains the following functions:
    nestedStructure() --> Parses and stores the text in a OrderedDict in the following structure:
                            {Books:
                                {Chapters:
                                    {Paragraphs:
                                        {Sentences:
                                            Sentences[]
                                            {Words:
                                                Word
                                            }
                                        }
                                    }
                                }
                            }
                        
                          Returns OrderedDict()
"""
#%% Imports

import re
from collections import OrderedDict
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from itertools import count

#%% FUNCTION
def nestedStructure(file):
    #%% Strings
    
    filename = file
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
    
    ## Last Chapters
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
    chapter_paras = [chapter_content[w][0].split("  ") for w in range(0, len(chapter_content))]
#    chapter_paras = []
#    for w in range(0, len(chapter_content)):
#        chapter_paras.append(chapter_content[w][0].split("  "))
    
    ## Creating para of sentences list
    para_sentences = [sent_tokenize(chapter_paras[s][t]) for s in range(0, len(chapter_paras)) \
                      for t in range(0, len(chapter_paras[s]))]
#    para_sentences = []
#    for s in range(0, len(chapter_paras)):
#        for t in range(0, len(chapter_paras[s])):
#            para_sentences.append(sent_tokenize(chapter_paras[s][t]))
    
    ## Creating sentence of words list
    wordonly_tokenizer = RegexpTokenizer(r'\w+')
    sentence_words = [wordonly_tokenizer.tokenize(u[v]) for u in para_sentences for v in range(0, len(u))]
#    sentence_words = []      
#    for u in para_sentences:
#        for v in range(0, len(u)):
#            sentence_words.append(wordonly_tokenizer.tokenize(u[v]))
            
    #%% Creating dictionaries
    
    ## Creating word dictionary
    word_dict = OrderedDict()
    word = "Word: "
    for i, sen in enumerate(sentence_words):
        tempdict1 = OrderedDict()
        for j in range(0, len(sen)):
            tempdict1[word + str(j+1)] = sen[j]
        word_dict[str(i+1)] = tempdict1   
    
    ## Creating sentence and para dictionaries
    para_dict = OrderedDict()
    sentence = "Sentence: "
    para = "Paragraph: "
    sequence1 = count(start = 1, step = 1)
    for k in range(0, len(para_sentences)):
        sentence_dict= OrderedDict()
        for m in range(0, len(para_sentences[k])):
            sentence_dict.setdefault(sentence + str(m+1), []).append(para_sentences[k][m])
            sentence_dict.setdefault(sentence + str(m+1), []).append(word_dict[str(next(sequence1))])
        para_dict[para + str(k+1)] = sentence_dict
    
    ## Creating chapter dictionaries
    chapter_dict = OrderedDict()
    chapter = "Chapter: "
    sequence2 = count(start = 1, step = 1)
    for n in range(0, len(chapter_paras)):
        tempdict2 = OrderedDict()
        for p in range(0, len(chapter_paras[n])):
            tempdict2[para + str(p+1)] = para_dict[para + str(next(sequence2))]
        chapter_dict[chapter + str(n+1)] =  tempdict2
        
    
    #%% FINAL NESTED STRUCTURE
    
    ## Creating dictionary of books
    dictionary_books = OrderedDict()
    book = "Book: "
    sequence3 = count(start = 1, step = 1)
    for q in range(0, len(list_books)):
        tempdict3 = OrderedDict()
        for r in range(0, chapter_count[q]):
            tempdict3[chapter + str(r+1)] = chapter_dict[chapter + str(next(sequence3))]
        dictionary_books[book + str(q+1)] = tempdict3

    #%% RETURN
    return(dictionary_books)
    