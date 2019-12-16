#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class Jabuti(object):
    idprocessamento_jabuti = int
    id_pessoa = int
    fase_processamento = str
    resultado = str


    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        idprocessamento_jabuti = -1
        id_pessoa = -1
        fase_processamento = "null"
        resultado = "null"
    
    def carrega(self,id_pessoa):
        
        lista=[]
        resps =myc.buscar("select * from  processamento_jabuti  where id_pessoa = "+str(id_pessoa))
        for resp in resps:
            jabu = Jabuti()
            idprocessamento_jabuti = resp[0]
            id_pessoa = resp[1]
            fase_processamento = resp[2]
            resultado = resp[3]
            lista.append(jabu)  
        if len(lista) == 0:
            jabu = Jabuti()
            lista.append(jabu)  
        return lista
           
           
    def cadTxJabuti(self):    
        sql="""insert into 
                processamento_jabuti(id_pessoa,fase_processamento,resultado)
            value ("""+str(self.id_pessoa)+",'"+str(self.fase_processamento)+"','"+str(self.resultado)+"')" 
        #print(sql)
        myc.inserir(sql)   