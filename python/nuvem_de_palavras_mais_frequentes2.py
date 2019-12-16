#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk 
from nltk.draw.dispersion import dispersion_plot
import re
import matplotlib.pyplot as plt
import funcoes as fun
from nltk.probability import FreqDist
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
pos = {}
texto = "Era uma vez um lugarzinho no meio do nada texto testa teste comida comida mãe mãe tudo Era uma vez uma menina bitcoins menina Era uma vez um grafo com bitcoins"
texto = fun.converter(texto)
from string import punctuation
palavras = word_tokenize(texto.lower())
stopwords = set(stopwords.words('portuguese') + list(punctuation))

palavras_sem_stopwords = nltk.FreqDist(palavra.lower() for palavra in palavras if palavra not in stopwords)  

palavras2 = ''
for index, palavra in palavras_sem_stopwords.most_common(10):
    palavras2+= index+' , '
    
   
print (palavras2)  
   

wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(palavras2)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('nuvem.png', dpi=100)
plt.show()

  

