#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import funcoes as fun

def verifica_escola(texto):
    result=""
    contador=0
    substring1 = "escola"
    if substring1 in texto:
        result+=substring1+" "
        contador+=1    
    return result,contador


def encontra_esportes(texto):
    result=""
    contador=0    
    pesquisar_esportes = ['futebol', 'volei', 'tênis de mesa', 'natação', 'futsal', 'capoeira', 'skate', 'skatismo', 'surf', 'vôlei de praia', 'badminton', 'frescobol', 'judô', 'atletismo', 'críquete', 'basquete', 'hockey na grama', 'hockey no gelo', 'beisebol', 'fórmula 1', 'Rugby', 'futebol americano', 'golfe', 'handebol', 'queimado', 'hipismo', 'ginástica olímpica', 'Triatlo', 'maratona', 'canoagem', 'peteca', 'jiu-jitsu', 'esgrima', 'vale-tudo', 'karatê', 'corrida', 'ciclismo', 'boxe', 'MMA', 'Taekwondo']
    # print(len(pesquisar_esportes))
    for i in pesquisar_esportes:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador


def busca_batalha_luta_guerra(texto):
    result=""
    contador=0
    palavras_crivo_intermediario = ['lut','guerr','batalha']
    # palavras_crivo_intermediario = ''.join(palavras_crivo_intermediario_inicio)
    # palavras_crivo_intermediario = palavras_crivo_intermediario_inicio.split()
    # palavras_crivo_intermediario_encontradas = []
    for i in palavras_crivo_intermediario:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador


def busca_amizade(texto):
    result=""
    contador=0
    palavras_crivo_amizade = ['amig', 'amiz', 'migux','amigos','amigas']
    for i in palavras_crivo_amizade:
        if i in texto:
            result+=i+" "
            contador+=1    
    return result,contador


def busca_jogo(texto):
    result=""
    contador=0
    substring = "jog"
    if substring in texto:
        result+=substring+" "
        contador+=1    
    return result,contador





def proc_inter(texto):
    result=""
    contador=0
    
        
    r,c =encontra_esportes(texto)
    result+=r
    contador+=c
        
    r,c =busca_batalha_luta_guerra(texto)
    result+=r
    contador+=c
        
    r,c =busca_amizade(texto)
    result+=r
    contador+=c
        
    r,c =busca_jogo(texto)
    result+=r
    contador+=c
            
    return result,contador