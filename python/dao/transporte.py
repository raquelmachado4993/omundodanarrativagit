#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc
#import mysql_connect as myc

class Transporte:
    id_transporte=int
    id_pessoa=int
    nometransporte=str
    caracteristica_transp=str
    capacidade_transp=str
    caracteristica_mistica_transp=str
    historia_transp=str
    objtransporte=str
    tempo_gasto=str

    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        self.id_transporte=-1
        self.id_pessoa=-1
        self.nometransporte=""
        self.caracteristica_transp=""
        self.capacidade_transp=""
        self.caracteristica_mistica_transp=""
        self.historia_transp=""
        self.objtransporte=""
        self.tempo_gasto=""

    
    def getTempoGasto(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from transporte where id_pessoa = "+id_pessoa)
            for r in reto:
                t=Transporte()
                t.tempo_gasto=r[8]
                lista.append(t)
            if len(lista) == 0:
                t=Transporte()
                lista.append(t)
            return lista
        else:
            return None

    def getTotal(id_pessoa):
        if(id_pessoa!=""):
            soma=0
            reto= myc.buscar("select * from transporte where id_pessoa = "+str(id_pessoa))
            t=Transporte()
            for r in reto:
                soma=0
                #print (r)
                if(r[2]!="" and r[2]!=" " and r[2]!=None):
                    soma+=1
                if(r[3]!="" and r[3]!=" " and r[3]!=None):
                    soma+=1
                if(r[4]!="" and r[4]!=" " and r[4]!=None):
                    soma+=1
                if(r[5]!="" and r[5]!=" " and r[5]!=None):
                    soma+=1
                if(r[6]!="" and r[6]!=" " and r[6]!=None):
                    soma+=1    
            return soma
        else:
            return None
        
        
    def getTransporte(self,id_pessoa):
        id_pessoa= str(id_pessoa)
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from transporte where id_pessoa = "+id_pessoa+" group by id_pessoa,nometransporte,caracteristica_transp,capacidade_transp,caracteristica_mistica_transp,historia_transp,objtransporte,tempo_gasto")
            
            for r in reto:
                t=Transporte()
                #print(r)                
                t.id_pessoa=r[1]
                t.nometransporte=r[2]
                t.caracteristica_transp=r[3]
                t.capacidade_transp=r[4]
                t.caracteristica_mistica_transp=r[5]
                t.historia_transp=r[6]
                t.objtransporte=r[7]
                t.tempo_gasto=r[8]            
                lista.append(t)
            if len(lista) == 0:
                t=Transporte()
                lista.append(t)
            return lista
        else:
            print("deu merda no transporte")
            return None