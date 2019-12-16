
# -*- coding: utf-8 -*-
import re

total_ocorrencias_paradigma_egocentrico = 0 



def verifica_amav(texto):
    substring = 'amav'
    if substring in texto:
        total_ocorrencias_paradigma_egocentrico +1
        count = texto.count(r'amav')
        print("'amav'  / contagem de ocorrencias : " , count)
        
    else:
        print ("O radical -amav- não foi encontrado!")
    return

def verifica_e_foram_felizes_para_sempre(texto):
    substring1 = "e foram felizes para sempre"  
    if substring1 in texto:
        total_ocorrencias_paradigma_egocentrico +1
        verificando_grafia_e_foram_felizes_para_sempre = 'achou' 
    else:
        verificando_grafia_e_foram_felizes_para_sempre = 'nao'  
    return 


def verifica_e_foram_felizes_pra_sempre(texto):
    substring1 = "e foram felizes pra sempre"
    if substring1 in texto:
        total_ocorrencias_paradigma_egocentrico +1
        verificando_grafia_e_foram_felizes_pra_sempre = 'achou'
    else:
        verificando_grafia_e_foram_felizes_pra_sempre = 'nao'

    return


def verifica_felizes(verifica_e_foram_felizes_para_sempre, verifica_e_foram_felizes_pra_sempre):
    if verifica_e_foram_felizes_para_sempre or verifica_e_foram_felizes_pra_sempre == 'achou':
        total_ocorrencias_paradigma_egocentrico +1
        print ("Sentido de 'Felizes para sempre' - ENCONTRADO")
    else:
        print ("Sentido de 'Felizes para sempre' - NÃO ENCONTRADO") 
    return


def verifica_sentido_casar (texto):
    substring1 = "casaram"
    if substring1 in texto:
        total_ocorrencias_paradigma_egocentrico +1
        print ("Sentido de casar / casamento - ENCONTRADO")
    else:
        print ("Sentido de casar / casamento - NÃO ENCONTRADO")
    
    return


def verifica_sentido_namoro_namorar(texto):
    substring = "namor"
    if substring in texto:
        total_ocorrencias_paradigma_egocentrico +1
        print ("Sentido de namoro / namorar - ENCONTRADO")
    else:
        print ("Sentido de namoro / namorar - NÃO ENCONTRADO")
    
    return 

def verifica_sentido_castigo_castigar(texto):
    substring = "castig"
    if substring in texto:
        total_ocorrencias_paradigma_egocentrico +1
        print ("Sentido de castigo / castigar - ENCONTRADO")
    else:
        print ("Sentido de castigo / castigar - NÃO ENCONTRADO")
    return 


def verifica_papai_do_ceu(texto):
    substring1 = "papai do céu"  
    if substring1 in texto:
        print ("Menção a papai do céu - ENCONTRADA") 
    else:
        print ("Menção a papai do cẽu - NÃO ENCONTRADA")  
    return 

def verifica_papai_noel(texto):
    substring1 = "papai noel"
    if substring1 in texto:
        print ("Menção a papai noel - ENCONTRADA")
    else:
        print ("Menção a papai noel - NÃO ENCONTRADA")
    return


def verifica_anjo_da_guarda(texto):
    substring1 = "anjo da guarda"
    if substring1 in texto:
        print ("Menção a anjo da guarda - ENCONTRADA")
    else:
        print ("Menção a anjo da guarda - NÃO ENCONTRADA")
    return

    


























teste = [" era amigo  natação UMA VEZ um namorado lutar vôlei o rei amavam o rei tinha uma namorada papai do céu que vivia batalha num reino  distante,  com a sua filha pequena, que se chamava Branca de Neve. O rei, como se sentia só, voltou a , achando que também seria bom para a sua filha ter uma nova mãe. A nova rainha era uma mulher muito bela mas também muito má, e não gostava de Branca de Neve que, quanto mais crescia, mais bela se tornava. A rainha malvada tinha um espelho mágico, ao qual perguntava, todos os dias: - Espelho meu, espelho meu, haverá mulher mais bela do que eu? E o espelho respondia: - Não minha rainha, és tu a mulher mais bela! então eles casaram e não foram felizes pra sempre"]
texto = ''.join(teste)
texto = texto.lower()
# remove espaços, linhas e símbolos de pontuação
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")
# 
#remove acentos e cedilha
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")

verifica_amav(texto)
verifica_felizes (verifica_e_foram_felizes_para_sempre, verifica_e_foram_felizes_pra_sempre)
verifica_sentido_casar (texto)
verifica_sentido_castigo_castigar(texto)
verifica_sentido_namoro_namorar(texto)
verifica_papai_do_ceu(texto)
verifica_papai_noel(texto)
verifica_anjo_da_guarda(texto)