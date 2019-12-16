# -*- coding: latin-1 -*-

import random 
import MySQLdb
from collections import Counter

db = MySQLdb.connect(host="raqueleluis.ddns.net",    # your host, usually localhost
                     user="root",         # your username
                     passwd="luis3009",  # your password
                     db="omundo88_jogonarrativa")        # name of the data base


cur = db.cursor()

# variavel = "raquel"
# cur.execute("select * from pessoa where nome like '%"+variavel+"%'")
# for pessoas in cur.fetchall():
#      print (pessoas)


def verifica_palavras():


    num_caracteres = 0
    num_palavras = 0
    num_linhas = 0
    vogais = []
    consoantes = []

    cur.execute("select texto_narrativa from narrativa where id_usuario = 2")
    for recuperatexto in cur.fetchall():
        texto = recuperatexto
        print texto 
       
        for caracter in texto:
            if caracter in 'aeiou':
                vogais = vogais + 1 
            else:
                consoantes = consoantes + 1
                print "Vogais: %d" %vogais
                print "Consoantes: %d" %consoantes
                print "Total de letras: %d - %d" %(len(texto), (vogais+consoantes)) 
                total_linhas = len(texto.splitlines())
                total_caracteres = len(texto)
                total_palavras = len(texto.split())
                print ("numero de palavras:" + str(total_palavras))
                print ("Numero de linhas em texto:" + str(total_linhas))
                print ("Total de caracteres:" + str(total_caracteres))
                print ("-----------------")
                print texto.split(' ')

                print ("-----------------")
                print ("FREQUÊNCIA DE PALAVRAS:")
                palavras = texto.replace('\n',' ').replace('\t','').split(' ')
                contador = Counter(palavras)
                for i in contador.items():
                    print i



verifica_palavras()


# 
# def verifica_relacoes(personagem_escolhido):
    # sql= "select g.nome from grupo_de_escolhas g where tipo='Cenario' and g.id in (select ce.correlacao from  correlacao_escolhas ce inner join grupo_de_escolhas ge on (ce.atributo_pai=ge.id) where ge.nome like '"+personagem_escolhido+"')"
    
    # cur.execute(sql) 
    # for relacoes in cur.fetchall():
        # print (relacoes)
# 
