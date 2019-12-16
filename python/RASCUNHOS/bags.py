from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing

# def salvainfo(texto):
    
    # print(texto)
    # print ("O menor valor e:", min(texto))
    # print ("O maior valor e:", max(texto))

corpus = [
'tridente sereia oceano',
'bruxa livrodefeitico vassoura castelo casaassombrada oceano',
'vampiro capa castelo casaassombrada',
'sereia oceano tridente',
'fada varinha floresta',
'tridente'
]

# w = ['tridente sereia oceano']

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
    variavel2=(vectorizer.inverse_transform(f),cosine_similarity(features[0],f))
    print variavel2
    # # print ("coeficiente de similaridade", cosine_similarity(features[0],f))
    # if (cosine_similarity(features[0],f) !=1):
    #     print (cosine_similarity(features[0],f))
    #     menossimilares.append()
    # # print "0s e 1s:"
    # # print(features[0])
    # # variavel.append(variavel2)
    # # print "Retornando o vetor original:"
    variavel.append(vectorizer.inverse_transform(features[0]))
    # print(vectorizer.inverse_transform(features[0]))
    # print ("Os menos similares sao:",menossimilares)
# menos_similares()


        

    


# salvainfo(variavel)




    

