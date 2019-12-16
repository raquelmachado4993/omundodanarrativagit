import re
import string
import numpy as np

corpus = np.array(['a vaca desceu', 
'porque ela quis',
'nao sei',
'morreu',
'caiu',
'se machucou',
'se arrebentou toda',
'se ferrou',
'se deu mal'
])

resposta_usuario = np.array(['Por que ela quis'])

def clear_text(text):
    pattern = "[{}]".format(string.punctuation)
    text = [word.lower() for word in text]
    text = [[re.sub(pattern,"",word) for word in words.split()] for words in text]
    text = [[word for word in words if len(word)>1] for words in text]
    text = [''.join(words) for words in text]
return np.array(text)

corpus_clear = clear_text(corpus)

def text_all(text):
    text_set = set()
    for w in [words.split() for words in text]:
        text_set.update(w) 
    return np.array(list(text_set))

vocabulary = text_all(corpus_clear)

def fit_transform(text, words=vocabulary):
    return [1 if word in text.split() else 0 for word in words]

features = np.array(list(map(fit_transform,corpus_clear)))

def cosine_similarity(v,w):
    return np.dot(v,w)/np.sqrt(np.dot(v,v)*np.dot(w,w)


# def text_simillarities(n_text=3):
#     simillarity = [[cosine_similarity(features[id_text], feature), int(i)] for i, feature in enumerate(features)]
#     simillarity = np.array(sorted(simillarity, key = lambda sim: sim[0], reverse=True))
#     return [[text[y], simillarity[x,0]] for x,y in enumerate(np.int0(simillarity[1:,1]), 1) [:n_text]

print ('Texto analisado ->,' resposta_usuario, '\n')
for t, s in text_simillarities(3):
	print ('Texto: {} | Similaridade: {}.format(t,round(s,2)))