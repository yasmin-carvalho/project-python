import psycopg2


class config():

    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='northwind' user='postgres' password='123456'"
        return self

    def alteraBD(self, stringSQL, valores):
        # iniciar a inserção do registro
        conn = None
        try:
            # abrir a conexão
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)

            # abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()

            # Executar a inserção na memória RAM
            sessao.execute(stringSQL, valores)

            # Comitar a inserção - fechar a transação
            conexao.commit()

            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error

        finally:
            if conn is not None:
                conn.close()
            return 'sucesso'

    def consultaBD(self, stringSQL, valores):
        # iniciar a inserção do registro
        conn = None
        try:
            # abrir a conexão
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)

            # abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()

            # Executar a consulta
            sessao.execute(stringSQL, valores)

            # Armazenar os resultados
            registros = sessao.fetchall()
            colnames = [desc[0] for desc in sessao.description]

            # Comitar para fechar a transação
            conexao.commit()

            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        else:
            if conn is not None:
                conn.close()
            return(colnames, registros)
