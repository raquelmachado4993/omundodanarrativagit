#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import nltk
from collections import Counter
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import tokenize  
import  funcoes as func 
#from nltk.book import *
texto2 = []
segmentador_frases=nltk.data.load('tokenizers/punkt/portuguese.pickle') 
text = "Eu sabia! Era verdade! Ela não me disse ela não me disse eu sabia mesmo dinossauro."
texto22 = func.converter(text)
texto22 = word_tokenize(text)

size = len(texto22)
#print len(texto2)
variavel_float_token = float(size)
variavel_float_token_ok = round(variavel_float_token,2)
print ("Tokens:", variavel_float_token_ok) 

texto3 = sorted(set(texto22))
print ("eu sou um sort " + str(texto3)) 
wordtype =len(set(texto3))
variavel_float_type = float(wordtype)
variavel_float_type_ok = round(variavel_float_type,2)
print ("Types:", variavel_float_type_ok)


ls = variavel_float_type_ok / variavel_float_token_ok
relacao_type_tokenc = round(ls, 2)

print ("Relacao Type-Token", relacao_type_tokenc) 
print ("\n")
print ("--------------fim -----------------")