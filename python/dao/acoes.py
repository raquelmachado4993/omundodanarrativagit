#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc
import dao.missao   as mis
import dao.objeto as obj
import dao.perssonagem as per 
import dao.transporte as trans
from dao.processamento import Processamento as pro


class Acoes(object):
    id_acao = int
    id_pessoa = int
    datahora = str
    tipo_acao = str
    acao =str

    # ,id_pessoa,datahora,tipo_acao,acao
    def __init__(self):
        id_acao = -1
        id_pessoa = -1
        datahora = ""
        tipo_acao = ""
        acao =""
    
    def carrega(self,id_pessoa,tipo):
        if(tipo==''):
            if(id_pessoa!=""):
                lista=[]
                
                resps =myc.buscar("select * from acoes where id_pessoa = "+str(id_pessoa))
                for resp in resps:
                    aco = Acoes()
                    aco.id_acao=resp[0]
                    aco.id_pessoa=resp[1]
                    aco.datahora=resp[2]
                    aco.acao=resp[3]
                    aco.tipo_acao=resp[4]
                    lista.append(aco)
                    #print(resp[3])  
                if len(lista) == 0:
                    aco = Acoes()
                    lista.append(aco)  
                return lista
            else:
                #print("algo errado")
                return None
        else:
            if(id_pessoa!=""):
                lista=[]
                sql="""select a.* from acoes a
                                    inner join pessoa p on a.id_pessoa = p.cod_pessoa
                                    where tipo_acao like '"""+str(tipo)+"""'
                                    and id_pessoa = """+str(id_pessoa)+"""
                                    group by a.id_acao, a.id_pessoa, a.datahora, a.tipo_acao, a.acao
                                    order by  id_pessoa,a.datahora"""
                print("\r\n\r\n\r\n\r\n\r\n"+sql+"\r\n\r\n\r\n\r\n")
                resps =myc.buscar(sql)
                for resp in resps:
                    aco = Acoes()
                    aco.id_acao=resp[0]
                    aco.id_pessoa=resp[1]
                    aco.datahora=resp[2]
                    aco.acao=resp[3]
                    aco.tipo_acao=resp[4]
                    #print(resp[4])                      
                    lista.append(aco)
                if len(lista) == 0:
                    aco = Acoes()
                    lista.append(aco)      
                return lista
            else:
                return None
            
            
            
    def busca_paradigma(self,id_pessoa):
        sql="select acao from acoes  where tipo_acao like 'direcao%' and id_pessoa="+str(id_pessoa)+" order by id_acao asc limit 1;" 
        #print(sql)
        resps =myc.buscar(sql)
        lista=[]
        for resp in resps: 
            aco = Acoes()
            aco.acao=resp[0]
            lista.append(aco)
        if len(lista) == 0:
            aco = Acoes()
            lista.append(aco)      
        return lista