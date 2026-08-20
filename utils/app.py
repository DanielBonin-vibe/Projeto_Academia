from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from utils import banco_de_dados

app = FastAPI()

# Aluno
class Aluno(BaseModel):
    nome: str = Field(min_lenght=3)
    idade: int = Field(gt=0)
    cpf: str = Field(min_length=11, max_lenght=11)
    id_plano: int = Field(gt=0)

@app.post('/aluno')
def cadastrar_aluno_api(aluno = Aluno):

    banco_de_dados.cadastro_aluno(aluno)

    return {'Mensagem': 'Cadastro realizado com sucesso.'}

@app.delete('/aluno/{id_aluno}')
def descadastrar_aluno_api(id_aluno):

    quantidade = banco_de_dados.descadastrar_aluno(id_aluno)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='Nenhum aluno encontrado.'
        )
    return {"mensagem": "Aluno removido com sucesso."}

@app.get('/aluno')
def listagem_alunos_api():

    listagem = banco_de_dados.listagem_alunos()

    return listagem 

@app.get('/aluno/pesquisa-id/{id_aluno_informado}')
def pesquisa_aluno_id_api(id_aluno_informado: int):

    resultado = banco_de_dados.pesquisa_aluno_id(id_aluno_informado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail='Nenhum aluno encontrado.'
        )
    return {"mensagem": "Aluno removido com sucesso."}   

@app.get('/aluno/pesquisa-nome/{nome_informado}')
def pesquisa_aluno_nome(nome_informado: str):

    resultado = banco_de_dados.pesquisa_aluno_nome(nome_informado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail='Nenhum aluno encontrado.'
        )
    return {'Mensagem': 'Conta removido com isso.'}

#####################################################################
# Professor

class Professor(BaseModel):
    nome: str = Field(min_lenght=3)
    idade: int = Field(gt=0)
    cpf: str = Field(min_lenght=11, max_lenght=11)
    especialidade: str = Field (min_lenght=3)

@app.post('/professor')
def cadastro_professor_api(professor = Professor):

    banco_de_dados.cadastro_professor(professor)

    return {'Mensagem': 'Professor cadastrado com sucesso.'}

@app.delete('/professor/{cpf_professor}')
def descadastrar_professor_api(cpf_professor: str):

    banco_de_dados.descadastrar_professor(cpf_professor)

    return {'Mensagem': 'Professor descadastrado com sucesso.'}

@app.get('/professor')
def listagem_professor_api():

    listagem = banco_de_dados.listagem_professor()

    return listagem

@app.get('/professor/{id_informado}')
def pesquisa_professor_id_api(id_informado: int):

    resultado = banco_de_dados.pesquisa_professor_id(id_informado)

    return resultado 

@app.get('professor/{nome_informado}')
def pesquisa_professor_nome(nome_informado: str):

    resultado = banco_de_dados.pesquisa_professor_nome(nome_informado)

    return resultado 

#######################################################################
# Mensalidade:

class Mensalidade(BaseModel):
    nome_plano: str
    valor: int

@app.get('/mensalidade/{ìd_aluno}')
def verificacao_status_financeiro_api(id_aluno: int):

    resultado = banco_de_dados.verificacao_status_financeiro(id_aluno)

    return resultado
