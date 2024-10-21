import database

# Inserir usuário
# Insere um novo usuário e retorna o ID
def criar_usuario(usuario):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO usuario(nome, login, senha, email) VALUES ('{usuario['nome']}', '{usuario['login']}', '{usuario['senha']}','{usuario['e-mail']}')"
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()
def lista_usuario():
    usuarios = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM usuario ORDER BY nome'
        cursor.execute(sql)
        lista_usuario = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for usuario in lista_usuario:
            usuarios.append(
                {
                  'id': usuario[0],
                  'nome': usuario[1],
                  'login': usuario[2],
                  'senha': usuario[3],
                  'email': usuario[4]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar usuario: {ex}')
    finally:
        cursor.close()
        conect.close()    
    return usuarios