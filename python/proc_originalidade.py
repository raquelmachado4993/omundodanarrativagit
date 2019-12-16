#!/usr/bin/python3
# -*- coding: utf-8 -*-        
import dao.mysql_connect as myc
from dao.jogador import Jogador as jogador
import math

def calculo_originalidade(tot_pessoas,tot_obj):
    calculo=math.ceil((tot_obj*100)/tot_pessoas)
     
    if calculo>60:
        return("não original") 
    elif calculo>30 and calculo<=60:
        return("não original") 
    elif calculo>10 and calculo<=30:
        return("pouco original")
    elif calculo<=10:
        return("original")
    

def buscaGeral(listapessoas):
    sql_total_pessoas="""select count(*) as total_pessoas from (select concat(p2.tipo_personagem,' - ',c.objcenario) as escolhas, c.id_pessoa
            from pessoa p
            inner  join perssonagem p2 on p.cod_pessoa = p2.id_pessoa
            inner join cenario c on p.cod_pessoa = c.id_pessoa
            where c.id_pessoa in  ("""+listapessoas+""")
            group by c.id_pessoa,escolhas) as tot_pessoas """
    tot_pessoas= myc.buscar(sql_total_pessoas)
    tot_pessoas=tot_pessoas[0][0]
    
    sql_comparacao="""select concat(p2.tipo_personagem,' - ',c.objcenario) as escolhas, c.id_pessoa
            from pessoa p
            inner  join perssonagem p2 on p.cod_pessoa = p2.id_pessoa
            inner join cenario c on p.cod_pessoa = c.id_pessoa
            where c.id_pessoa in  ("""+listapessoas+""")
            group by c.id_pessoa,escolhas """
    resps= myc.buscar(sql_comparacao)
    for resp in resps:
        ## print(resp)
        escolha_usuario=resp[0]
        id_pessoa=resp[1]

        sql_quantas_existem=""" select distinct p2.tipo_personagem,c.objcenario,c.id_pessoa
                                from pessoa p
                                inner  join perssonagem p2 on p.cod_pessoa = p2.id_pessoa
                                inner join cenario c on p.cod_pessoa = c.id_pessoa
                                where concat(p2.tipo_personagem,' - ',c.objcenario) 
                                like '"""+escolha_usuario+"""' ;"""
        #print("\r\n\r\n",sql_quantas_existem,"\r\n\r\n")
        tot_obj= myc.buscar(sql_quantas_existem)
        tot_obj=len(tot_obj)
        resp_original= calculo_originalidade(tot_pessoas,tot_obj)
        #print(id_pessoa," - ","escolhas ",resp_original)
        j=jogador()
        j.id_pessoa=id_pessoa
        j.originalidade=resp_original
        j.cadOriginalidade()

