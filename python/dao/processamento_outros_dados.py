import dao.mysql_connect as myc

# processamento_outros_dados(
# id_processamento
# termo
# classe)


class Processamento_outros_dados:
    
    def __init__(self,id_pessoa, id_processamento, termo, classe):
        self.id_processamento = id_processamento
        self.termo = termo
        self.classe = classe
        self.id_pessoa = id_pessoa
        

    def inserir(self):

        sql=("""INSERT INTO omundo88_jogonarrativa.processamento_outros_dados
             (id_processamento , termo, classe)VALUES("""
        +self.id_processamento+",'"
        +self.termo+"','"
        + self.id_pessoa +");") 
        #print(sql)
        myc.inserir(sql)
