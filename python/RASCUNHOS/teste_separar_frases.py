# coding=utf-8

import nltk
from nltk.tokenize import sent_tokenize
from nltk import tokenize  

segmentador_frases=nltk.data.load('tokenizers/punkt/portuguese.pickle')  
mytext = "Era uma vez um lugarzinho no meio do nada, com sabor de chocolate e cheiro de terra molhada. O nome dela é Jennifer."
frases=segmentador_frases.tokenize(mytext)


print("Número de frases encontradas:",len(frases),"\n")
print("Exemplos de frases encontradas:\n")


for i in range(0,2):
  print("Frase ",i,": <<",frases[i],">>\n")


# #separa frases 

# print(sent_tokenize(mytext,"portuguese"))


# #separa palavras
# palavras_tokenize = tokenize.word_tokenize(mytext, language='portuguese')   
# print (palavras_tokenize)