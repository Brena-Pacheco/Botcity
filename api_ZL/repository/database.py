import mysql.connector

def criar_db():
    try:
        # Configuração do Banco de Dados MySQL
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='banco_zl'
        )
    except Exception as ex:
        print(f'Ocorreu erro na conexão com o Banco de Dados: {ex}')        
    return mydb

