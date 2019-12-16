#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import nltk
import math
import  funcoes as func
 
from dao.processamento import Processamento as pro
from dao.jogador import Jogador as jogador

from dao.perssonagem import Perssonagem as per
from dao.cenario import Cenario as cen
from dao.objeto import Objeto as obj
from dao.transporte import Transporte as trans
from dao.missao import Missao as mis

def Calc_fluencia(id_pessoa):
    total=0
    total_per   = per.getTotal(id_pessoa)
    total_cen   = cen.getTotal(id_pessoa)
    total_obj   = obj.getTotal(id_pessoa)
    total_trans = trans.getTotal(id_pessoa)
    total_mis   = mis.getTotal(id_pessoa)
    
    total_per   = (total_per*100)/13
    total_cen   = (total_cen*100)/8
    total_obj   = (total_obj*100)/7
    total_trans = (total_trans*100)/5
    total_mis   = (total_mis*100)/9
    
    total=math.ceil((total_per+total_cen+total_obj+total_trans+total_mis)/5)
    
    if total>=0 and total<=30:
        total=("fluencia limitada") 
    elif total>30 and total<=60:
        total=("potencial fluencia")
    elif total>60:
        total=("fluente")
    
    
    
    j=jogador()
    j.id_pessoa=id_pessoa
    j.fluencia=total
    j.cadFluencia()
    
    
    #print("total: ",total_per)
    #print("total: ",total_cen)
    #print("total: ",total_obj)
    #print("total: ",total_trans)
    #print("total: ",total_mis)


    print("temos isso",total)
    print("\r\n\r\n")