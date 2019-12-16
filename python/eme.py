#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import re
import nltk
from collections import Counter
import  funcoes as func 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import tokenize
from dao.eme import Eme as emem

nltk.download('treebank')
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('punkt')

  
# from nltk.book import *
texto2 = []
segmentador_frases=nltk.data.load('tokenizers/punkt/portuguese.pickle') 

def processar_eme(text, id_pessoa, id_texto):

    text22 = text.replace("!","")
    texto22 = word_tokenize(text)


    # print ("Extensão Média do Enunciado")
    #numero_de_palavras / numero_de_enunciados

    segmentador_frases =nltk.data.load('tokenizers/punkt/portuguese.pickle')  
    frases=segmentador_frases.tokenize(text)
    numero_de_frases = len(frases)
    numero_de_frases = round(numero_de_frases,2)
    # print("Numero de frases encontradas:", numero_de_frases)
    texto_c =func.converter(text)
    total_palavras = len(texto_c.split())
    # print ("numero de palavras:" + str(total_palavras))
    eme = total_palavras / numero_de_frases 
    eme = round(eme,2) 
    # print ("Extensao media do enunciado:", eme)
    e = emem(total_palavras, eme, id_pessoa,id_texto)
    e.inserir()