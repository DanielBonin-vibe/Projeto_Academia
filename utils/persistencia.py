import json

def salvar_aluno(alunos):

    dados = []

    for aluno in alunos:
        dados.append(aluno.to_dict())    # Estamos criando uma lista de objetos em uma lista de dicionários

    with open('dados/alunos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # 'dados' é o que será salvo, 'arquivo' é aonde será salvo


