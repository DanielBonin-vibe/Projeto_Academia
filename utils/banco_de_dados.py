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
    pago INETRGER NOT NULL DEFAULT 0,

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
#####################################################################
# Cadastros:

def cadastro_aluno(nome, idade, cpf, id_plano):
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO aluno(nome, idade, cpf, id_plano)
    VALUES(?, ?, ?, ?)
    """, (nome, idade, cpf, id_plano))

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
    conexao =  sqlite3.connect('database/academia.db')
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
def planos():
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""

    """)


def cadastrar_aluno():
    conexao =  sqlite3.connect('database/academia.db')
    cursor = conexao.cursor()

    cursor.execute("""

    """)

