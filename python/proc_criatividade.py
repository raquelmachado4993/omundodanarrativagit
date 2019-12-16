#!/usr/bin/python3
# -*- coding: utf-8 -*-        
import dao.mysql_connect as myc


def buscaGeral(id_pessoa):
    print("\r\n",id_pessoa)
    sql=""" select p.cod_pessoa,p.Nome,p2.tipo_personagem,c.objcenario from pessoa p
            left  join perssonagem p2 on p.cod_pessoa = p2.id_pessoa
            left join cenario c on p.cod_pessoa = c.id_pessoa
            where c.id_pessoa="""+str(id_pessoa)+ """ group by p.cod_pessoa,p.Nome,p2.tipo_personagem,c.objcenario ; """
    
    resps= myc.buscar(sql)
    originalidade=""
    for resp in resps:
        
        originalidade = correlacao(resp[2],resp[3])
        #print("\r\n",resp[2]," - ",resp[3])
    return originalidade



def  correlacao(personagem,local):        
    
    lista={('et','espacosideral'),
    ('et','saladecontroleespacial'),
    ('animais','floresta'),
    ('animais','montanhas'),
    ('animais','deserto'),
    ('animais','fundodomar'),
    ('animais','safari'),
    ('arvores','floresta'),
    ('arvores','montanhas'),
    ('astronauta','espacosideral'),
    ('astronauta','saladecontroleespacial'),
    ('astronauta','laboratorio'),
    ('bruxa','casaassombrada'),
    ('cientistas','laboratorio'),
    ('cientistas','saladecontroleespacial'),
    ('dino','floresta'),
    ('dino','montanhas'),
    ('dino','cidade'),
    ('elfa','floresta'),
    ('elfa','casanaarvore'),
    ('elfa','montanhas'),
    ('fada','floresta'),
    ('fantasma','casaassombrada'),
    ('farao','egito'),
    ('farao','deserto'),
    ('frutas','floresta'),
    ('frutas','montanhas'),
    ('frutas','cidade'),
    ('frutas','casanaarvore'),
    ('legumes','cidade'),
    ('legumes','floresta'),
    ('lobisomem','floresta'),
    ('lobisomem','montanha'),
    ('monstro','calabouço'),
    ('monstro','casaassombrada'),
    ('monstro','portas'),
    ('ogro','floresta'),
    ('ogro','caverna'),
    ('pirata','fundodomar'),
    ('pirata','praia'),
    ('rei','floresta'),
    ('princesa','floresta'),
    ('robo','laboratorio'),
    ('robo','saladecontroleespacial'),
    ('robo','espacosideral'),
    ('samurai','japao'),
    ('samurai','montanhas'),
    ('sereia','fundodomar'),
    ('sereia','praia'),
    ('sereshumanos','cidade'),
    ('sereshumanos','iglu'),
    ('sereshumanos','laboratorio'),
    ('Soldados','cidade'),
    ('Soldados','floresta'),
    ('heroi','cidade'),
    ('transformer','escola'),
    ('vampiro','casaassombrada'),
    ('vampiro','caverna'),
    ('vampiro','floresta'),
    ('barbaro','montanhas'),
    ('barbaro','floresta'),
    ('zumbi','cidade'),
    ('zumbi','aeroporto'),
    ('zumbi','aeroport'),
    ('zumbi','escola'),
    ('zumbi','estadio'),
    ('zumbi','festa'),
    ('zumbi','parquedediversoes'),
    ('zumbi','portas'),
    ('mumia','casaassombrada'),
    ('mumia','egito'),
    ('mumia','caverna'),
    ('mumia','calabouco')}
    
    resposta=True
    #print(lista)
    for a in lista:
        
        if(a[0]==personagem):
            if(a[1]==local):
                resposta=False
    return resposta    
            
    
# print(buscaGeral(24))
# print(buscaGeral(36))
# print(buscaGeral(13))
# print(buscaGeral(39))
# print(buscaGeral(20))
# print(buscaGeral(11))
# print(buscaGeral(19))
# print(buscaGeral(15))
# print(buscaGeral(24))
# print(buscaGeral(7))
# print(buscaGeral(16))
# print(buscaGeral(9))
# print(buscaGeral(6))