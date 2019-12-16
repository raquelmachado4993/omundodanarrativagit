import dao.mysql_connect as myc


class Nuvem_palavras:
    
    def __init__(self,id_pessoa, imagem, id_texto):
        self.id_pessoa = str(id_pessoa)
        self.imagem = str(imagem)
        self.id_texto=str(id_texto)
        

    def inserir(self):
        sql=("""insert into nuvem_palavras(id_pessoa,imagem)
                values ("""+self.id_pessoa+""",'"""+self.imagem+"""');""")
        # print(sql)
        myc.inserir(sql)