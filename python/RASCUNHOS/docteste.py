# -*- coding: utf-8 -*-
import re
import nltk
# from featx import bag_of_words 

teste = ['hoje',' amanha']
frase = ['Era uma vez hoje ainda']


texto = ''.join(frase)
texto = texto.lower()
# remove espaços, linhas e símbolos de pontuação
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")
# 
#remove acentos e cedilha
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")

for i in teste:
        if i in texto:
            variavel = i 
            print variavel 

