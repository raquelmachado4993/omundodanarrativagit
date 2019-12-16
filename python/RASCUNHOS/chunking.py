# coding=utf-8
import nltk
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
# sentences = nltk.sent_tokenize(texto)
# sentences = [nltk.word_tokenize(sent) for sent in sentences]
# sentences = [tagger.tag(sent) for sent in sentences]

texto = "O ministro Edson Fachin do Supremo Tribunal Federal determimou a separacao do inquerito contra o presidente Michel Temer da investigacao contra o senador afastado Aecio Neves."
tokens = nltk.word_tokenize(texto)
tagged = tagger.tag(tokens)
gramatica = r"""NE: {<NPROP>+}"""
analiseGramatical = nltk.RegexpParser(gramatica)
resposta=analiseGramatical.parse(tagged)
print resposta
print ("----------")
 


