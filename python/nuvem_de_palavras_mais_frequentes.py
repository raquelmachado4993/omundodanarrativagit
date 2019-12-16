#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk 
import re
import  funcoes as func 
from dao.nuvem_palavras import Nuvem_palavras as nuvem
from nltk.probability import FreqDist


from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from string import punctuation

# nltk.download('stopwords')

def np_mais_frequentes(texto, id_pessoa, id_texto):
    if(texto!=''):
        # print("texto "+str(texto))
        # print("\r\n")
        texto = func.converter(texto)
        from nltk.corpus import stopwords    
        palavras = word_tokenize(texto.lower())
        stopwords = set(stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = nltk.FreqDist(palavra.lower() for palavra in palavras if palavra not in stopwords)  

        palavras2 = ''
        for index, palavra in palavras_sem_stopwords.most_common(10):
            palavras2+= index+' , '

        # print (palavras2)  
        return (palavras2)


def salvaImg(id_pessoa,imagem,id_texto): 
    if(imagem!=''):
        if(imagem!= None ): 
            print("imagem "+str(imagem))
            # min_freq=3,max_words=50,
            imagem = WordCloud(max_font_size=100,width = 1520, height = 535 ).generate(imagem)
            plt.figure(figsize=(16,9))
            plt.imshow(imagem)

            plt.axis("off")
            # savefig('{}/graph.png'.format(output_dir))
            img ='./img_processamento/nuvem_pessoa_'+str(id_pessoa)+'.png' 
            plt.savefig(img, dpi=100)
            # plt.show()
            n=nuvem(id_pessoa, img ,id_texto)
            n.inserir()
            #plt.show()