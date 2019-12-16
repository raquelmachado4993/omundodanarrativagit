# -*- coding: utf-8 -*-
teste = ["ERA  natação UMA VEZ um  vôlei rei que vivia   num reino  distante,  com a sua filha pequena, que se chamava Branca de Neve. O rei, como se sentia só, voltou a casar, achando que também seria bom para a sua filha ter uma nova mãe. A nova rainha era uma mulher muito bela mas também muito má, e não gostava de Branca de Neve que, quanto mais crescia, mais bela se tornava. A rainha malvada tinha um espelho mágico, ao qual perguntava, todos os dias: - Espelho meu, espelho meu, haverá mulher mais bela do que eu? E o espelho respondia: - Não minha rainha, és tu a mulher mais bela!"]
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
# 
# 
# 
# 






pesquisar_esportes = ['futebol', 'volei', 'tênis de mesa', 'natacao', 'futsal', 'capoeira', 'skate', 'skatismo', 'surf', 'vôlei de praia', 'badminton', 'frescobol', 'judô', 'atletismo', 'críquete', 'basquete', 'hockey na grama', 'hockey no gelo', 'beisebol', 'fórmula 1', 'Rugby', 'futebol americano', 'golfe', 'handebol', 'queimado', 'hipismo', 'ginástica olímpica', 'Triatlo', 'maratona', 'canoagem', 'peteca', 'jiu-jitsu', 'esgrima', 'vale-tudo', 'karatê', 'corrida', 'ciclismo', 'boxe', 'MMA', 'Taekwondo']
#print(len(pesquisar_esportes))

# pesquisa = ''.join(pesquisar_esportes)

esportes_encontrados = [] 
for i in pesquisar_esportes:

    if i in texto:
        esportes_encontrados.append(i)
        
    if i not in texto:
        naoachei = "nao achei"

print esportes_encontrados
quantidade_esportes = len(esportes_encontrados)
print ("Quantidade de esportes:", quantidade_esportes)
