#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class Objeto(object):
    id_objeto=int
    id_pessoa=int
    nomeobj=str
    serventiaobjeto=str
    funcaoobj=str
    materialobjeto=str
    historiaobjeto=str
    comoobjchegaaopersonagem=str
    pqobjeto=str
    objselecao=str
    tempo_gasto=str

    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        self.id_objeto=-1
        self.id_pessoa=-1
        self.nomeobj=""
        self.serventiaobjeto=""
        self.funcaoobj=""
        self.materialobjeto=""
        self.historiaobjeto=""
        self.comoobjchegaaopersonagem=""
        self.pqobjeto=""
        self.objselecao=""
        self.tempo_gasto=""
    
    def getTempoGasto(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from objeto where id_pessoa = "+id_pessoa)
            
            for r in reto:
                o=Objeto()
                o.tempo_gasto=r[10]
                lista.append(o)
            if len(lista) == 0:
                o=Objeto()
                lista.append(o)
                
            return lista
        else:
            return None
        
    def getobjeto(self,id_pessoa):
        id_pessoa =str(id_pessoa)
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from objeto where id_pessoa = "+id_pessoa+" group by id_pessoa,nomeobj,serventiaobjeto,funcaoobj,materialobjeto,historiaobjeto,comoobjchegaaopersonagem,pqobjeto,objselecao,tempo_gasto")
            #print("select * from objeto where id_pessoa = "+id_pessoa)
            
            for r in reto:
                #print(r)
                o=Objeto()
                o.id_objeto=r[0]
                o.id_pessoa=r[1]
                o.nomeobj=r[2]
                o.serventiaobjeto=r[3]
                o.funcaoobj=r[4]
                o.materialobjeto=r[5]
                o.historiaobjeto=r[6]
                o.comoobjchegaaopersonagem=r[7]
                o.pqobjeto=r[8]
                o.objselecao=r[9]
                o.tempo_gasto=r[10]                
                
                lista.append(o)
            if len(lista) == 0:
                o=Objeto()
                lista.append(o)
            return lista 
        else:
            print("deu merda no objeto\r\n")
            return None
           
        
    def getTotal(id_pessoa):
        if(id_pessoa!=""):
            soma=0
            reto= myc.buscar("select * from objeto where id_pessoa = "+str(id_pessoa))
            o=Objeto()
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
                if(r[7]!="" and r[7]!=" " and r[7]!=None):
                    soma+=1    
                if(r[8]!="" and r[8]!=" " and r[8]!=None):
                    soma+=1      
            return soma
        else:
            return None