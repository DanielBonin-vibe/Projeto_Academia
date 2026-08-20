import sqlite3

conexao = sqlite3.connect('database/academia.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno(
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL,
    id_plano TEXT NOT NULL,

    FOREIGN KEY(id_plano) REFERENCES plano(id_plano))
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mensalidade(
    id_mensalidade INTERGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_plano INTEGER NOT NULL,
    pago INTEGER NOT NULL DEFAULT 0,

    FOREIGN KEY(id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY(id_plano) REFERENCES plano(id_plano))
""") #'id_aluno' será uma chave estrangeira, que referencia a coluna 'id-aluno' da tabela aluno

cursor.execute("""
CREATE TABLE IF NOT EXISTS professor(
    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL,
    especialidade TEXT NOT NULL)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS plano(
    id_plano INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_plano TEXT NOT NULL,
    valor REAL NOT NULL)
""")

cursor.execute("""
INSERT OR IGNORE INTO plano (nome_plano, valor)
VALUES('Básico', 79.99)
""")

cursor.execute("""
INSERT OR IGNORE INTO plano (nome_plano, valor)
VALUES('Interprise', 99.99)
""")

cursor.execute("""
INSERT OR IGNORE INTO plano (nome_plano, valor)
VALUES('Deluxe', 150.00)
""")

#####################################################################
# Cadastros:

def cadastro_aluno(nome, idade, cpf, id_plano):
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO aluno(nome, idade, cpf, id_plano)
    VALUES(?, ?, ?, ?)
    """, (nome, idade, cpf, id_plano))

    id_aluno = cursor.lastrowid     # pega o ID que acabou de ser criado para o aluno

    cursor.execute("""
    INSERT INTO mensalidade (id_aluno, id_plano)
    VALUES(?, ?)
    """, (id_aluno, id_plano))

    conexao.commit
    conexao.close()


def cadastro_professor(nome, idade, cpf, especialidade):
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO professor(nome, idade, cpf, especialidade)
    VALUES(?, ?, ?, ?)
    """, (nome, idade, cpf, especialidade))

    conexao.commit()
    conexao.close()

def descadastrar_aluno(id_aluno):
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM mensalidade
    WHERE id_aluno = ?
    """, (id_aluno))

    cursor.execute("""
    DELETE FROM aluno
    WHERE id_aluno = ?
    """, (id_aluno))

    if cursor.rowcount == 0:                      # Serve para verificar se o id existe mesmo
        print('Aluno, não encontrado')
    else:
        print('Aluno e mensalidade removidos com sucesso.')

    conexao.commit()
    conexao.close()

def descadastrar_professor(cpf_professor):
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM professor
    WHERE cpf = ?
    """, (cpf_professor))

    if cursor.rowcount == 0:
        print('Professor não localizado')
    else:
        print('Professor removido com sucesso.')

    conexao.commit()
    conexao.close()

#######################################################################
# Listagem

def listagem_alunos():
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM aluno
    """)
    
    listagem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM aluno
    """)

    total = cursor.fetchone()[0]

    for aluno in listagem:
        print(f'ID: {aluno[0]}')
        print(f'Nome: {aluno[1]}')
        print(f'CPF: {aluno[2]}')
        print(f'Telefone: {aluno[3]}')
        print(f'Plano: {aluno[4]}')
        print('-' * 30)

    print(f'Total de alunos: {total}')
    print('Listagem concluída')

    conexao.close()

    return listagem

def listagem_professor():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professor
    """)

    listagem = cursor.fetchall()

    for professor in listagem:
        print(f'ID: {professor[0]}')
        print(f'Nome: {professor[1]}')
        print(f'Idade: {professor[2]}')
        print(f'CPF: {professor[3]}')
        print(f'Especialidade: {professor[4]}')

    conexao.close()

    return listagem

#############################################################
# Pesquisas:
   
def pesquisa_aluno_id(id_aluno_informado):
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id_aluno FROM aluno
    WHERE id_aluno = ?
    """, (id_aluno_informado))

    resultado = cursor.fetchone()

    if resultado:
        print(f'ID: {resultado[0]}')
        print(f'Nome: {resultado[1]}')
    else:
        print('Aluno não encontrado')

    conexao.close()

    return resultado

def pesquisa_aluno_nome(nome_informado):
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT nome FROM aluno
    WHERE nome LIKE ?
    """, (f'%{nome_informado}%'))

    resultado = cursor.fetchall()

    for aluno in resultado:
        print(aluno)

    conexao.close()

    return resultado 

def pesquisa_professor_id(id_informado):
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id_professor FROM professor
    WHERE id_professor = ?
    """, (id_informado))

    resultado = cursor.fetchone()

    if resultado:
        print(f'ID: {resultado[0]}')
        print(f'Nome = {resultado[1]}')
    else:
        print('Professor não encontrado.')

    conexao.close()

    return resultado

def pesquisa_professor_nome(nome_informado):
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT nome FROM professor
    WHERE nome LIKE ?
    """, (f'%{nome_informado}%'))

    resultado = cursor.fetchall()

    for professor in resultado:
        print(professor)

    conexao.close()

    return resultado

#############################################################
# Ações:

def verificacao_status_financeiro(id_aluno): 
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT mensalidade.id_plano, plano.nome_plano, plano.valor, mensalidade.pago FROM mensalidade
    JOIN plano
        ON mensalidade.id_plano = plano.id_plano 
    WHERE mensalidade.id_aluno
    """, (id_aluno))

    resultado = cursor.fetchone()

    if resultado:
        print(f'Plano: {resultado[1]}')
        print(f'Valor: R$ {resultado[2]}')

        if resultado[3] == 1:
            print('Status: Pago')
        else:
            print('Status: Pendente')

    else:
        print('Nenhuma mensalidade encontrada para esse aluno.')

    conexao.close()

    return resultado

#############################################################
# Relatórios aluno:

def relatorio_aluno_padrao():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM aluno
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

    conexao.close()

def relatorio_aluno_nome_ordem_alfabetica():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM aluno
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

    conexao.close()

def relatorio_aluno_media_idade():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        CASE
            WHEN idade BETWEEN 14 AND 17 THEN '14 a 17'
            WHEN idade BETWEEN 18 AND 30 THEN '18 a 30'
            WHEN idade BETWEEN 31 AND 50 THEN '31 a 40'
            ELSE '51+'
        END AS faixa_etaria,
        COUNT(*) quantidade
    FROM aluno
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

    conexao.close()

def relatorio_aluno_plano():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT aluno.id_aluno, plano.nome_plano FROM aluno
    JOIN plano
        ON aluno.id_plano = plano.id_plano;
    """)

    planos = cursor.fetchall()
    for plano in planos:
        print(plano[0], plano[1])

    conexao.close()

####################################################################################################
# Relatórios professor:

def relatorio_professor_padrao():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professor
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

def relatorio_professor_nome_ordem_alfabetica():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM professor
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

def relatorio_professor_media_idade():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        CASE 
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

    conexao.close()

def relatorio_professor_especialidade():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id_professor,
        nome,
        idade,
        cpf,
        especialidade
    FROM professor
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

##############################################################################
# Relatórios mensalidade:

def relatorio_mensalidade_media():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT AVG(valor) FROM plano
    """)

    resultado = cursor.fetchone()

    print(f'MÉDIA MENSAL: R$ {resultado[0]}')

    cursor.close()

def relatorio_mensalidade_situacao():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT pago FROM mensalidade
    """)

    dado = cursor.fetchall()

    for pagamento in dado: 
        if pagamento[0] == 0:
            print('Pagamento pendente')
        else:
            print('Pagamento concluído')    

    conexao.close()

def relatorio_mensalidade_faturamento():
    conexao = sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT 
        SUM(plano.valor) AS faturamento_esperado,
        SUM(CASE
            WHEN mensalidade.pago = 1 THEN plano.valor
            ELSE 0
        END) AS faturamento_recebido
    FROM mensalidade
    JOIN plano
        ON mensalidade.id_plano = plano.id_plano
    """)

    faturamento = cursor.fetchone()

    print(f'Faturamento esperado: R$ {faturamento[0]}')
    print(f'Faturamento recebido: R$ {faturamento[1]}')

    cursor.close()
    conexao.close()