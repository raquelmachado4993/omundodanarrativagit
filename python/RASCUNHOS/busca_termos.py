# -*- coding: utf-8 -*-
teste = ["ERA UMA VEZ um rei que vivia   num reino  distante,  com a sua filha pequena, que se chamava Branca de Neve. O rei, como se sentia só, voltou a casar, achando que também seria bom para a sua filha ter uma nova mãe. A nova rainha era uma mulher muito bela mas também muito má, e não gostava de Branca de Neve que, quanto mais crescia, mais bela se tornava. A rainha malvada tinha um espelho mágico, ao qual perguntava, todos os dias: - Espelho meu, espelho meu, haverá mulher mais bela do que eu? E o espelho respondia: - Não minha rainha, és tu a mulher mais bela!"]
resposta = ''.join(teste)
resposta_minuscula = resposta.lower()


pesquisar_esportes = ['futebol', 'vôlei', 'tênis de mesa', 'natação', 'futsal', 'capoeira', 'skate', 'skatismo', 'surf', 'vôlei de praia', 'badminton', 'frescobol', 'judô', 'atletismo', 'críquete', 'basquete', 'hockey na grama', 'hockey no gelo', 'beisebol', 'fórmula 1', 'Rugby', 'futebol americano', 'golfe', 'handebol', 'queimado', 'hipismo', 'ginástica olímpica', 'Triatlo', 'maratona', 'canoagem', 'peteca', 'jiu-jitsu', 'esgrima', 'vale-tudo', 'karatê', 'corrida', 'ciclismo', 'boxe', 'MMA', 'Taekwondo']
print(len(pesquisar_esportes))

# pesquisa = ''.join(pesquisar_esportes)
 
for i in pesquisar_esportes:
    if i in resposta_minuscula:
        print ("achei", i)
    
    if i not in resposta_minuscula:
        naoachei = "nao achei"

if naoachei == 'nao achei':
    print naoachei
        


    
    # else:
    #     if i not in resposta_minuscula:
    #         print ("Nao achei")
    # else:
        # if i not in resposta_minuscula:
            # print ("nao achei")
        
        # for i in pesquisar_esportes:
            # if i not in resposta_minuscula:
                # print ("nao achei")
    # 