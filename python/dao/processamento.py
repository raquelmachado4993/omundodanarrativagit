# processamento.py
# Classe criada para abstracao da tabela de processamento

import dao.mysql_connect as myc


# processamento(
# id_pessoa
# datahora
# id_texto
# )

class Processamento:

    def __init__(self,id_pessoa, tipo_processamento, dados, id_texto):
        self.id_pessoa = id_pessoa
        self.tipo_processamento = tipo_processamento
        # self.dados = dados
        self.id_texto = id_texto
        

    def inserir(self):
        tip_proce= str((self.tipo_processamento))
        # tip_dad= str(((self.dados)))

        # dados,
        sql=("""INSERT INTO omundo88_jogonarrativa.processamento(id_pessoa,tipo_processamento,
        id_texto)VALUES("""
        +self.id_pessoa+",'"
        +tip_proce+"','"
        # +tip_dad+"',"
        +self.id_texto+");") 
        #print(sql)
        myc.inserir(sql)
