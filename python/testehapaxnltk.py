#!/usr/bin/python3
# -*- coding: utf-8 -*-
import funcoes as fun
import nltk 
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
pos = {}
texto = "Era uma vez um lugarzinho. era uma vez uma quitanda."
texto = fun.converter(texto)


palavras = word_tokenize(texto.lower())
fdist1 = FreqDist(palavras)
qtd_palavras_texto = len(palavras)
print (fdist1.hapaxes())
numerodehapaxes =  len((fdist1.hapaxes()))
print ("numero de hapaxes:" , numerodehapaxes)
print ("Quantidade de palavras do texto", qtd_palavras_texto)
print (palavras)

hapax_legomana = numerodehapaxes / qtd_palavras_texto

print ("razao hapax:", round(hapax_legomana,2))