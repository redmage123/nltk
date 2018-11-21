#!/usr/bin/env python3

import nltk

sentence = 'Fee Fi Fo Fum, I smell the blood of an Englishman'
tokens = nltk.tokenize.api.word_tokenize(sentence)
print (tokens)
