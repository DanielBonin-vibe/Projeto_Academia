

def relatorio_aluno_padrao():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM alunos
    """)

    relatorio = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO ALUNO PADRÃO', '=' * 15)
    print('=' * 50)
    for aluno in relatorio:
        print(f'ID: {aluno[0]}')
        print(f'NOME: {aluno[1]}')
        print(f'IDADE: {aluno[2]}')
        print(f'CPF: {aluno[3]}')
        print(f'PLANO: {aluno[4]}')
        print()

    cursor.close()
    conexao.close()

def relatorio_aluno_nome_ordem_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM alunos
    ORDER BY nome ASC
    """)

    relatorio = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO ALUNO PELO NOME', '=' * 15)
    print('=' * 50)
    for aluno in relatorio:
        print(f'ID: {aluno[0]}')
        print(f'NOME: {aluno[1]}')
        print(f'IDADE: {aluno[2]}')
        print(f'CPF: {aluno[3]}')
        print(f'PLANO: {aluno[4]}')
        print()

    cursor.close()
    conexao.close()

def relatorio_aluno_media_idade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        CASE
            WHEN idade < 14 THEN '<14, Precisam de autorização.'
            WHEN idade BETWEEN 14 AND 17 THEN '14 a 17'
            WHEN idade BETWEEN 18 AND 30 THEN '18 a 30'
            WHEN idade BETWEEN 31 AND 50 THEN '31 a 50'
            ELSE '51+'
        END AS faixa_etaria,
        COUNT(*) quantidade
    FROM alunos
    GROUP BY faixa_etaria
    ORDER BY faixa_etaria;
    """) 

    faixas = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO ALUNO POR FAIXA ETÁRIA', '=' * 15)
    print('=' * 50)
    for faixa in faixas:
        print(f'Faixa etária: {faixa[0]}')
        print(f'Total: {faixa[1]}')
        print()

    cursor.close()
    conexao.close()

    return faixas

def relatorio_aluno_plano():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT aluno.id_aluno, plano.nome_plano FROM alunos
    JOIN planos
        ON alunos.id_plano = planos.id_plano;
    """)

    planos = cursor.fetchall()

    for plano in planos:
        print(plano[0], plano[1])

    cursor.close()
    conexao.close()

    return planos

####################################################################################################
# Relatórios professor:

def relatorio_professor_padrao():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professores
    """)

    professores = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO PROFESSOR PADRÃO', '=' * 15)
    print('=' * 50)
    for professor in professores:
        print(f'ID: {professor[0]}')
        print(f'NOME: {professor[1]}')
        print(f'IDADE: {professor[2]}')
        print(f'CPF: {professor[3]}')
        print(f'ESPECIALIDADE: {professor[4]}')
        print()

    cursor.close()
    conexao.close()

    return professores

def relatorio_professor_nome_ordem_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professores
    ORDER BY nome ASC
    """)

    professores = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO PROFESSOR PELO NOME', '=' * 15)
    print('=' * 50)
    for professor in professores:
        print(f'ID: {professor[0]}')
        print(f'NOME: {professor[1]}')
        print(f'IDADE: {professor[2]}')
        print(f'CPF: {professor[3]}')
        print(f'ESPECIALIDADE: {professor[4]}')
        print()

    cursor.close()
    conexao.close()

    return professores

def relatorio_professor_media_idade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        CASE 
            WHEN idade < 18 THEN 'Menor de idade, apenas estágio.'
            WHEN idade BETWEEN 18 AND 25 THEN '18 a 25'
            WHEN idade BETWEEN 26 AND 40 THEN '26 a 40'
            WHEN idade BETWEEN 41 AND 60 THEN '41 a 60'
            ELSE '60+'
        END AS faixa_etaria
        COUNT(*) quantidade
    FROM professor
    ORDER BY faixa_etaria
    GROUP BY faixa_etaria;
    """)

    faixas = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO PROFESSOR POR FAIXA ETÁRIA', '=' * 15)
    print('=' * 50)
    for faixa in faixas:
        print(f'Faixa etária: {faixa[0]}')
        print(f'Total: {faixa[1]}')
        print()

    cursor.close()
    conexao.close()

    return faixas

def relatorio_professor_especialidade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id_professor,
        nome,
        idade,
        cpf,
        especialidade
    FROM professores
    ORDER BY especialidade ASC
    """)

    professores = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO PROFESSOR ESPECIALIDADE', '=' * 15)
    print('=' * 50)
    for professor in professores:
        print(f'ID: {professor[0]}')
        print(f'NOME: {professor[1]}')
        print(f'IDADE: {professor[2]}')
        print(f'CPF: {professor[3]}')
        print(f'ESPECIALIDADE: {professor[4]}')
        print()

    cursor.close()
    conexao.close()

    return professores

##############################################################################
# Relatórios mensalidade:

def relatorio_mensalidade_media():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT AVG(valor) FROM planos
    """)

    resultado = cursor.fetchone()

    print(f"MÉDIA DOS PLANOS: R$ {resultado[0]}")

    cursor.close()
    conexao.close()

    return resultado[0]

def relatorio_mensalidade_situacao():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT pago FROM mensalidades
    """)

    dado = cursor.fetchall()

    for pagamento in dado: 
        if pagamento[0] == 0:
            print('Pagamento pendente')
        else:
            print('Pagamento concluído')    

    cursor.close()
    conexao.close()

    return dado

def relatorio_mensalidade_faturamento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT 
        SUM(plano.valor) AS faturamento_esperado,
        SUM(CASE
            WHEN mensalidades.pago = 1 THEN planos.valor
            ELSE 0
        END) AS faturamento_recebido
    FROM mensalidades
    JOIN planos
        ON mensalidades.id_plano = planos.id_plano
    """)

    faturamento = cursor.fetchone()

    print(f'Faturamento esperado: R$ {faturamento[0]}')
    print(f'Faturamento recebido: R$ {faturamento[1]}')

    cursor.close()
    conexao.close()

    return faturamento