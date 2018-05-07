# -*- coding: utf-8 -*-
"""
File contains the following functions:
    wordFreqAnalysis() --> 1. Generates a frequency count of words present in the text.
                           2. Writes table of frequency count to csv file 'word_freq.csv'
                           3. Generates a Freq Dist plot of the top 50 common words
                           4. Generates a Word Cloud of the top 500 words
"""

#%% Imports
import csv
from ratio import listof_sentences
from nltk.tokenize import  RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from addStopWords import add_stopwords

#%% Function for Word Frequency Analysis
def wordFreqAnalysis(dict_books):
    
    #%% Retrieving data
    list_sentences = listof_sentences(dict_books)
    
    #%% NLP
    # Only words - no digits or special characters
    wordonly_tokenizer = RegexpTokenizer(r'\w+')
    words_sentences = [wordonly_tokenizer.tokenize(sentence) for sentence in list_sentences]
    
    # List of list of words
    words_list = [word for element in words_sentences for word in element]
    
    # All lowercase
    words_lower = [wlo.lower() for wlo in words_list]
    
    # Removing stopwords
    manual_SW = add_stopwords()
    fullset_SW = stopwords.words('english') + manual_SW
    stopWords = set(fullset_SW)   
    words_filtered = [w for w in words_lower if w not in stopWords]
    
    # Removing single letter words
    words_letter = [wle for wle in words_filtered if len(wle) > 1]     
    
    # Removing a2, c45 etc
    words_alpha = [wa for wa in words_letter if not any(c.isdigit() for c in wa)]
    
    # Lemmatizations     
    lemmatizer = WordNetLemmatizer()
    #verb lemmatization
    words_lemmatized_verb = [lemmatizer.lemmatize(wv, 'v') for wv in words_alpha]
    #adjective lemmatization
    words_lemmatized_adj = [lemmatizer.lemmatize(wadj, 'a') for wadj in words_lemmatized_verb]
    #adverb lemmatization
    words_lemmatized_adv = [lemmatizer.lemmatize(wadv, 'r') for wadv in words_lemmatized_adj]
    #noun lemmatization
    words_lemmatized = [lemmatizer.lemmatize(wl) for wl in words_lemmatized_adv]
    
     
    #%% Dictionary of word count   
    wordcount = FreqDist(wc for wc in words_lemmatized)
#    print("something")
#    # Suppress console temporarily
#    sys.stdout = open(os.devnull, "w")
    wordcount.tabulate(10)
#    sys.stdout = sys.__stdout__
#    print("nothing")
    #%% Write to table (csv file)
    file_freqtable = "word_freq.csv"
    try:
        with open(file_freqtable, "x") as fp:
            writer = csv.writer(fp)
            writer.writerows(wordcount.items())
        print (file_freqtable, "file is created")
        print("\n -----------------------------------------------\n")
    except IOError:
        print (file_freqtable, "file already exists")
        print("\n -----------------------------------------------\n")
    
    #%% Word count plot
    print("Plotting Word Count")
    print("\n -----------------------------------------------\n")
    
    ttl = "Word Count for Top 50 Words" 
    plt.figure(figsize = (40, 20))
    wordcount.plot(50)
    plt.title(ttl, fontsize = 80)
    #plt.xlabel("Words", fontsize = 26, style = "oblique")
    plt.ylabel("Frequency of Words", fontsize = 38, style = "oblique")
    ax = plt.gca()
    ax.set_xticklabels(ax.get_xticklabels(), fontdict = {'fontsize' : 30})
    #yticks = [400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
    ax.set_yticklabels(ax.get_yticks(), fontdict = {'fontsize' : 30})
    plt.show()
    
    #%% Word cloud
    WC_height = 800
    WC_width = 1600
    WC_max_words = 500
    
    wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)
     
    # Plotting Word cloud with most frequently occurring words (unigrams)
    print("Plotting Word Cloud")
    print("\n -----------------------------------------------\n")
    wordCloud.generate_from_frequencies(wordcount)
    plt.figure(figsize = (36, 18))
    plt.title('Most frequently occurring words (unigrams)', fontsize = 60)
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()    