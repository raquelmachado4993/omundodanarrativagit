#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc

class Perssonagem(object):
    id_perssonagem=int
    id_pessoa=int
    nome=str
    idade=int
    onde_mora=str
    melhore_amigos=str
    inimigos=str
    carac_fisio=str
    carac_psico=str
    carac_poderes=str
    mais_info=str
    inteligencia=int
    forca=int
    criatividade=int
    coragem=int
    tipo_personagem=str
    id_imagem=int
    tempo_gasto=str

    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        self.id_perssonagem=-1
        self.id_pessoa=-1
        self.nome=""
        self.idade=-1
        self.onde_mora=""
        self.melhore_amigos=""
        self.inimigos=""
        self.carac_fisio=""
        self.carac_psico=""
        self.carac_poderes=""
        self.mais_info=""
        self.inteligencia=-1
        self.forca=-1
        self.criatividade=-1
        self.coragem=-1
        self.tipo_personagem=""
        self.id_imagem=-1
        self.tempo_gasto=""

    def getTempoGasto(id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from perssonagem where id_pessoa = "+str(id_pessoa))
            p=Perssonagem()
            for r in reto:
                p.tempo_gasto=r[17]
                lista.append(p)
            return lista
        else:
            return None
        
        
    def getPersonagem(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from perssonagem where id_pessoa = "+str(id_pessoa))
            for r in reto:
                p=Perssonagem()
                p.id_perssonagem=r[17]
                p.id_pessoa=r[17]
                p.nome=r[17]
                p.idade=r[17]
                p.onde_mora=r[17]
                p.melhore_amigos=r[17]
                p.inimigos=r[17]
                p.carac_fisio=r[17]
                p.carac_psico=r[17]
                p.carac_poderes=r[17]
                p.mais_info=r[17]
                p.inteligencia=r[17]
                p.forca=r[17]
                p.criatividade=r[17]
                p.coragem=r[17]
                p.tipo_personagem=r[17]
                p.id_imagem=r[17]
                p.tempo_gasto=r[17]
                lista.append(p)
            if len(lista) == 0:
                p=Perssonagem()
                lista.append(p)
            return lista
        else:
            return None
        
        
    def getTotal(id_pessoa):
        if(id_pessoa!=""):
            soma=0
            reto= myc.buscar("select * from perssonagem where id_pessoa = "+str(id_pessoa)+" group by id_pessoa,nome,idade,onde_mora,melhore_amigos,inimigos,carac_fisio,carac_psico,carac_poderes,mais_info,inteligencia,forca,criatividade,coragem,tipo_personagem,id_imagem,tempo_gasto")
            for r in reto:
                soma=0
                #print (r)
                if(r[2]!=""and r[2]!=" " and r[2]!=None):
                    soma+=1
                if(r[3]!=""and r[3]!=" " and r[3]!=None):
                    soma+=1
                if(r[4]!=""and r[4]!=" " and r[4]!=None):
                    soma+=1
                if(r[5]!=""and r[5]!=" " and r[5]!=None):
                    soma+=1
                if(r[6]!=""and r[6]!=" " and r[6]!=None):
                    soma+=1
                if(r[7]!=""and r[7]!=" " and r[7]!=None):
                    soma+=1    
                if(r[8]!=""and r[8]!=" " and r[8]!=None):
                    soma+=1
                if(r[9]!=""and r[9]!=" " and r[9]!=None):
                    soma+=1
                if(r[10]!=""and r[10]!=" " and r[10]!=None):
                    soma+=1
                if(r[11]!=""and r[11]!=" " and r[11]!=None):
                    soma+=1
                if(r[12]!=""and r[12]!=" " and r[12]!=None):
                    soma+=1   
                if(r[13]!=""and r[13]!=" " and r[13]!=None):
                    soma+=1   
                if(r[14]!=""and r[14]!=" " and r[14]!=None):
                    soma+=1                 
            return soma
        else:
            return None
