#!/usr/bin/python3
# -*- coding: utf-8 -*-
# informacoes de encoding
# importações de bibliotecas
from dao.processamento import Processamento as pro
from pickle import load
from pickle import dump
import nltk
import funcoes as func

import re
# importar matpotlib para desenhar
import numpy as np
# import matplotlib.pyplot as plt
from nltk import bigrams
import nltk
import nltk.corpus

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()


def processar(texto, id_pessoa, id_texto):

    tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
    tokens = nltk.word_tokenize(texto)
    unigram_tagger = nltk.tag.UnigramTagger(tagged_sents)
    variavel = unigram_tagger.tag(tokens)
    word_frequencies = nltk.FreqDist(tokens)

    print("RESULTADO PARA INTEGRAÇÃO:")
    preposicoes = list(filter(lambda x: x[1] == 'PREP', variavel))
    print("preposições:")
    print(preposicoes)

    palavras_denotativas = list(filter(lambda x: x[1] == 'PDEN', variavel))
    print("palavras denotativas:")
    print(palavras_denotativas)

    conjuncoes_subordinativas = list(filter(lambda x: x[1] == 'KS', variavel))
    print("conjunções subordinativas:")
    print(conjuncoes_subordinativas)

    conjuncoes_coordenativas = list(filter(lambda x: x[1] == 'KC', variavel))
    print("conjunções coordenativas:")
    print(conjuncoes_coordenativas)

    print("------------------------------")

    print("RESULTADO PARA AGENTIVIDADE:")


    # procurando -DOR
    print("Ocorrências de palavras com sufixo - DOR:")
    print(re.findall(r'\b(\w+dor)\b', texto))

    # procurando - NTE
    print("Ocorrências de palavras com sufixo - NTE")
    print(re.findall(r'\b(\w+nte)\b', texto))

    nomes_proprios = list(filter(lambda x: x[1] == 'NPROP', variavel))
    print("Nomes próprios:")
    print(nomes_proprios)

    pronomes_subs = list(filter(lambda x: x[1] == 'PROSUB', variavel))
    print("Pronomes substantivos:")
    print(pronomes_subs)

    pronomes_pessoais = list(filter(lambda x: x[1] == 'PROPESS', variavel))
    print("Pronomes pessoais:")
    print(pronomes_pessoais)

    print("------------------------------")

    print("------------------------------")

    print("RESULTADO PARA ORGANIZAÇÃO TEMPORAL:")

    # procurar verbos

    ver = list(filter(lambda x: x[1] == 'V', variavel))
    print("verbos:")
    print(ver)

    # adverbios de tempo
    # print("Advérbios de tempo")
    print("Advérbios:")
    advt = ['cedo', 'tarde', 'ontem', 'hoje', 'amanha', 'antes',
           'agora', 'depois', 'entao', 'ainda', 'sempre', 'nunca']
    for i in advt:
        if i in texto:
            adverbiosdetempo = i
            print("Advérbios de tempo:", i)

   
    print("------------------------------")

    print("RESULTADO PARA CAUSALIDADE:")

    print("Conjunções causais:")
    conjuncoes_causais = ['porque', 'entao', 'por isso', 'como se tivesse', 'por ter',
                          '^pois', 'portanto', 'visto que', 'visto como', 'ja que', 'uma vez que', 'desde que']
    for i in conjuncoes_causais:
        if i in texto:
            conjuncoescausais = i
            print("Conjunções causais:", i)
       
    
    #tentando procurar palavras terminadas em -DOR
    for w in texto:
        if w.endswith('dor'):
            print ("procurando a palavra terminada em -DOR",w)
        
  

    print("Outros dados para análise:")

    adjetivos = list(filter(lambda x: x[1] == 'ADJ', variavel))
    print("Adjetivos:")
    print(adjetivos)

    adverbio_conectivo_subordinativo = list(filter(
        lambda x: x[1] == 'ADV-KS', variavel))
    print("Advérbios conectivos subordinativos:")
    print(adverbio_conectivo_subordinativo)

    adverbio_relativo_subordinativo = list(filter(
        lambda x: x[1] == 'ADV-KS-REL', variavel))
    print("Advérbios relativos subordinativos:")
    print(adverbio_relativo_subordinativo)

    artigo = list(filter(lambda x: x[1] == 'ARTIGO', variavel))
    print("Advérbios relativos subordinativos:")
    print(adverbio_relativo_subordinativo)

    interjei = list(filter(lambda x: x[1] == 'IN', variavel))
    print("Interjeições:")
    print(interjei)

    num = list(filter(lambda x: x[1] == 'NUM', variavel))
    print("Numerais:")
    print(num)

    participio = list(filter(lambda x: x[1] == 'PCP', variavel))
    print("Particípios:")
    print(participio)

    
    p_adj = list(filter(lambda x: x[1] == 'PROADJ', variavel))
    print("Pronomes adjetivos:")
    print(p_adj)

    p_c_s = list(filter(lambda x: x[1] == 'PRO-KS', variavel))
    print("Pronomes conectivos subordinativos:")
    print(p_adj)

    p_c_s = list(filter(lambda x: x[1] == 'PRO-KS-REL', variavel))
    print("Pronomes relativos conectivos subordinativos:")
    print(p_adj)

    estrangeirismos = list(filter(lambda x: x[1] == 'EST', variavel))
    print("Estrangeirismos:")
    print(estrangeirismos)

    contras_e_enclises = list(filter(lambda x: x[1] == '|+', variavel))
    print("Contrações e ênclises:")
    print(contras_e_enclises)

    mesoclises = list(filter(lambda x: x[1] == '|!', variavel))
    print("Mesóclises:")
    print(mesoclises)

    ver_aux = list(filter(lambda x: x[1] == 'VAUX', variavel))
    print("verbos auxiliares:")
    print(ver_aux)

    
    # tentando encontrar sujeitos dos verbos
    print("Tentei encontrar sujeitos:")
    finder2 = BigramCollocationFinder.from_words(
        wrd for (wrd, tags) in variavel if tags in('NPROP', 'V'))
    scored = finder2.score_ngrams(bigram_measures.raw_freq)
    print(sorted(finder2.nbest(bigram_measures.raw_freq, 2)))

    finder3 = BigramCollocationFinder.from_words(
        wrd for (wrd, tags) in variavel if tags in('PROPESS', 'V'))
    scored3 = finder3.score_ngrams(bigram_measures.raw_freq)
    print(sorted(finder3.nbest(bigram_measures.raw_freq, 1)))

    finder4 = BigramCollocationFinder.from_words(
        wrd for (wrd, tags) in variavel if tags in('PROPESS', 'V'))
    scored4 = finder4.score_ngrams(bigram_measures.raw_freq)
    print(sorted(finder4.nbest(bigram_measures.raw_freq, 1)))

    finder5 = TrigramCollocationFinder.from_words(
        wrd for (wrd, tags) in variavel if tags in('PCP', 'PREP', 'N'))
    scored5 = finder5.score_ngrams(trigram_measures.raw_freq)
    print(sorted(finder5.nbest(trigram_measures.raw_freq, 1)))

    