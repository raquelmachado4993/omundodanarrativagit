# -*- coding: utf-8 -*-
import re
sentence = "Eu amava amar você"
word = "ama"
for match in re.finditer(word, sentence):
    print (match.start(), match.end())

