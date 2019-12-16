import numpy
import string 
import re
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# corpus = np.array(['bruxa,  castelo,  casa assombrada,  livro de feiticos,  caldeirao, varinha, vassoura, bola de cristal',
                #    'vampiro, castelo, capa, casa assombrada',
                #    'sereia,oceano,tridente,'
                #    'fada, varinha,floresta,castelo'])


def comparartodos (v, w):
    print ("coeficiente de similaridade:")
    variavel = numpy.dot(v,w) / numpy.sqrt(numpy.dot(v,v) * numpy.dot(w,w)) 
    return variavel





A = numpy.array(['bruxa',  'castelo', 'casa assombrada', 'livro de feiticos', 'caldeirao', 'varinha', 'bola de cristal','vassoura'])
C0 = numpy.array(['fada','floresta','castelo','varinha','coroa','caldeirao','castelo','varinha' ])
C1 = numpy.array([ 'sereia', 'oceano','', 'tridente','','','',''])
C2 = numpy.array(['mumia', 'egito','', 'sarcofago','farao','','',''])
C3 = numpy.array(['vampiro', 'castelo', 'casaassombrada', 'capa','caixao','','',''])
C4 = numpy.array(['mago', '', '', 'pedra filosofal','relogio','','','',''])

personagens= numpy.array(["A","C0","C1","C2","C3","C4"])


variavel = numpy.dot(A,C0) / numpy.sqrt(numpy.dot(A,A) * numpy.dot(C0,C0)) 
print variavel

# for x in personagens:
#     print x
#     variavel =  comparartodos(A,x)
#     print variavel

