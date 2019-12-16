#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dao.mysql_connect as myc

class Jogador(object):
    id_jogador=int
    id_pessoa=int
    qtd_jogadas=int
    tempo_jogado=float
    desistencias=int
    pegaajuda=int
    aceitasugestao=int
    flexibilidade=str
    personaliza=str
    originalidade=str
    fluencia=str
    criatividade=str
    adaptacao = str
    analisejabuti = str

    def __init__(self):
        self.qtd_jogadas='NULL'
        self.tempo_jogado='NULL'
        self.desistencias='NULL'
        self.pegaajuda='NULL'
        self.aceitasugestao='NULL'
        self.flexibilidade='NULL'
        self.personaliza='NULL'
        self.originalidade='NULL'
        self.fluencia='NULL'
        self.criatividade='NULL'
        self.adaptacao="null"
        self.analisejabuti="null"
    
    
    def getJogador(self,id_pessoa):
        if(id_pessoa!=""):
            lista=[]
            reto= myc.buscar("select * from jogador where id_pessoa = "+str(id_pessoa))
            for r in reto:
                j=Jogador()
                j.id_jogador=int(r[0])
                j.id_pessoa=int(r[1])
                j.qtd_jogadas=str(r[2])
                j.tempo_jogado=str(r[3])
                j.desistencias=str(r[4])
                j.pegaajuda=str(r[5])
                j.aceitasugestao=str(r[6])
                j.flexibilidade=str(r[7])
                j.personaliza=str(r[8])
                j.originalidade=str(r[9])
                j.fluencia=str(r[10])
                j.criatividade=str(r[11])
                j.adaptacao=str(r[12])
                lista.append(j)
            if len(lista) == 0:
                j=Jogador()
                lista.append(j)
            return lista
        else:
            return None
        
    def inicializa(self):
        sql="""INSERT INTO jogador(id_pessoa,qtd_jogadas,tempo_jogado,desistencias,pegaajuda,aceitasugestao,flexibilidade,personaliza,originalidade,fluencia,criatividade)
        VALUES("""+str(self.id_pessoa)+""", 
                """+str(self.qtd_jogadas)+""", 
                """+str(self.tempo_jogado)+""", 
                """+str(self.desistencias)+""", 
                """+str(self.pegaajuda)+""", 
                """+str(self.aceitasugestao)+""", 
                """+str(self.flexibilidade)+""", 
                """+str(self.personaliza)+""", 
                """+str(self.originalidade)+""", 
                """+str(self.fluencia)+""", 
                """+str(self.criatividade)+""");"""
        myc.inserir(sql)

    def cadOriginalidade(self):
        originalidade=self.originalidade
        resps =myc.buscar("select count(*) from jogador where id_pessoa="+str(self.id_pessoa))
        if(resps[0][0]==0):
            self.inicializa()
        #print("eu aqui")    
        sql=""" update jogador set originalidade='
            """+str(originalidade)+"' where id_pessoa="+str(self.id_pessoa)+";"
        #print(sql)
        myc.inserir(sql)
        
    def cadFluencia(self):
        fluencia=self.fluencia
        resps =myc.buscar("select count(*) from jogador where id_pessoa="+str(self.id_pessoa))
        if(resps[0][0]==0):
            self.inicializa()
        print("eu aqui")    
        sql=""" update jogador set fluencia='
            """+str(fluencia)+"' where id_pessoa="+str(self.id_pessoa)+";"
        #print(sql)
        myc.inserir(sql)       
    
    
    def cadFlexibilidade(self):
        flexibilidade=self.flexibilidade
        adaptacao= self.adaptacao
        resps =myc.buscar("select count(*) from jogador where id_pessoa="+str(self.id_pessoa))
        if(resps[0][0]==0):
            self.inicializa()
        print("eu aqui")    
        sql=""" update jogador set flexibilidade='
            """+str(flexibilidade)+"', adaptacao='"+str(adaptacao)+"' where id_pessoa="+str(self.id_pessoa)+";"
        #print(sql)
        myc.inserir(sql)   
        
        
        
    def cadCriatividade(self):
        criatividade=self.criatividade
        resps =myc.buscar("select count(*) from jogador where id_pessoa="+str(self.id_pessoa))
        if(resps[0][0]==0):
            self.inicializa()
        print("eu aqui")    
        sql=""" update jogador set criatividade='
            """+str(criatividade)+"' where id_pessoa="+str(self.id_pessoa)+";"
        #print(sql)
        myc.inserir(sql)   
        
        
    def cadJabuti(self):
        analisejabuti=self.analisejabuti
        resps =myc.buscar("select count(*) from jogador where id_pessoa="+str(self.id_pessoa))
        if(resps[0][0]==0):
            self.inicializa()
        print("eu aqui")    
        sql=""" update jogador set analisejabuti='
            """+str(analisejabuti)+"' where id_pessoa="+str(self.id_pessoa)+";"
        #print(sql)
        myc.inserir(sql)              