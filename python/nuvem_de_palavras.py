# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt




texto = 'A Rainha tinha um espelho magico, para o qual ela perguntava frequentemente, olhando para si mesma: “Espelho, espelho meu, existe alguem mais bonita do que eu?” E o espelho sempre respondia a mesma coisa: “Nao, ninguem e mais linda do que minha Rainha.”'
wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(texto)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('nuvem.png', dpi=100)
plt.show()
