from database.conexao_postgre import conectar

def aluno_plano():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT id_plano FROM alunos
        """)

        resultado = cursor.fetchall()

        if resultado:
            conexao.commit()
            return resultado

        conexao.r

    except Exception as erro:
        conexao.rollback()