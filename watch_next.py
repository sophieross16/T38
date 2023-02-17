#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:58:57 2023

@author: sophieross
"""

# Compulsory Task 2
import spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

'''
Input: description
Output: title of the most similar movie
Description: this function reads a list of movies and their descriptions from a txt file, then compares an inputted description to those in the file. It then outputs the movie, similarity value and corresponding description
'''

def movie_similarity(description):
    # Initialising a nested list of movies and their description from the txt file
    movies = []
    with open('movies.txt','r') as movie_file:
        for line in movie_file:
            movie = line.split(':')
            movies.append(movie)
    # Initiliases a list to store the movie name and similarity value
    similarities = []
    # Compare inputted description to other descriptions in the nested list
    for movie in movies:
    # Applying NLP to the inputted and iterated description to find the similarities
        iterated_description = nlp(movie[1])
        similarity = nlp(description).similarity(iterated_description)
    # Adding the movie, description and similarity value to the similarities list
        similarity_val = [movie[0], movie[1], similarity]
        similarities.append(similarity_val)
    # Initialising the highest simlarity value as 0 in order to find the largest
        highest_val = 0
    for index in similarities:
        if index[2] > highest_val:
            highest_val = index[2]
            highest_movie = index[0]
            highest_description = index[1]
    # Outputting results to the user
    print(f'\n{highest_movie} is the most similar to your description, with a similarity value of {highest_val:.2f}.')
    print(f'\nDescription: {highest_description}')

# Testing function
inputted_description = input('Enter a movie description: ')
movie_similarity(inputted_description)