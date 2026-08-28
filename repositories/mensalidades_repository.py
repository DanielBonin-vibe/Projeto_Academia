from database.conexao_postgre import conectar

def registrar_mensalidade(id_aluno, id_plano, valor, data_vencimento):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO (id_aluno, id_plano, valor, data_vencimento)
        VALUES (%s, %s, %s, %s)
        """, (id_aluno, id_plano, valor, data_vencimento))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao registrar mensalidade: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_mensalidades(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM mensalidades
        WHERE id_aluno = (
        SELECT id_aluno FROM alunos
        WHERE cpf = %s)
        """, (cpf,))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro a listar as mensalidades: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def buscar_pagamento(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT data_pagamento FROM mensalidade
        WHERE id_aluno = (
        SELECT * FROM alunos 
        WHERE cpf = %s)
        AND data_pagamento IS NOT NULL
        ORDER BY data_pagamento DESC
        LIMIT 5
        """, (cpf,))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao buscar pagamento: {erro}.')
        return []

    finally:
        cursor.close()
        conexao.close()

def consultar_mensalidade(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        
        """)

        resultado = ...

    except Exception as erro:
        ...
    finally:
        cursor.close()
        conexao.close()