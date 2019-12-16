
# -*- coding: utf-8 -*-
mainStr = 'Era uma vez um rei que amava uma princesa, ela também amava ele então eles se amavam'
substring = 'amav'
if substring in mainStr:
	count = mainStr.count('que amava uma princesa')
        print ("O radical foi encontrado")
        print("'que amava uma princesa'  / contagem de ocorrencias : " , count)
	
else:
    print ("O radical não foi encontrado!")