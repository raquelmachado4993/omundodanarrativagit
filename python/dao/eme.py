import dao.mysql_connect as myc


class Eme:
    
    def __init__(self,total_palavras, eme, id_pessoa,id_texto):
        self.total_palavras = str(total_palavras)
        self.eme = str(eme)
        self.id_pessoa = str(id_pessoa)
        self.id_texto=str(id_texto)
        
    
    def inserir(self):
        sql=("""insert into processamento_eme(num_palaras, extensao_media_enun, id_pessoa,id_texto)
        values ("""+self.total_palavras+""",'"""+self.eme+"""',"""+self.id_pessoa+""","""+self.id_texto+""");""")
        #print(sql)
        myc.inserir(sql)
         