#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc


class Paradigma(object):
    idproc_paradg=int
    id_pessoa=int
    cod_tx=int
    imagem=str
    paradigma=str
    socializado_palavras=str
    socializado_qtds=int
    intermediario_palavras=str
    intermediario_qtds=int
    egocentrico_palavras=str
    egocentrico_qtds=int

    def __init__(self):
        idproc_paradg=-1
        id_pessoa=-1
        cod_tx=-1
        imagem=""
        paradigma=""
        socializado_palavras=""
        socializado_qtds=-1
        intermediario_palavras=""
        intermediario_qtds=-1
        egocentrico_palavras=""
        egocentrico_qtds=-1
        
        
    def getobjeto(self,id_pessoa):
        id_pessoa =str(id_pessoa)
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from objeto where id_pessoa = "+id_pessoa+" group by id_objeto,id_pessoa,nomeobj,serventiaobjeto,funcaoobj,materialobjeto,historiaobjeto,comoobjchegaaopersonagem,pqobjeto,objselecao,tempo_gasto")
            #print("select * from objeto where id_pessoa = "+id_pessoa)
            for r in reto:
                p=Paradigma()
                p.idproc_paradg=r[0]
                p.id_pessoa=r[1]
                p.cod_tx=r[2]
                p.imagem=r[3]
                p.paradigma=r[4]
                p.socializado_palavras=r[5]
                p.socializado_qtds=r[6]
                p.intermediario_palavras=r[7]
                p.intermediario_qtds=r[8]
                p.egocentrico_palavras=r[9]
                p.egocentrico_qtds=r[10]
                print(r[0])
                lista.append(p)
            if len(lista) == 0:
                p=Paradigma()
                lista.append(p)
                return lista 
        else:
            print("deu merda no objeto\r\n")
        return None
    
    def updateParadigma(self):
        sql="""UPDATE omundo88_jogonarrativa.proc_paradgma SET 
                 imagem = '"""+str(self.imagem)+"""', 
                 paradgma = '"""+str(self.paradigma)+"""', 
                 socializado_palavras = '"""+str(self.socializado_palavras)+"""',
                 socializado_qtds = """+str(self.socializado_qtds)+""",
                 intermediario_palavras = '"""+str(self.intermediario_palavras)+"""', 
                 intermediario_qtds = """+str(self.intermediario_qtds)+""", 
                 egocentrico_palavras = '"""+str(self.egocentrico_palavras)+"""', 
                 egocentrico_qtds = """+str(self.egocentrico_qtds)+""" 
                 WHERE idproc_paradg = """+str(self.idproc_paradg)+""";"""
        #print(sql)
        myc.inserir(sql)




    def inserirParadigma(self):
         sql="""INSERT INTO omundo88_jogonarrativa.proc_paradgma (id_pessoa, cod_tx, imagem, paradgma, socializado_palavras, socializado_qtds, intermediario_palavras, intermediario_qtds, egocentrico_palavras, egocentrico_qtds) 
         VALUES ("""+str(self.id_pessoa)+",'"+str(self.cod_tx)+"','"+str(self.imagem)+"','"+str(self.paradigma)+"','"+str(self.socializado_palavras)+"','"+str(self.socializado_qtds)+"','"+str(self.intermediario_palavras)+"','"+str(self.intermediario_qtds)+"','"+str(self.egocentrico_palavras)+"','"+str(self.egocentrico_qtds)+"');"
         #print(sql)
         myc.inserir(sql)
         
         
         
         
         
    def cadParadigma(self):
        sql="select idproc_paradg from proc_paradgma where id_pessoa="+str(self.id_pessoa)+" and cod_tx="+str(self.cod_tx)
        #sql="select idproc_paradg from proc_paradgma where id_pessoa=-1"
        
        reto= myc.buscar(sql)
        if(reto==[]):
            print("entrei aqui")
            self.inserirParadigma()
        else:
            for r in reto:
                self.idproc_paradg=r[0]
                self.updateParadigma()
            
   