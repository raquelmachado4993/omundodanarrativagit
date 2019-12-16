#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def converter(texto):
    
    if(texto=='' or texto==None or texto==str):
        return ""
    # texto = (re.sub(r"[^a-zA-Z0-9]+", ' ', texto))
    # texto = re.sub('[^A-Za-z0-9]+', '', texto)
    # texto = str(texto.encode('utf-8'))
    # texto = unicode(texto).encode("utf-8")
    texto = ''.join(texto)
    texto = texto.lower()
    #texto = texto.replace(" ","")
    texto = texto.replace("\n","")
    texto = texto.replace(".","")
    texto = texto.replace("!","")
    texto = texto.replace("?","")
    texto = texto.replace(",","")
    texto = texto.replace(";","")
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

    return texto


def convMM(texto):

    texto = texto.replace("PRO-KSREL","PRONOME CONECTIVO SUBORDIN. RELATIVO")
    texto = texto.replace("ADV-KS-REL","ADVÉRBIO RELATIVO SUBORDINATIVO")
    texto = texto.replace("ADV-KS","ADVÉRBIO CONECTIVO SUBORDINATIVO")
    texto = texto.replace("PROPESS","PRONOME PESSOAL")
    texto = texto.replace("PROADJ","PRONOME ADJETIVO")
    texto = texto.replace("PROSUB","PRONOME SUBSTANTIVO")
    texto = texto.replace("PRO-KS","PRONOME CONECTIVO SUBORDINATIVO")
    texto = texto.replace("NPROP","NOME PROPRIO")
    texto = texto.replace("VAUX","VERBO AUXILIAR")
    texto = texto.replace("PREP","PREPOSICAO")
    texto = texto.replace("PDEN","PALAVRA DENOTATIVA")
    texto = texto.replace("ART","ARTIGO")
    texto = texto.replace("NUM","NUMERAL")
    texto = texto.replace("PCP","PARTICIPIO")    
    texto = texto.replace("CUR","SIMBOLO DE MOEDA CORRENTE ")
    texto = texto.replace("ADV","ADVERBIO")
    texto = texto.replace("IN","INTERJEICAO")
    texto = texto.replace("KC","CONJUNCAO COORDENATIVA")
    texto = texto.replace("None","SEM CLASSIFICACAO")
    texto = texto.replace("N","NOME")
    texto = texto.replace("V","VERBO")
    
    return texto


def get_jaccard_sim(lista_similaridade,resposta_aluno):
    lista = lista_similaridade
    if(lista_similaridade=="" or lista_similaridade==None):
        return -1
    if(resposta_aluno=="" or resposta_aluno==None):
        return -1
    a = set(resposta_aluno.split()) 
    for palavra in lista:
        #palavra=palavra.lower()
        b = set(palavra.split())
        c = a.intersection(b)
        resultado = float(len(c)) / (len(a) + len(b) - len(c))
        #print (resultado)
        if resultado !=0:
            return resultado
    return 0


## lista=['a vaca desceu' ,'a vaca pousou' ,'a vaca pousou no chao' ,'a vaca foi morta' ,'porque ela quis' ,'a vaca caiu' ,'nao sei' ,'morreu' ,'caiu' ,'se machucou' ,'se arrebentou toda' ,'se ferrou' ,'se deu mal']
## print(get_jaccard_sim(lista,"a raquel morreu a vaca"))


## print(get_jaccard_sim("onibus","""Anna Luiza estava num beco andando ate que ela ver uma Ônibus... um Ônibus diferente, ela decidiu entrar (narradora:-uma péssima ideia mas tudo bem)   ela entro e tinha uma menina machucada e chorando muito e amarada... Anna Luiza ficou assutada e não pensou duas vezes... e ajudou a menina a sair dali Anna Luiza perguntou por que ela estava naquele estado,ela disse que um cara com uma mascara,a mascara de um palhaço... ela disse que na casa dele onde ele me bateu,tinha fotos de outras meninas machucadas, e outras fotos as as meninas não macucadas sabe?1 como se fosse as próximas vitimas... perguntei a ela se ela sabia onde ele estava,ela disse que ele estava com malas do lado da cama,sai correndo para o aeroporto quando chequei la,eu vi uma cara de óculos  escuro... sai correndo atras dele quando ele percebeu ele correu também...ate que ele fugiu
##                                                                        ~QUEBRA DE TEMPO~
##      Anos se passaram e eu não encontrei a peste... a noticias não paravam falando,de mulheres sendo espancadas e largadas em Ônibus... ate que um dia eu entendi a rota dele ele ia voltar para cá.... me preparei e treinei fui a floresta e vi uma casa bem velha,entrei na casa e vi uma mago pedi ajuda dele e ele disse:-acada passo que você da,uma porta no universo se abre (narradora:sei lá tô sem criatividade.) eu não entendi nada... ele me deu uma chave essa chave abria portas para outro mundo,perguntei como isso poderia me ajudar ele disse eu ira saber..... 
##                                                                        ~QUEBRA DE TEMPO~
##     Eu finalmente encontrei ele, estava eu e ele cara a cara,eu tava doida para da uns murro na cara dele.... ai eu lembrei do que o mago disse a cada passo que eu do,uma porta no universo se abre,fui andando ate ele ate,e ele ate mim... eu coloquei a mão no meu bolço,e peguei a chave,e disse o que o mago disse,"acada passo que você dar,uma porta no universo se abre" e encostei a chave no peito dele... ele sumiu todos disseram.
##                                                                     ~QUEBRA DE TEMPO~
## tudo voltou como era antes, tudo estava lindo e normal como sempre foi.
##                                                                             FIM!!
## """))
