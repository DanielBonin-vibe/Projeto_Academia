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


################################################

def receital_total():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT SUM(valor) FROM mensalidades
        WHERE data_pagamento IS NOT NULL
        """)

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de quantidade de alunos por plano: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def receital_periodo():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT
                DATE_TRUNC('month', data_pagamento) AS mes,
                SUM(valor)
            FROM mensalidades
            WHERE data_pagamento IS NOT NULL
            AND data_pagamento >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
            AND data_pagamento < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'
            GROUP BY DATE_TRUNC('month', data_pagamento)
            ORDER BY mes
        """)


        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de receita por período: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def mensalidades_pagas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT id_mensalidade, id_aluno, valor, data_vencimento FROM mensalidades
        WHERE data_pagamento IS NOT NULL
        ORDER BY data_pagamento DESC
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidades pagas: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def mensalidades_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT id_mensalidade, id_aluno, valor, data_vencimento FROM mensalidades
        WHERE data_pagamento IS NULL
        ORDER BY data_vencimento
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidades pendentes: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def total_pendente():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT SUM(valor) FROM mensalidades
        WHERE data_pagamento IS NULL
        """)

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de valor total de mensalidades pendentes: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

##################################################################

def ordem_alfabetica_professores():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM professores
        ORDER BY nome DESC
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de professores em ordem alfabética: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def professor_especialidade():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM professores
        ORDER BY especialidade ASC
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de professores por especialidade: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

#############################################

def mensalidades_mes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM mensalidades
        WHERE data_vencimento >= DATE_TRUNC('month', CURRENT_DATE)
        AND data_vencimento < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidade por mês: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def mensalidades_pagas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM mensalidades
        WHERE data_pagamento IS NOT NULL
        AND data_pagamento >= DATE_TRUNC('month', CURRENT_DATE)
        AND data_pagamento < ('month' DATE_TRUNC) + INTERVAL '1 month'
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidade por mês pagas: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def mensalidades_pendentes():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM mensalidades
        WHERE data_pagamento IS NULL
        AND data_vencimento >= DATA_TRUNC('month' CURRENT_DATA)
        AND data_vencimento < DATA_TRUNC('month' CURRENT_DATA) + INTERVAL '1 month'
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidade por mês pagas: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()

def percentual_inadimplencia():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT COUNT(*) FROM mensalidades
        WHERE data_pagamento IS NOT NULL
        AND data_pagamento >= DATE_TRUNC('month', CURRENT_DATE)
        AND data_pagamento < ('month' DATE_TRUNC) + INTERVAL '1 month'
        """)

        pagas = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM mensalidades
        WHERE data_pagamento IS NULL
        AND data_vencimento >= DATA_TRUNC('month' CURRENT_DATA)
        AND data_vencimento < DATA_TRUNC('month' CURRENT_DATA) + INTERVAL '1 month'
        """)

        pendentes = cursor.fetchone()[0]

        total = pagas + pendentes 

        if total == 0:
            return 0

        percentual = (pendentes / total) * 100

        return percentual

    except Exception as erro:
        print(f'Erro ao gerar relatório de mensalidade por mês pagas: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()
