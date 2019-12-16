#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host="",    # your host, usually localhost
                                       user="",         # your username
                                       passwd="",  # your password
                                       db="")        # name of the data base

# conn = mysql.connector.connect(host="raqueleluis.ddns.net",    # your host, usually localhost
# user="jogonarrativa",         # your username
# passwd="k9kbg1tmMAeK",  # your password
# db="omundo88_jogonarrativa")        # name of the data base

        #print("estou aqui vivo")
        return conn
    except Error as e:
        print(e)
        


def buscar(sql):
    cnx = connect()
    cur = cnx.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    cnx.close()
    return myresult

    
## def busca2(sql):
    ## cnx = connect()
    ## cur = cnx.cursor(dictionary=True)
    ## return cur.execute(sql)
    ## cnx.close()
    ## return cur


def alterar(sql):
    # cnx = connect()
    # cur = cnx.cursor()
    # cur.execute(sql)
    # cur.execute(sql)
    # myresult = cnx.commit()
    # return myresult
    return("ainda nao implementado")


def inserir(sql):
    try:
        cnx = connect()
        cur = cnx.cursor()
        cur.execute(sql)
        cnx.commit()
        cnx.close()
    except Error as error:
        print(error)
        print(sql)

    finally:
        cur.close()
        cnx.close()


def escapa(sql):
    return mysql.escape_string(sql)    