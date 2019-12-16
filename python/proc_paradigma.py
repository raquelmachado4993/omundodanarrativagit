#!/usr/bin/python3
# -*- coding: utf-8 -*-
from dao.acoes import Acoes
import funcoes as fun
import funcoes_busca_egocentrico as egocentrico
import funcoes_busca_intermediario as intermediario
import funcoes_busca_socializado as socializado
from   dao.paradigma import Paradigma


def analiseparadigma_fases(id_pessoa):
    aco = Acoes()
    c =aco.busca_paradigma(id_pessoa)
    resultado=""
    
    if c[0].acao == 'escolheu ir para o fasepersonagem':
        resultado = 'personagem'

    if c[0].acao == 'escolheu ir para o fasecenarios':
        resultado = 'cenario'     

    if c[0].acao == 'escolheu ir para o faseobjeto':
        resultado = 'objeto'
        
    if c[0].acao == 'escolheu ir para o fasemissao':
        resultado = 'missao'
        
    if c[0].acao == 'escolheu ir para o fasetransporte':
        resultado = 'transporte'
    
    if(resultado==""):
        return "Null"
    return resultado
    
    
def analiseParadigma (id_pessoa,texto,id_narrativa):    
    if(texto!=""):
        #texto=texto.lower()
        paradigma = Paradigma()
        
        paradigma.cod_tx=id_narrativa
        paradigma.id_pessoa=id_pessoa
        
        r,c = egocentrico.proc_ego(texto)
        paradigma.egocentrico_palavras=r
        paradigma.egocentrico_qtds=c
        
        
        r,c = intermediario.proc_inter(texto)
        paradigma.intermediario_palavras=r
        paradigma.intermediario_qtds=c
        
        r,c = socializado.proc_soci(texto)
        paradigma.socializado_palavras=r
        paradigma.socializado_qtds=c
        
        paradigma.paradigma = analiseparadigma_fases(id_pessoa)
        
        if(paradigma.paradigma=="Null"):
            paradigma.imagem="Null"
        else:       
            paradigma.imagem="./img_paradigma/"+str(paradigma.paradigma)+".png"
        
        
        paradigma.cadParadigma()
             