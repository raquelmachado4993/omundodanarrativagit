#!/usr/bin/python3
# -*- coding: utf-8 -*-
#informacoes de encoding
#importações de bibliotecas
import nltk
import  funcoes as func 

import re
#importar matpotlib para desenhar
import numpy as np
#import matplotlib.pyplot as plt
from nltk import bigrams
import nltk
import nltk.corpus

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
#instalações realizadas

from dao.processamento import Processamento as pro

def processar(texto, id_pessoa, id_texto):

    #inicio - setando o texto
    tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
    tokens = nltk.word_tokenize(texto)
    unigram_tagger = nltk.tag.UnigramTagger(tagged_sents)
    variavel = unigram_tagger.tag(tokens)
    word_frequencies = nltk.FreqDist(tokens)
    # ANÁLISE MORFOLÓGICA DO TEXTO
    print ()
    txtInsert='['  
    for variavel2 in unigram_tagger.tag(tokens):
        
        if(txtInsert!='['):
            txtInsert+=','  
        
        termo =  variavel2[0]
        termo = termo.replace("'", "´")
        
        classificacao = func.convMM(str(variavel2[1]))
        classificacao = classificacao.replace("'", "´")

        txtInsert += '{"TERMO ":"' +termo+'","CLASSIFICACAO ":"'+classificacao+'"}'
    
    txtInsert+=']'
    p = pro(str(id_pessoa), 'ANÁLISE MORFOLÓGICA DO TEXTO', txtInsert, str(id_texto))
    p.inserir()
