#textos.py

import dao.mysql_connect as myc

class Pessoas(object):
    id_pessoa =int
    login =str
    senha =str
    Nome =str
    tipo =str

    def __init__(self):
        pass

    def busca(self, tipo,id_pessoa):
        # print("aqui")
        if(tipo==""):
             sql= "select * from pessoa"
        elif(tipo=="lista"):
            sql="select * from pessoa where cod_pessoa in ("+id_pessoa+")"
        else:
             sql="select * from pessoa where tipo like '%"+tipo+"%' and cod_pessoa like '%"+id_pessoa+"%'"
        lista=[]
        resps =myc.buscar(sql)
        for resp in resps:
            pe = Pessoas()
            pe.id_pessoa=resp[0]
            pe.login=resp[1]
            pe.senha=resp[2]
            pe.Nome=resp[3]
            pe.tipo=resp[4]
            lista.append(pe)
        if len(lista) == 0:
            pe = Pessoas()
            lista.append(pe)
        return lista
    