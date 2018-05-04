# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:09:56 2018

@author: Gaurav Roy
"""

from nest import nested_structure
from ratio import listof_sentences
from collections import OrderedDict

dict_books = OrderedDict()
dict_books = nested_structure()
list_sentences = listof_sentences(dict_books)