# -*- coding: utf-8 -*-

from collections import Counter
texto = 'A Rainha tinha um espelho magico, raquel para o qual ela perguntava frequentemente, olhando para si mesma: raquel “Espelho, espelho meu, existe alguem mais bonita do que eu?” raquel E o espelho sempre respondia a mesma coisa: “Nao, ninguem e mais linda do que minha Rainha.”'
texto = texto.lower() #converte para minúsculas 

#remove espaços, linhas e símbolos de pontuação
# texto = texto.replace(" ","")
# texto = texto.replace("\n","")
# texto = texto.replace(".","")
# texto = texto.replace("!","")
# texto = texto.replace("?","")
# texto = texto.replace(",","")
# texto = texto.replace(";","")

# #remove acentos e cedilha
# texto = texto.replace("á","a")
# texto = texto.replace("à","a")
# texto = texto.replace("ã","a")
# texto = texto.replace("é","e")
# texto = texto.replace("ê","e")
# texto = texto.replace("í","i")
# texto = texto.replace("ó","o")
# texto = texto.replace("ô","o")
# texto = texto.replace("ú","u")
# texto = texto.replace("ç","c")


num_caracteres = 0
num_palavras = 0
num_linhas = 0

vogais = 0
consoantes = 0

for caracter in texto:
    if caracter in 'aeiou':
        vogais = vogais + 1
    else: 
        consoantes = consoantes + 1

print "Vogais: %d" %vogais
print "Consoantes: %d" %consoantes
print "Total de letras: %d - %d" %(len(texto), (vogais+consoantes)) 
total_linhas = len(texto.splitlines())
total_caracteres = len(texto)
total_palavras = len(texto.split())
print ("numero de palavras:" + str(total_palavras))
print ("Numero de linhas em texto:" + str(total_linhas))
print ("Total de caracteres:" + str(total_caracteres))
print ("-----------------")
print texto.split(' ')

print ("-----------------")
print ("FREQUÊNCIA DE PALAVRAS:")
palavras = texto.replace('\n',' ').replace('\t','').split(' ')
contador = Counter(palavras)
for i in contador.items():
    print i

    