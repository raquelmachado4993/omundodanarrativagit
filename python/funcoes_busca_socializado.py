#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import funcoes as fun

def busca_social(texto):
    result=""
    contador=0
    palavras_crivo_social = ['soc', 'sócio-', 'sociedade']
    for i in palavras_crivo_social:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 



def busca_cultural(texto):
    result=""
    contador=0
    palavras_crivo_cultural = ['cultural', 'cultura', 'culto', 'cult']
    for i in palavras_crivo_cultural:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 


def busca_responsabilidade_social(texto):
    result=""
    contador=0
    palavras_crivo_responsabilidade_social = ['caridade', 'solidariedade', 'voluntario', 'voluntariado', 'ecologia', 'ecossistema', 'reciclagem', 'economia']
    for i in palavras_crivo_responsabilidade_social:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 



def busca_critica(texto):
    result=""
    contador=0
    palavras_crivo_critica = ['critica', 'julgar','julgamento']
    for i in palavras_crivo_critica:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 

def busca_profissoes(texto):
    result=""
    contador=0
    profissoes = ['medico', 'trabalhar', 'trabalho', 'enfermeiro', 'advogado', 'youtuber','escritor', 'bibliotecario', 'programador', 'webdesigner', 'agricultor', 'defensor', 'procurador', 'gerente', 'delegado', 'policial', 'engenheiro', 'hacker', 'piloto', 'tecnico', 'analista', 'psicologo', 'farmaceutico', 'fisioterapeuta', 'professor', 'cientista', 'nutricionista', 'vendedor', 'cozinheiro', 'faxineiro', 'inspetor', 'zelador', 'porteiro', 'musico', 'estilista', 'secretaria', 'apresentador', 'açougueiro', 'operador de telemarketing', 'padeiro', 'vidraceiro', 'motorista']
    for i in profissoes:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 

def busca_religioes(texto):
    result=""
    contador=0
    religioes = ['catolicismo','catolic', 'nestorianismo', 'judaismo', 'jude', 'samaritano', 'mashichismo', 'sunismo', 'xiismo', 'carijismo', 'sufismo', 'ibadismo', 'islamismo', 'atonismo', 'espiritismo', 'espirita', 'seicho-no-ie', 'xintoísmo', 'santeria', 'vodu', 'candomble', 'tambor de mina', 'xangô do nordeste', 'umbanda', 'quimbanda', 'helenismo', 'wicca', 'xamanismo', 'odinismo', 'druidismo', 'kemetismo', 'asatru', 'satanismo', 'ocultismo', 'budismo', 'taoísmo', 'budismo tibetano', 'nova era', 'cristianismo esoterico', 'santo daime', 'ayyavazhi', 'cheondoismo', 'anglicionismo']
    for i in religioes:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador 






def proc_soci(texto):
    result=""
    contador=0
            
    r,c =    busca_social(texto)
    result+=r
    contador+=c
        
    r,c =    busca_critica(texto)
    result+=r
    contador+=c
        
    r,c =    busca_cultural(texto)
    result+=r
    contador+=c
        
    r,c =    busca_profissoes(texto)
    result+=r
    contador+=c
        
    r,c =    busca_responsabilidade_social(texto)
    result+=r
    contador+=c
        
    r,c =    busca_profissoes(texto)
    result+=r
    contador+=c
        
    r,c =    busca_religioes(texto)
    result+=r
    contador+=c

    return result,contador