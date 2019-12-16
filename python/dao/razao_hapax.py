    #!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class RazaoHapax(object):
    idproc_razaoHapax=int 
    id_pessoa=int
    cod_tx=int
    numerodehapaxes=str
    qtd_palavras_texto=str
    hapax_legomana=str
    
    
    
    def __init__(self):
        self.idproc_razaoHapax=int
        self.id_pessoa=int
        self.cod_tx=int
        self.numerodehapaxes=str
        self.qtd_palavras_texto=str
        self.hapax_legomana=str
    
        
    def getRazaoHapax(self,id_pessoa):
        id_pessoa =str(id_pessoa)
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from proc_razaoHapax where id_pessoa = "+id_pessoa+"; ")
            #print("select * from objeto where id_pessoa = "+id_pessoa)
            for r in reto:
                #print(r)
                rh=RazaoHapax()
                rh.idproc_razaoHapax=r[0] 
                rh.id_pessoa=r[1]
                rh.cod_tx=r[2]
                rh.numerodehapaxes=r[3]
                rh.qtd_palavras_texto=r[4]
                rh.hapax_legomana=r[5]              
                lista.append(rh)
            if len(lista) == 0:
                rh=RazaoHapax()
                lista.append(rh)
            return lista 
        else:
            print("deu merda no objeto\r\n")
            return None
           
        
    def cadRazaoHapax(self):    
     sql="""INSERT INTO omundo88_jogonarrativa.proc_razaoHapax 
            ( id_pessoa, cod_tx, numerodehapaxes, qtd_palavras_texto, hapax_legomana) 
            VALUES ( """+str(self.id_pessoa)+",'"+str(self.cod_tx)+"','"+str(self.numerodehapaxes)+"','"+str(self.qtd_palavras_texto)+"','"+str(self.hapax_legomana)+"');" 
     #print(sql)
     myc.inserir(sql)   