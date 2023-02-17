#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:47:25 2023

@author: sophieross
"""
import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana cheese none sophie')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Banana and apple rate highly because they are both fruits
# Monkey and cat rate highly because they are both animals
# Cheese rates highly compared to apple/banana since it is a food but not as high as banana to apple since it is not a fruit 
# None rates the lowest in similarity to other words since it is neither an animal nor a food

