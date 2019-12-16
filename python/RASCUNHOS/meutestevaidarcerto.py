# import statments
import numpy
import re

# def tokenize(sentences):
#     words = []
#     for sentence in sentences:
#         w = word_extraction(sentence)
#         words.extend(w)
        
#     words = sorted(list(set(words)))
#     return words

def word_extraction(sentence):
    ignore = ['a', "the", "is"]
    words = re.sub("[^\w]", " ",  sentence).split()
    cleaned_text = [w.lower() for w in words if w not in ignore]
    return cleaned_text    
    
def generate_bow(allsentences):    
    vocab = (allsentences)
    

    for sentence in allsentences:
        words = word_extraction(sentence)
        bag_vector = numpy.zeros(len(vocab))
        for w in words:
            for i,word in enumerate(vocab):
                if word == w: 
                    bag_vector[i] += 1
                    
        print("{0} \n{1}\n".format(sentence,numpy.array(bag_vector)))


allsentences = numpy.array(['bruxa',  'castelo',  'casa assombrada',  'livro de feiticos',  'caldeirao', 'varinha', 'bola de cristal','vassoura'])



generate_bow(allsentences)
