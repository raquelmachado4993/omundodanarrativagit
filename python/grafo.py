#!/usr/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#import networkx as nx
from networkx import *
import re
import time
from datetime import datetime
from  valores import Valores as valores

from dao.processamento_outros_dados import Processamento_outros_dados as pod
from dao.acoes import Acoes as acoes
    
def pegatempo(acao):
    if(acao=='escolheu ir para o fasecenarios'):
        return "cenário" 
                
    if(re.search('missao', acao, re.IGNORECASE)):
        return "missao"
      
    if(re.search('objeto', acao, re.IGNORECASE)):
        return "objeto"
      
    if(re.search('personagem', acao, re.IGNORECASE)):
        return "personagem"
        
    if(re.search('transporte', acao, re.IGNORECASE)):
        return "transporte"
    else:
        return ""        
 
 
 
def criagrafo(lista,id_pessoa,nome):
    G = networkx.Graph()
    edge_labels={}
    
    if(lista!=[]):
        for lis in lista:
            G.add_edge(lis.vertice1, lis.vertice2, weight=0.1)   
            dic = {(lis.vertice1,lis.vertice2):lis.arest} 
            edge_labels.update(dic)
            #edge_labels[(lis.vertice1,lis.vertice2)]=lis.arest

        ## layout antigo
        #pos = nx.shell_layout(G)
        ## tipo de layout
        pos = networkx.shell_layout(G)
        # nodes
        networkx.draw_networkx_nodes(G, pos, node_size=900)
        # edges
        networkx.draw_networkx_edges(G, pos, width=1)
        networkx.draw_networkx_edges(G, pos, 
                               width=1, alpha=0.5, edge_color='k', style='solid')
        # labels
        networkx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        networkx.draw_networkx_edge_labels(G,pos,edge_labels, font_color='red')
        plt.axis('off')
        arquivos='img_processamento/grafico_'+str(nome)+'.png'
        #plt.savefig(arquivos, dpi=100)
        plt.savefig(arquivos, dpi=None, facecolor='w', edgecolor='w',
                    orientation='portrait', papertype=None, format=None,
                    transparent=False, bbox_inches=None, pad_inches=0.1,
                    frameon=None, metadata=None)
        #time.sleep(30)
        plt.show()
        #time.sleep(10)
 
 
 
def processa_grafo(id_pessoa,nome):       
    anterior=valores()
    posterior=valores()
    ac =acoes()             
    anterior=""
    temp_anterior=""
    temp_posterior=""
    lista=[]
    contador=0
    acos = ac.carrega(id_pessoa,"direcao")   
    for aco in acos:
        contador+=1
        #resp =str(contador)+" - "+pegatempo(aco.tipo_acao)
        resp =pegatempo(aco.tipo_acao)
        time = datetime.time(aco.datahora)
        if(anterior==""):
            anterior=resp
            temp_anterior =time.strftime('%H:%M:%S')
        else:
            temp_posterior=time.strftime('%H:%M:%S')                
            FMT = '%H:%M:%S'
            arest = datetime.strptime(temp_posterior, FMT) - datetime.strptime(temp_anterior, FMT)
            val =valores()
            val.vertice1=anterior
            val.vertice2=resp
            val.arest=arest
            lista.append(val)
            anterior=resp
            temp_anterior=temp_posterior
    #print(lista)
    print(nome+"\r\n\r\n")
    criagrafo(lista,id_pessoa,nome)       
                
  

#listas=(36,13,39,20,11,19,15,24,7,16,9,6)
#for l in listas:    
#    processa_grafo(l)
#print("terminou")

