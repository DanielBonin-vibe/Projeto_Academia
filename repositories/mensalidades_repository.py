from database.conexao_postgre import conectar

def registrar_mensalidade(id_aluno, id_plano, valor, data_vencimento):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO (id_aluno, id_plano, valor, data_vencimento)
        VALUES (%s, %s, %s, %s)
        """, (id_aluno, id_plano, valor, data_vencimento))

        resultado = cursor.rowcount

        if resultado > 0:
            conexao.commit()
            return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao registrar mensalidade: {erro}.')
        return 0

    finally:
        cursor.close()
        conexao.close()