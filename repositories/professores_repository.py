from database.conexao_postgre import conectar


def cadastrar_professor(nome, idade, cpf, especialidade):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO professores (nome, idade, cpf, especialidade)
        VALUES (%s, %s, %s, %s)
        """, (nome, idade, cpf, especialidade))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao cadastrar professor: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()


def listar_professores():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM professores
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao listar professores: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()


def buscar_professor(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM professores
        WHERE cpf = %s
        """, (cpf,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao buscar professor: {erro}.')
        return None

    finally:
        cursor.close()
        conexao.close()


def alterar_professor(id_professor, nome, idade, cpf, especialidade):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE professores
        SET nome = %s, idade = %s, cpf = %s, especialidade = %s
        WHERE id_professor = %s
        """, (nome, idade, cpf, especialidade, id_professor))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao alterar professor: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()


def excluir_professor(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        DELETE FROM professores
        WHERE cpf = %s
        """, (cpf,))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

        conexao.rollback()
        return 0

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao excluir professor: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()