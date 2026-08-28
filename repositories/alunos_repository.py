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

def alterar_plano(cpf, plano):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE ALUNOS
        SET id_plano = %s
        WHERE cpf = %s
        """, (cpf, plano))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao alterar o plano: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def excluir_aluno(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        DELETE FROM mensalidades
        WHERE id_aluno =
        (SELECT id_aluno FROM alunos 
        WHERE cpf = %s)
        """, (cpf,))

        cursor.execute("""
        DELETE FROM alunos
        WHERE cpf = %s
        """, (cpf,))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro a excluir aluno: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def mostrar_mensalidade(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM mensalidades
        WHERE id_aluno = (
        SELECT * FROM alunos 
        WHERE cpf = %s)
        """, (cpf,))

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao mostrar a mensalidade: {erro}.')
        return 0
        
    finally:
        cursor.close()
        conexao.close()