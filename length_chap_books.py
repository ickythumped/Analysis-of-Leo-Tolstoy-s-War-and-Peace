# -*- coding: utf-8 -*-
"""

File contains the following function:
    bookLength() --> Returns a stacked horizontal bar plot of the length of Books and
                     Chapters according to word count


"""

#%% Imports
import pandas as pd

#%% Function for visualization of length of books and chapters
def bookLength(dict_book):
    
    print("Plotting length of books and chapters")
    print("\n -----------------------------------------------\n")
    #%% Initializations
    book_names = [] 
    book_list = []
    
    #%% Extracting word lists for books and chapters
    #sequence2 = count(start = 0, step = 1)
    for book, chapter in dict_book.items():
        book_names.append(book)
        counter1 = 1
        wordsin_chapter = {}
        for para in chapter.values():
            counter2 = 1
            for sentn in para.values():
                for sentence in sentn.values():
                    for word in sentence[1].values():
                        wordsin_chapter[counter1] = counter2
                        counter2 += 1
            counter1 += 1
        book_list.append(wordsin_chapter)
    
    #%% Converting to dataframe
   
    df = pd.DataFrame(book_list, index = book_names)
    chapter_names = ["Chapter "+ str(column+1) for column in range(0, len(df.columns))]
    df.columns = chapter_names
    
    #%% Visualization of length of books and chapters    
    
    ttl = "Length (word count) of chapters and books"
    ax = df.plot(kind = 'barh', stacked = True, figsize = (40, 20))
    ax.set_title(ttl, fontsize = 65)
    ax.set_xlabel("Number of words", fontsize = 40, style = "oblique")
    ax.set_ylabel("Books", fontsize = 40, style = "oblique")
    xticks = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000]
    ax.set_xticklabels(xticks, fontdict = {'fontsize' : 30})
    ax.set_yticklabels(ax.get_yticklabels() ,fontdict = {'fontsize' : 30})
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc = "best", ncol = 6, prop = {'size' : 16})