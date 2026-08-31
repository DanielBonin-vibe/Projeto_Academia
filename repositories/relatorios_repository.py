from database.conexao_postgre import conectar

def alunos_plano():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT
                alunos.nome,
                alunos.cpf,
                planos.nome,
                planos.valor
            FROM alunos
            JOIN planos
                ON alunos.id_plano = planos.id_plano
            ORDER BY planos.nome, alunos.nome
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar o relatório de alunos por plano: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def ordem_alfabetica_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM alunos
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar o relatório de alunos por ordem alfabética: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def alunos_mensalidades_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT alunos.nome, alunos.cpf, mensalidades.data_vencimento, mensalidades.data_pagamento, mensalidades.valor,
        FROM alunos 
        JOIN mensalidades
            ON alunos.id_aluno = mensalidade.id_plano
        WHERE mensalidades.data_pagamento is NULL
        ORDER BY mensalidades.data_vencimento
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar o relatório de mensalidades pendentes: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def quantidade_alunos_plano():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT planos.nome_plano COUNT(alunos.id_plano) FROM planos 
        JOIN alunos
            ON planos.id_plano = alunos.id_plano
        GROUP BY planos.nome
        ORDER BY planos.nome
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de quantidade de alunos por plano: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()
