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

    return {'Mensagem': 'Cadastro realizado com sucesso'}

@app.delete('/aluno/{id_aluno}')
def descadastrar_aluno_api(id_aluno):

    banco_de_dados.descadastrar_aluno(id_aluno)

    return {'Mensagem': 'aluno descadastrado com sucesso.'}

@app.get('/aluno')
def listagem_alunos_api():

    listagem = banco_de_dados.listagem_alunos()

    return listagem 

@app.get('/aluno/{id_aluno_informado}')
def pesquisa_aluno_id_api(id_aluno_informado):

    resultado = banco_de_dados.pesquisa_aluno_id(id_aluno_informado)

    return resultado