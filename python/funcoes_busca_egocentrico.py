#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import funcoes as fun

def verifica_eu(texto):
    result=""
    contador=0
    substring1 = "eu"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


def verifica_amav(texto):
    result=""
    contador=0
    substring = 'amav'
    if substring in texto:
        result+=substring+" "
        contador+=1    
    return result,contador

def verifica_e_foram_felizes_para_sempre(texto):
    result=""
    contador=0
    substring1 = "e foram felizes para sempre"  
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador 


def verifica_e_foram_felizes_pra_sempre(texto):
    result=""
    contador=0
    substring1 = "e foram felizes pra sempre"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


#def verifica_felizes(verifica_e_foram_felizes_para_sempre, verifica_e_foram_felizes_pra_sempre):
#    result=""
#    contador=0
#    if verifica_e_foram_felizes_para_sempre or verifica_e_foram_felizes_pra_sempre == 'achou':
#        print ("Sentido de 'Felizes para sempre' - ENCONTRADO")
#    else:
#        print ("Sentido de 'Felizes para sempre' - NÃO ENCONTRADO") 
#    return


def verifica_sentido_casar (texto):
    result=""
    contador=0
    substring1 = "casaram"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


def verifica_sentido_namoro_namorar(texto):
    result=""
    contador=0
    substring = "namor"
    if substring in texto:
        result+=substring+" "
        contador+=1    
    return result,contador

def verifica_sentido_castigo_castigar(texto):
    result=""
    contador=0
    substring = "castig"
    if substring in texto:
        result+=substring+" "
        contador+=1    
    return result,contador 


def verifica_papai_do_ceu(texto):
    result=""
    contador=0
    substring1 = "papai do céu"  
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador 

def verifica_papai_noel(texto):
    result=""
    contador=0
    substring1 = "papai noel"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


def verifica_anjo_da_guarda(texto):
    result=""
    contador=0
    substring1 = "anjo da guarda"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


def busca_familia(texto):
    result=""
    contador=0
    palavras_crivo_familia = ['pai','mae', 'avo', 'avo', 'bisavo', 'tataravo', 'primo', 'prima', 'tio', 'tia', 'irmao','irma', 'filho', 'filha', 'sobrinho', 'sobrinha', 'afilhado', 'afilhada','cunhado', 'cunhada', 'sogro', 'sogra', 'meia-irma', 'meio-irmao', 'enteado', 'enteada', 'vovo', 'vovo', 'papai', 'mamae', 'vovo bisa', 'vovo bisa', 'madrasta', 'padrasto', 'tio-avô', 'tia-avô', 'marido', 'esposa', 'esposo']
    for i in palavras_crivo_familia:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 

    


def proc_ego(texto):
    result=""
    contador=0
    texto = fun.converter(texto)
    
    #verifica_felizes (verifica_e_foram_felizes_para_sempre, verifica_e_foram_felizes_pra_sempre)

    
    r,c = verifica_amav(texto)
    result+=r
    contador+=c
        
    r,c = verifica_sentido_casar (texto)
    result+=r
    contador+=c
    
    r,c = verifica_sentido_castigo_castigar(texto)
    result+=r
    contador+=c
    
    r,c = verifica_sentido_namoro_namorar(texto)
    result+=r
    contador+=c
    
    r,c = verifica_papai_do_ceu(texto)
    result+=r
    contador+=c
    
    r,c = verifica_papai_noel(texto)
    result+=r
    contador+=c
    
    r,c = verifica_anjo_da_guarda(texto)
    result+=r
    contador+=c
    
    r,c =busca_familia(texto)
    result+=r
    contador+=c
    
    
    return result,contador