#!/usr/bin/python3
# -*- coding: utf-8 -*-
import dao.mysql_connect as myc
from datetime import datetime

reto= myc.buscar(""" select (select Nome from pessoa where cod_pessoa=lo.id_pessoa) as nome ,
                    (select data_espiracao from credenciais where cod_pessoa=lo.id_pessoa
                         and  cast(data_espiracao as date ) = cast(lo.data as date)
                        order by  data_espiracao asc limit 1 ) as inicio,
                    (select data from log_jogo
                     where pag_acessada like 'https://www.omundodanarrativa.com.br/narrativ%'
                     and id_pessoa=lo.id_pessoa
                     and  cast(data as date) = cast(lo.data as date)
                     order by  data desc limit 1) as final,
                    (select aplicacao from aplicacoes where lo.data
                     between data_inicio and data_fim) as aplicacao
                    from log_jogo lo
                    where id_pessoa in (36,13,39,20,18,11,12,19,15,26,27,24,22,7,16,9,8,6)
                    group by nome,inicio, final,aplicacao""")
for r in reto:
    nome=r[0]
    inicio=r[1]
    final=r[2]
    aplicacao=r[3]
    
    if(inicio!=None):
        inicio = datetime.time(inicio)
        inicio =inicio.strftime('%H:%M:%S')
    if(final!=None):
        final = datetime.time(final)
        final =final.strftime('%H:%M:%S')
        
    if(inicio!=None and final!=None):    
        FMT = '%H:%M:%S'
        arest = datetime.strptime(final, FMT) - datetime.strptime(inicio, FMT)
        print("pessoa "+str(nome)+" com o tempo "+str(arest)+" na fase "+str(aplicacao))
    else:
        print("pessoa "+str(nome)+" com o tempo 0  na fase "+str(aplicacao))
    
            