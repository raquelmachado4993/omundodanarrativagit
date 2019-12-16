# -*- coding: utf-8 -*-
teste = ["ERA UMA VEZ um rei que vivia num reino distante, com a sua filha pequena, que se chamava Branca de Neve. O rei, como se sentia só, voltou a casar, achando que também seria bom para a sua filha ter uma nova mãe. A nova rainha era uma mulher muito bela mas também muito má, e não gostava de Branca de Neve que, quanto mais crescia, mais bela se tornava. A rainha malvada tinha um espelho mágico, ao qual perguntava, todos os dias: - Espelho meu, espelho meu, haverá mulher mais bela do que eu? E o espelho respondia: - Não minha rainha, és tu a mulher mais bela!"]
resposta = ''.join(teste)
resposta_minuscula = resposta.lower()
palavra = 'espelho'

if palavra in resposta_minuscula: 
   print 'sucesso'
   print resposta_minuscula.count(palavra)
else:
    print 'nao tem'

