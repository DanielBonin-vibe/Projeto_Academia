import json
from models import Aluno
from models import Professor

def salvar_aluno(alunos):

    dados = []

    for aluno in alunos:
        dados.append(aluno.to_dict())    # Estamos criando uma lista de objetos em uma lista de dicionários

    with open('dados/alunos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # 'dados' é o que será salvo, 'arquivo' é aonde será salvo


def salvar_professor(professores):

    dados = []

    for professor in professores:
        dados.append(professor.to_dict())

    with open('dados/professores.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_aluno():

    with open ('dados/alunos.json', 'r', encoding='utf-8') as arquivo: # Abre o arquivo 'alunos.json'
        dados = json.load(arquivo)  # Aqui retorna uma lista de dicionários

    alunos = []                 # Cria um alista vazia

    for aluno in dados:         # Pecorre os dicionários na lista dados
        alunos.append(Aluno.from_dict(aluno))    # Converte cada dicionário em um obejto e adiciona na lista vazia

    return alunos

def carregar_professor():

    with open('dados/professores.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)     # retorna a lista de dicionários

    professores = []

    for professor in dados:
        professores.append(Professor.from_dict(professor))

    return professores
