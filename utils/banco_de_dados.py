from database.conexao_postgre import conectar

#####################################################################
# Cadastros:

def cadastro_aluno(nome, idade, cpf, id_plano):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO alunos(nome, idade, cpf, id_plano)
    VALUES(%s, %s, %s, %s)
    RETURN id_aluno
    """, (nome, idade, cpf, id_plano))

    id_aluno = cursor.fetchone()[0]

    cursor.execute("""
    INSERT INTO mensalidades (id_aluno, id_plano)
    VALUES (%s, %s)
    """, (id_aluno, id_plano))


    conexao.commit()
    cursor.close()
    conexao.close()

    return {'mensagem': f'O ID do aluno é {id_aluno}'}

def cadastro_professor(nome, idade, cpf, especialidade):
    conexao =  conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO professores(nome, idade, cpf, especialidade)
    VALUES(%s, %s, %s, %s)
    RETURNING id_professor
    """, (nome, idade, cpf, especialidade))

    id_professor = cursor.fetchone()[0]

    conexao.commit()
    cursor.close()
    conexao.close()

    return {'mensagem': f'O ID do aluno é {id_professor}'}

def descadastrar_aluno(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_aluno
        FROM alunos
        WHERE cpf = %s
    """, (cpf,))
    aluno = cursor.fetchone()

    if aluno is None:
        cursor.close()
        conexao.close()
        return {'mensagem': 'Aluno não encontrado'}

    id_aluno = aluno[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM mensalidades
        WHERE id_aluno = %s
        AND pago = FALSE
    """, (id_aluno,))

    mensalidades_pendentes = cursor.fetchone()[0]

    if mensalidades_pendentes > 0:
        cursor.close()
        conexao.close()

        return {
            'mensagem': 'Não é possível excluir o aluno. Existem mensalidades pendentes.'
        }

    cursor.execute("""
        DELETE FROM mensalidades
        WHERE id_aluno = %s
    """, (id_aluno,))

    cursor.execute("""
        DELETE FROM alunos
        WHERE id_aluno = %s
    """, (id_aluno,))

    conexao.commit()
    cursor.close()
    conexao.close()

    return {'mensagem': 'Aluno descadastrado com sucesso'}

def descadastrar_professor(cpf_professor):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM professores
    WHERE cpf = %s
    """, (cpf_professor,))

    quantidade = cursor.rowcount

    conexao.commit()
    cursor.close()
    conexao.close()

    return quantidade

#######################################################################
# Listagem

def listagem_alunos():
    conexao =  conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM alunos
    """)
    
    listagem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM alunos
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return listagem, total

def listagem_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professores
    """)

    listagem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM professores
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return listagem, total

#############################################################
# Pesquisas:
   
def pesquisa_aluno_id(id_aluno_informado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id_aluno FROM alunos
    WHERE id_aluno = %s
    """, (id_aluno_informado,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def pesquisa_aluno_nome(nome_informado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM alunos
    WHERE nome LIKE %s
    """, (f'%{nome_informado}%',))

    resultado = cursor.fetchone()[3]

    cursor.close()
    conexao.close()

    return resultado 

def pesquisa_professor_id(id_informado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professores
    WHERE id_professor = %s
    """, (id_informado,))

    resultado = cursor.fetchone()[1]

    cursor.close()
    conexao.close()

    return resultado

def pesquisa_professor_nome(nome_professor_informado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professores
    WHERE nome LIKE %s
    """, (f'%{nome_professor_informado}%',))

    resultado = cursor.fetchone()[3]

    cursor.close()
    conexao.close()

    return resultado

#############################################################
# Ações:

def verificacao_status_financeiro(cpf): 
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT mensalidade.id_plano, plano.nome_plano, plano.valor, mensalidade.pago
    FROM mensalidades
    JOIN planos
        ON mensalidades.id_plano = planos.id_plano
    JOIN alunos
        ON mensalidades.id_aluno = alunos.id_aluno
    WHERE alunos.cpf = ?
    """, (cpf,))

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

#############################################################
# Relatórios aluno:

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