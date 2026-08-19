import sqlite3

conexao = sqlite3.connect('database/academia.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno(
    id_aluno INTERGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTERGER NOT NULL,
    cpf TEXT NOT NULL,
    id_plano TEXT NOT NULL,

    FOREIGN KEY(id_plano) REFERENCES plano(id_plano))
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mensalidade(
    id_mensalidade INTERGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTERGER NOT NULL,
    id_plano INTERGER NOT NULL,
    pago INTERGER NOT NULL DEFAULT 0,

    FOREIGN KEY(id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY(id_plano) REFERENCES plano(id_plano))
""") #'id_aluno' será uma chave estrangeira, que referencia a coluna 'id-aluno' da tabela aluno

cursor.execute("""
CREATE TABLE IF NOT EXISTS professor(
    id_professor INTERGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTERGET NOT NULL,
    cpf TEXT NOT NULL,
    especialidade TEXT NOT NULL)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS plano(
    id_plano INTERGER PRIMARY KEY AUTOINCREMENT,
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
# Relatórios:


