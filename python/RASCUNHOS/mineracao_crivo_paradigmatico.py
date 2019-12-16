# -*- coding: utf-8 -*-
import re

teste = [" era amigo natação UMA VEZ um lutar vôlei o rei papai do céu que vivia batalha num reino  distante,  com a sua filha pequena, que se chamava Branca de Neve. O rei, como se sentia só, voltou a casar, achando que também seria bom para a sua filha ter uma nova mãe. A nova rainha era uma mulher muito bela mas também muito má, e não gostava de Branca de Neve que, quanto mais crescia, mais bela se tornava. A rainha malvada tinha um espelho mágico, ao qual perguntava, todos os dias: - Espelho meu, espelho meu, haverá mulher mais bela do que eu? E o espelho respondia: - Não minha rainha, és tu a mulher mais bela! então eles casaram e foram felizes para sempre"]
texto = ''.join(teste)
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


def termos_crivo_egocentrico():
    palavras_crivo_egocentrico = ['namor', 'casar', 'casamento', 'foram felizes para sempre', 'teste', 'papai do ceu', 'papai noel', 'anjo da guarda', 'castig']
    palavras_crivo_egocentrico_encontradas = []
    for i in palavras_crivo_egocentrico:
        if i in texto:
            palavras_crivo_egocentrico_encontradas.append(i)
            quantidade_palavras_crivo_egocentrico_encontradas = len(palavras_crivo_egocentrico_encontradas)
            print ("crivo egocentrico")
            print palavras_crivo_egocentrico_encontradas
            print quantidade_palavras_crivo_egocentrico_encontradas

def termos_crivo_intermediario():
    palavras_crivo_intermediario = ['jog','lut','guerr','batalha','amig','amiz']
    # palavras_crivo_intermediario = ''.join(palavras_crivo_intermediario_inicio)
    # palavras_crivo_intermediario = palavras_crivo_intermediario_inicio.split()
    palavras_crivo_intermediario_encontradas = []
    for i in palavras_crivo_intermediario:
        if i in texto:
            palavras_crivo_intermediario_encontradas.append(i)
            quantidade_palavras_crivo_intermediario_encontradas = len(palavras_crivo_intermediario_encontradas)
            print ("crivo intermediario")
            print palavras_crivo_intermediario_encontradas
            print quantidade_palavras_crivo_intermediario_encontradas


termos_crivo_egocentrico()
termos_crivo_intermediario()