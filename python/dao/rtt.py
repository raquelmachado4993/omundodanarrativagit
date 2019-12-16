import dao.mysql_connect as myc


class Textos:
    
    def __init__(self,id_pessoa,qtd_types,qtd_tokens,rtt,id_texto):
        self.id_pessoa =str(id_pessoa)
        self.qtd_types=str(qtd_types)
        self.qtd_tokens= str(qtd_tokens)
        self.rtt =str(rtt)
        self.id_texto = str(id_texto)



    def inserir(self):
        sql=("""insert into processamento_rtt(id_pessoa,qtd_types,qtd_tokens,rtt,id_texto)
                values ("""+self.id_pessoa+""",'"""+self.qtd_types+""",'"""
                +self.qtd_tokens+""",'"""+self.rtt+""",'"""+self.id_texto+"""');""")
        # print(sql)
        myc.inserir(sql)