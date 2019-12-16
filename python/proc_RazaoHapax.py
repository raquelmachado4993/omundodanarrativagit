#!/usr/bin/python3
# -*- coding: utf-8 -*-
import funcoes as fun
import nltk 
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from dao.razao_hapax import RazaoHapax

def proc_RHx(id_pessoa,id_texto, texto):
    pos = {}
    texto = fun.converter(texto)


    palavras = word_tokenize(texto.lower())
    fdist1 = FreqDist(palavras)
    qtd_palavras_texto = len(palavras)
    numerodehapaxes =  len((fdist1.hapaxes()))
    hapax_legomana = numerodehapaxes / qtd_palavras_texto
    razao_hapax=round(hapax_legomana,2)
    
    raz = RazaoHapax()
    raz.cod_tx=id_texto
    raz.hapax_legomana= razao_hapax
    raz.id_pessoa= id_pessoa
    raz.numerodehapaxes= numerodehapaxes
    raz.qtd_palavras_texto= qtd_palavras_texto
    raz.cadRazaoHapax()
    
    
    
    
    
    