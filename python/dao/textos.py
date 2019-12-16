#textos.py

import dao.mysql_connect as myc

class Textos(object):
    id_narrativa =int 
    id_usuario = int
    texto_narrativa = str
    tempo_gasto = str
    fase =str


    def __init__(self):
        id_narrativa =-1 
        id_usuario = -1
        texto_narrativa = ""
        tempo_gasto = ""
        fase =""
    
    def busca_processamento(self,id_pessoa,fase):
        lista=[]
        sql=("""select n.* from pessoa pe inner join narrativa n on pe.cod_pessoa = n.id_usuario
                                where n.id_narrativa not in ( select id_texto from processamento)
                                and cod_pessoa = """+str(id_pessoa)+" group by id_usuario,texto_narrativa,tempo_gasto,fase")
        if(fase!=""):
            sql+=""" and fase="""+fase
        
        #print("sql é ", sql)
        resps =myc.buscar(sql)
        for resp in resps:
            tx= Textos()
            tx.id_narrativa=resp[0]
            tx.id_usuario=resp[1]
            tx.texto_narrativa=resp[2]
            tx.tempo_gasto=resp[3]
            tx.fase=resp[4]
            lista.append(tx)
        if len(lista) == 0:
            tx= Textos()
            lista.append(tx)
        return lista