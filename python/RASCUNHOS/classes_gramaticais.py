#!/usr/bin/python3
# -*- coding: utf-8 -*-
#informacoes de encoding
#importações de bibliotecas
import nltk
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

#nltk.download("mac_morpho")
#nltk.download("punkt")
#from nltk.corpus import mac_morpho
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#inicio - setando o texto
tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
texto = 'A Eva viu o Romeu e a Elena comeu o ossinho pois estava cansada. O astronauta foi pra lua depois eles comeram pipoca. O poema foi recitado pelo poeta.'
tokens = nltk.word_tokenize(texto)
unigram_tagger = nltk.tag.UnigramTagger(tagged_sents)
variavel = unigram_tagger.tag(tokens)
word_frequencies = nltk.FreqDist(tokens)
# ANÁLISE MORFOLÓGICA DO TEXTO
print ("ANÁLISE MORFOLÓGICA DO TEXTO:")
print unigram_tagger.tag(tokens)

print ("-------------------------------------")

print ("RESULTADO PARA INTEGRAÇÃO:")
preposicoes = filter(lambda x:x[1]=='PREP',variavel)
print ("preposições:") 
print preposicoes

palavras_denotativas = filter(lambda x:x[1]=='PDEN',variavel)
print ("palavras denotativas:")
print palavras_denotativas

conjuncoes_subordinativas = filter(lambda x:x[1]=='KS',variavel)
print ("conjunções subordinativas:")
print conjuncoes_subordinativas

conjuncoes_coordenativas = filter(lambda x:x[1]=='KC',variavel)
print ("conjunções coordenativas:")
print conjuncoes_coordenativas


print ("------------------------------")

print ("RESULTADO PARA AGENTIVIDADE:")
#procurando -DOR
print ("Ocorrências de palavras com sufixo - DOR:")
print re.findall(r'\b(\w+dor)\b',texto)

#procurando - NTE
print ("Ocorrências de palavras com sufixo - NTE")
print re.findall(r'\b(\w+nte)\b',texto)

nomes_proprios = filter(lambda x:x[1]=='NPROP',variavel)
print ("Nomes próprios:")
print nomes_proprios

pronomes_subs = filter(lambda x:x[1]=='PROSUB',variavel)
print ("Pronomes substantivos:")
print pronomes_subs

pronomes_pessoais = filter(lambda x:x[1]=='PROPESS',variavel)
print ("Pronomes pessoais:")
print pronomes_pessoais

#buscando entidades
tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
t0 = nltk.DefaultTagger('N')
t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)
from pickle import dump
output = open('mac_morpho.pkl', 'wb')
dump(t3, output, -1)
output.close()
from pickle import load
input = open('mac_morpho.pkl', 'rb')
tagger = load(input)
input.close()
tokens = nltk.word_tokenize(texto)
tagged = tagger.tag(tokens)
gramatica = r"""NE: {<NPROP>+}"""
analiseGramatical = nltk.RegexpParser(gramatica)
resposta=analiseGramatical.parse(tagged)
print ("Indícios de entidades:")
print resposta



print ("------------------------------")





print ("------------------------------")





print ("RESULTADO PARA ORGANIZAÇÃO TEMPORAL:")

#procurar verbos

ver = filter(lambda x:x[1]=='V',variavel)
print ("verbos:") 
print ver




#adverbios de tempo
# print("Advérbios de tempo")
print ("Advérbios:")
advt = ['cedo','tarde','ontem','hoje','amanha','antes','agora','depois','entao','ainda','sempre','nunca']
for i in advt:
        if i in texto:
            adverbiosdetempo = i 
            print ("Advérbios de tempo:", i) 




# advteste = filter(lambda x:x[1]=='ADV',variavel)
# #procurar advérbios de tempo#
# advs_e_conectivos_tempo = ['hoje', 'logo', 'enquanto' 'ontem', 'tarde', 'outrora', 'amanha', 'cedo', 'depois', 'ainda']

# teste_adv = ''.join(advs_e_conectivos_tempo)
# for i in texto:
#     if teste_adv in texto:
#         print ("Ocorrência de advérbios de tempo", i)

# for i in advs_e_conectivos_tempo:
#     if i in texto:
#         print ("OCORRÊNCIA DE ADVÉRBIOS E/OU CONECTIVOS COM NOÇÃO SEMÂNTICA DE TEMPO: - ENCONTRADA")
#     else:
#         print ("OCORRÊNCIA DE ADVÉRBIOS E/OU CONECTIVOS COM NOÇÃO SEMÂNTICA DE TEMPO - NÃO ENCONTRADA")












print ("------------------------------")


print ("RESULTADO PARA CAUSALIDADE:")

print ("Conjunções causais:")
conjuncoes_causais= ['porque', 'entao', 'por isso', 'como se tivesse', 'por ter', '^pois', 'portanto', 'visto que', 'visto como', 'ja que', 'uma vez que', 'desde que']
for i in conjuncoes_causais:
        if i in texto:
            conjuncoescausais = i 
            print ("Conjunções causais:", i) 
        else:
            print ("Conjunções causais: \n []")



#numero de caracteres
# print len (texto)

# #tentando procurar palavras terminadas em -DOR
# [w for w in texto if w.endswith('dor')]
# print ("procurando a palavra terminada em -DOR",w)  

# print ("Verificando dados de frequencia de palavras")
# fd = nltk.FreqDist(texto)
# print fd

#generate a chart of the 50 most frequent words
#print fd.plot(50,cumulative=False)

#procurando verbos

# text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
# pos_tagged = nltk.pos_tag(text)
# print pos_tagged
# nouns = filter(lambda x:x[1]=='NN',pos_tagged)
# print ("verbos:") 
# print nouns


#Outros dados

print("Outros dados para análise:")

adjetivos = filter(lambda x:x[1]=='ADJ',variavel)
print ("Adjetivos:")
print adjetivos

adverbio_conectivo_subordinativo = filter(lambda x:x[1]=='ADV-KS',variavel)
print ("Advérbios conectivos subordinativos:")
print adverbio_conectivo_subordinativo

adverbio_relativo_subordinativo = filter(lambda x:x[1]=='ADV-KS-REL',variavel)
print ("Advérbios relativos subordinativos:")
print adverbio_relativo_subordinativo

artigo= filter(lambda x:x[1]=='ARTIGO',variavel)
print ("Advérbios relativos subordinativos:")
print adverbio_relativo_subordinativo

interjei= filter(lambda x:x[1]=='IN',variavel)
print ("Interjeições:")
print interjei

num = filter(lambda x:x[1]=='NUM',variavel)
print ("Numerais:")
print num 

participio = filter(lambda x:x[1]=='PCP',variavel)
print ("Particípios:")
print participio

# palavra_denotativa = filter(lambda x:x[1]=='PDEN',variavel)
# print ("Palavras denotativas:")
# print palavra_denotativa


p_adj = filter(lambda x:x[1]=='PROADJ',variavel)
print ("Pronomes adjetivos:")
print p_adj

p_c_s = filter(lambda x:x[1]=='PRO-KS',variavel)
print ("Pronomes conectivos subordinativos:")
print p_adj

p_c_s = filter(lambda x:x[1]=='PRO-KS-REL',variavel)
print ("Pronomes relativos conectivos subordinativos:")
print p_adj

estrangeirismos = filter(lambda x:x[1]=='EST',variavel)
print ("Estrangeirismos:")
print estrangeirismos


contras_e_enclises = filter(lambda x:x[1]=='|+',variavel)
print ("Contrações e ênclises:")
print contras_e_enclises


mesoclises = filter(lambda x:x[1]=='|!',variavel)
print ("Mesóclises:")
print mesoclises
 


ver_aux = filter(lambda x:x[1]=='VAUX',variavel)
print ("verbos auxiliares:") 
print ver_aux

# #tentando plotar um grafico
# classes = ['verbos', 'advérbios', 'substantivos', 'adjetivos', 'preposições', 'conjunções']
# valores []

#TentandoContar

#print word_frequencies
#word_frequencies.plot(30,cumulative=False)


#tentando encontrar sujeitos dos verbos
print ("Tentei encontrar sujeitos:")
finder2 = BigramCollocationFinder.from_words(wrd for (wrd,tags) in variavel if tags in('NPROP','V'))
scored = finder2.score_ngrams(bigram_measures.raw_freq)
print sorted(finder2.nbest(bigram_measures.raw_freq, 2))

finder3 = BigramCollocationFinder.from_words(wrd for (wrd,tags) in variavel if tags in('PROPESS','V'))
scored3 = finder3.score_ngrams(bigram_measures.raw_freq)
print sorted(finder3.nbest(bigram_measures.raw_freq, 1))

finder4 = BigramCollocationFinder.from_words(wrd for (wrd,tags) in variavel if tags in('PROPESS','V'))
scored4 = finder4.score_ngrams(bigram_measures.raw_freq)
print sorted(finder4.nbest(bigram_measures.raw_freq, 1))

finder5 = TrigramCollocationFinder.from_words(wrd for (wrd,tags) in variavel if tags in('PCP','PREP','N'))
scored5 = finder5.score_ngrams(trigram_measures.raw_freq)
print sorted(finder5.nbest(trigram_measures.raw_freq, 1))


# print finder2 

# for (w1,t1), (w2,t2) in nltk.bigrams(tokens):
#     if (t1.startswith('PROPESS') and t2.startswith('V')):
#         print w1, w2


# for (w1,t1), (w2,t2) in nltk.bigrams(variavel):
#     print [(word, tag) for word, tag in variavel if tag in ('PROPESS', 'V')]

# for (w1,t1), (w2,t2) in nltk.bigrams(variavel):
#     print [(word, tag) for word, tag in variavel if tag in ('NPROP', 'V')]


# for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(variavel):
#     print [(word, tag) for word, tag in variavel if tag in ('PCP', 'PREP', 'N')]