#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class Missao:
    id_missao= int
    id_usuario= int
    recursospersonagem= str
    duracaomissao= str
    importanciamissao= str
    prejuizomissao= str
    demaisinfomissao= str
    finalfeliz= str
    facilidade= int
    aventura= int
    perigo= int
    biscoito= str
    tempo_gasto= str

    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        self.id_missao= -1
        self.id_usuario= -1
        self.recursospersonagem= ""
        self.duracaomissao= ""
        self.importanciamissao= ""
        self.prejuizomissao= ""
        self.demaisinfomissao= ""
        self.finalfeliz= ""
        self.facilidade= -1
        self.aventura= -1
        self.perigo= -1
        self.biscoito= ""
        self.tempo_gasto= ""
    
    def getMissao(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from missao where id_usuario = "+str(id_pessoa)+" group by id_usuario,recursospersonagem,duracaomissao,importanciamissao,prejuizomissao,demaisinfomissao,finalfeliz,facilidade,aventura,perigo,biscoito,tempo_gasto")
            for r in reto:
                m=Missao()
                m.id_missao= r[0]
                m.id_usuario= r[1]
                m.recursospersonagem= r[2]
                m.duracaomissao= r[3]
                m.importanciamissao= r[4]
                m.prejuizomissao= r[5]
                m.demaisinfomissao= r[6]
                m.finalfeliz= r[7]
                m.facilidade= r[8]
                m.aventura= r[9]
                m.perigo= r[10]
                m.biscoito= r[11]
                m.tempo_gasto= r[12]
                
                lista.append(m)
            if len(lista) == 0:
                m=Missao()
                lista.append(m)
            return lista
        else:
            return None
        
        
    def getTotal(id_pessoa):
        if(id_pessoa!=""):
            soma=0
            reto= myc.buscar("select * from missao where id_usuario = "+str(id_pessoa))
            m=Missao()
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
                if(r[9]!="" and r[9]!=" " and r[9]!=None):
                    soma+=1
                if(r[10]!="" and r[10]!=" " and r[10]!=None):
                    soma+=1  
            return soma
        else:
            return None
        
        
    def getTempoGasto(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from missao where id_usuario = "+id_pessoa)
            for r in reto:
                m=Missao()
                m.tempo_gasto= r[12]
                lista.append(m)
            if len(lista) == 0:
                m=Missao()
                lista.append(m)
            return lista
        else:
            return None
        
        
        
        