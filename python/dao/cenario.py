#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class Cenario(object):
    id_cenario = int
    id_pessoa = int
    nome_cenario = str
    explica_cenario = str
    localizacao_do_cenario = str
    caracteristicas_fisicas_cenario = str
    caracteristicas_misticas_cenario = str
    historia_cenario = str
    outras_info_cenario = str
    motivo_escolha_cenario = str
    objcenario = str
    tempo_gasto= str


    def __init__(self):
        self.id_cenario = -1
        self.id_pessoa = -1
        self.nome_cenario = ""
        self.explica_cenario = ""
        self.localizacao_do_cenario = ""
        self.caracteristicas_fisicas_cenario = ""
        self.caracteristicas_misticas_cenario = ""
        self.historia_cenario = ""
        self.outras_info_cenario = ""
        self.motivo_escolha_cenario = ""
        self.objcenario = ""
        self.tempo_gasto= ""
    
    def getCenario(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from cenario where id_pessoa = "+str(id_pessoa)+" group by id_pessoa,nome_cenario,explica_cenario,localizacao_do_cenario,caracteristicas_fisicas_cenario,caracteristicas_misticas_cenario,historia_cenario,outras_info_cenario,motivo_escolha_cenario,objcenario,tempo_gasto ")
            for r in reto:
                #print (r)
                c=Cenario()
                c.id_cenario =r[0]
                c.id_pessoa = r[1]
                c.nome_cenario = r[2]
                c.explica_cenario = r[3]
                c.localizacao_do_cenario = r[4]
                c.caracteristicas_fisicas_cenario = r[5]
                c.caracteristicas_misticas_cenario = r[6]
                c.historia_cenario = r[7]
                c.outras_info_cenario = r[8]
                c.motivo_escolha_cenario = r[9]
                c.objcenario = r[10]
                c.tempo_gasto= r[11]
                lista.append(c)
            
            if len(lista) == 0:
                c=Cenario()
                lista.append(c)
            return lista
        else:
            return None
        
    def getTotal(id_pessoa):
        if(id_pessoa!=""):
            soma=0
            reto= myc.buscar("select * from cenario where id_pessoa = "+str(id_pessoa))
            c=Cenario()
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
            return soma
        else:
            return None
        
        
        
        