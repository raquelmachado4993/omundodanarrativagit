from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing

C0 = ['bruxa',  'castelo', 'casa assombrada', 'livro de feiticos', 'caldeirao', 'varinha', 'bola de cristal','vassoura']
C1 = ['fada','floresta','castelo','varinha','coroa','caldeirao','castelo','varinha' ]
C2 = [ 'sereia', 'oceano','', 'tridente','','','','']
C3 = ['mumia', 'egito','', 'sarcofago','farao','','','']
C4 = ['vampiro', 'castelo', 'casaassombrada', 'capa','caixao','','','']
C5 = ['mago', '', '', 'pedra filosofal','relogio','','','','']

w = ['tridente', ,'sereia', 'oceano']

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).todense()
w = vectorizer.fit_transform(corpus).todense()
# print( vectorizer.vocabulary_ )


menossimilares=[]

# def menos_similares():
#     if cosine_similarity(features[0],f) < 1.0:
#         menossimilares.append(vectorizer.inverse_transform(f))
#         print ("Os itens menos similares sao:", menossimilares)

variavel=[]
for f in features:
    variavel2=(f,cosine_similarity(features[0],f))
    # print ("coeficiente de similaridade", cosine_similarity(features[0],f))
    if (cosine_similarity(features[0],f) !='1.'):
        print (cosine_similarity(features[0],f))
        menossimilares.append(vectorizer.inverse_transform(f))
    # print "0s e 1s:"
    # print(features[0])
    # variavel.append(variavel2)
    # print "Retornando o vetor original:"
    variavel.append(vectorizer.inverse_transform(features[0]))
    # print(vectorizer.inverse_transform(features[0]))
    # print ("Os menos similares sao:",menossimilares)
# menos_similares()


        

    


# salvainfo(variavel)




    

