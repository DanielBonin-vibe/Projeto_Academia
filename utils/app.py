from fastapi import FastAPI
from pydantic import BaseModel
from utils import banco_de_dados

app = FastAPI()

# Aluno
class Aluno(BaseModel):
    nome: str
    idade: int
    cpf: str
    id_plano: int

@app.post('/aluno')
def cadastrar_aluno_api(aluno = Aluno):

    banco_de_dados.cadastro_aluno(aluno)

    return {'Mensagem': 'Cadastro realizado com sucesso.'}

@app.delete('/aluno/{id_aluno}')
def descadastrar_aluno_api(id_aluno):

    banco_de_dados.descadastrar_aluno(id_aluno)

    return {'Mensagem': 'Aluno descadastrado com sucesso.'}

@app.get('/aluno')
def listagem_alunos_api():

    listagem = banco_de_dados.listagem_alunos()

    return listagem 

@app.get('/aluno/{id_aluno_informado}')
def pesquisa_aluno_id_api(id_aluno_informado):

    resultado = banco_de_dados.pesquisa_aluno_id(id_aluno_informado)

    return resultado

@app.get('/aluno/{nome_informado}')
def pesquisa_aluno_nome(nome_informado):

    aluno = banco_de_dados.pesquisa_aluno_nome(nome_informado)

    return aluno

#####################################################################
# Professor

class Professor(BaseModel):
    nome: str
    idade: int
    cpf: str
    especialidade: str

@app.post('/professor')
def cadastro_professor_api(professor = Professor):

    banco_de_dados.cadastro_professor(professor)

    return {'Mensagem': 'Professor cadastrado com sucesso.'}

@app.remove('/professor/{cpf_professor}')
def descadastrar_professor_api(cpf_professor):

    banco_de_dados.descadastrar_professor(cpf_professor)

    return {'Mensagem': 'Professor descadastrado com sucesso.'}

@app.get('/professor')
def listagem_professor_api():

    listagem = banco_de_dados.listagem_professor()

    return listagem

@app.get('/professor/{id_informado}')
def pesquisa_professor_id_api(id_informado):

    banco_de_dados.pesquisa_professor_id