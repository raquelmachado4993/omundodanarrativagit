#!/usr/bin/python3
# -*- coding: utf-8 -*-
import proc_morfologica as pro
import proc_sintagmatica as pro2
import  nuvem_de_palavras_mais_frequentes as npmf
import proc_originalidade  as porig
import proc_fluencia as fluencia
import proc_flexibilidade as flex
import proc_criativo as criativo
import proc_paradigma as paradigma

import eme 
import grafo 
import funcoes as fun
import jabuti
import proc_RazaoHapax as PRHX

from dao.pessoas import Pessoas as ps
from dao.textos import Textos 
from dao.acoes import Acoes as acoes


#print(myresult[0][1])
listaPessoas="39,36,13,39,20,11,19,15,24,7,16,9,6"
p = ps()
pessoas =p.busca("lista",listaPessoas)
for pessoa in pessoas:

        print(" texto da pessoa "+pessoa.login+"\r\n")
        tx2=''
        #print(pessoa.id_pessoa)
        
        ## processador de grafo 
        # grafo.processa_grafo(pessoa.id_pessoa,pessoa.Nome)
        
        
        
        ## processamento da flexibilidade
        flex.processamento(pessoa.id_pessoa)
        ## processamento da criatividade
        criativo.AnalizaCriatividade(pessoa.id_pessoa)
        ## processamento da fluencia
        fluencia.Calc_fluencia(pessoa.id_pessoa)     
        textos=Textos()   
        
        textos = textos.busca_processamento(pessoa.id_pessoa,"")   
        for texto in textos:
                tx = fun.converter(texto.texto_narrativa)
                
                ## analisa paradgma
                paradigma.analiseParadigma(pessoa.id_pessoa,texto.texto_narrativa,texto.id_narrativa)
                
                
                
                #processameto analise sintagmatica
                ##pro.processar(texto,pessoa.pessoa,pessoa.id_texto)  # analize morfologica
                ##pro2.processar(texto,pessoa.pessoa,pessoa.id_texto) # analize sintatica
                
                tx2+=" "+tx
                #eme.processar_eme(tx,pessoa.id_pessoa,texto.id_narrativa)
                PRHX.proc_RHx(pessoa.id_pessoa,texto.id_narrativa, tx2)
                
                #print(texto.texto_narrativa)
                #jabuti.analiseJabuti(pessoa.id_pessoa,texto.texto_narrativa,texto.fase)
                print("\r\n")        
        
        
        # serve pra criar a nuvem de palavras        
        # resultado =npmf.np_mais_frequentes(texto2,pessoa,id_texto)
        # npmf.salvaImg(id_pessoa,resultado,id_texto)
        
        
        print("terminou o texto do login "+ pessoa.login)
        print("-------------- \r\n")

## faz a anaise da originalidade
#porig.buscaGeral(listaPessoas)  


