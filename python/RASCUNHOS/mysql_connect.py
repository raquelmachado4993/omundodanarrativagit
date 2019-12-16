import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host="raqueleluis.ddns.net",    # your host, usually localhost
                                       user="jogonarrativa",         # your username
                                       passwd="k9kbg1tmMAeK",  # your password
                                       db="omundo88_jogonarrativa")        # name of the data base

##        conn = mysql.connector.connect(host="raqueleluis.ddns.net",    # your host, usually localhost
##                                       user="jogonarrativa",         # your username
##                                       passwd="k9kbg1tmMAeK",  # your password
##                                       db="omundo88_jogonarrativa")        # name of the data base



        #print("estou aqui vivo")
        return conn
    except Error as e:
        print(e)


def buscar(sql):
    cnx = connect()
    cur = cnx.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    return myresult



def alterar(sql):
    cnx = connect()
    cur = cnx.cursor()
    cur.execute(sql)
    cur.execute(sql)
    myresult = cnx.commit()
    return myresult



