#!/usr/bin/python3
# -*- coding: utf-8 -*-
import nltk 
import re
import funcoes as func
from dao.textos import Textos as textos
from dao.objeto import Objeto as objetos
from dao.transporte import Transporte as transp
from dao.jogador import Jogador 
import funcoes

def teste_de_adaptacao(textodoestudante,transporte):
    contagem = textodoestudante.count(transporte)
    # print ("contagem:", contagem)
    # contagem +=round(func.get_jaccard_sim(transporte,textodoestudante))
    if contagem == 0:
        pontos = 0
    else:
        if contagem == 1:
            pontos = 25
        else:
            pontos = 50
    
    return pontos


def flexibilidade_espontanea_semantica(respostadoestudante):
    quantidade_de_respostas = len(respostadoestudante.split())
   
    if quantidade_de_respostas <=2:
        pontos2 = 0
    else:
        pontos2 = 25
        if quantidade_de_respostas >6:
            pontos2 = 50
    ##print ("Pontuação no teste de flexibilidade espontanea semantica:", pontos2)
    return pontos2

def resultado_flexibilidade(pontos,pontos2):
    resultado = pontos+pontos2
    # print("total de pontos: ", resultado)
    if resultado == 0:
        resultado_final = "rigidez"
    else:
        resultado_final = "potencial flexibilidade"
        if resultado >75:
            resultado_final = "flexível"
    ##print ("Resultado final:", resultado_final)
    return resultado_final
    

def processamento(id_pessoa):
    
    # print (resultado_flexibilidade())

    tx = textos()
    texto = tx.busca_processamento(id_pessoa,"2")  
    if(texto==None):
        print("deu m ",id_pessoa)    
    texto=texto[0].texto_narrativa
    #texto=texto.lower()

    obj=objetos()
    resposta = obj.getobjeto(id_pessoa)
    if(resposta==None):
        print("deu m ",id_pessoa)   
    resposta=resposta[0].serventiaobjeto
    
    trsp=transp()
    transporte = trsp.getTransporte(id_pessoa) 
    if(transporte==None):
        print("deu m ",id_pessoa)
    transporte=transporte[0].historia_transp

            
    lista=['sei lá','nao sei','n sei','sla']
    resposta1 =teste_de_adaptacao(texto,transporte)
    if(func.get_jaccard_sim(lista,resposta)==0):
        resposta2 = flexibilidade_espontanea_semantica(resposta)
    else:
        resposta2 = 0
    jog =Jogador()
    jog.id_pessoa=id_pessoa
    texto_final="flexibilidade_espontanea_semantica "+str(resposta2)+" teste_de_adaptacao "+str(resposta1)
    texto_final+=" total é "+resultado_flexibilidade(resposta1,resposta2)
    jog.flexibilidade=texto_final
    jog.adaptacao = resposta1
    jog.cadFlexibilidade()



