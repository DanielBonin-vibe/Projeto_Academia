from database.conexao_postgre import conectar

def cadastro_aluno(nome, idade, cpf, id_plano):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO alunos(nome, idade, cpf, id_plano)
        VALUES(%s, %s, %s, %s)
        RETURN id_aluno
        """, (nome, idade, cpf, id_plano))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado
        else:
            conexao.rollback()
            return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao cadastrar aluno: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM alunos
        """)
        
        listagem = cursor.fetchall()

        total = len(listagem)

        return listagem, total

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao listar alunos: {erro}.')
        return 0
    finally:
        cursor.close()
        conexao.close()

def buscar_aluno(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM alunos
        WHERE cpf = %s
        """, (cpf,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao buscar aluno: {erro}.')
        return None

    finally:
        cursor.close()
        conexao.close()