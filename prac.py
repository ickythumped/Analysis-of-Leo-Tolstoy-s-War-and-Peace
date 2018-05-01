# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:33:45 2018

@author: Gaurav Roy
"""

import re

twitter_file = "twitter.txt"
pattern = r'^[A-Z].*(@[a-zA-Z0-9_]+|#[A-Za-z0-9_]+)$'
def read_file(file):
    return [l.rstrip() for l in open(file, "r", encoding="UTF8")]

def ex12_sol(file):
    for l in read_file(file) :
        if re.findall(pattern, l):
            print(l)

#print(len(ex12_sol(twitter_file)))
ex12_sol(twitter_file)