from database.conexao_postgre import conectar

def cadastro_plano(nome_plano, valor):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO (id_plano, nome_plano, valor)
        VALUES (%s, %s)
        """, (nome_plano, valor))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Não foi possível cadastrar o plano: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_planos():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM planos
        """)

        resultado = cursor.fetchall()

        return resultado
    
    except Exception as erro:
        print(f'Erro ao listar os planos: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def buscar_plano(id_plano):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM planos
        WHERE id_plano = %s
        """, (id_plano,))

        resultado = cursor.fetchone()

        return resultado
    
    except Exception as erro:
        print(f'Erro ao listar os planos: {erro}.')
        return None

    finally:
        cursor.close()
        conexao.close()