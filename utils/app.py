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

@app.delete('/aluno/{cpf}')
def descadastrar_aluno_api(cpf):

    quantidade = banco_de_dados.descadastrar_aluno(cpf)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='Nenhum aluno encontrado.'
        )
    return {"mensagem": "Aluno removido com sucesso."}

@app.get('/aluno')
def listagem_alunos_api():

    resultado = banco_de_dados.listagem_alunos()

    listagem = resultado[0]
    total = resultado[1]

    alunos = []

    for aluno in listagem:
        alunos.append({
            "id_aluno": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2],
            "cpf": aluno[3],
            "telefone": aluno[4],
            "id_plano": aluno[5]
        })

    return {
        "total": total,
        "alunos": alunos
    }
@app.get('/aluno/pesquisa-id/{id_aluno_informado}')
def pesquisa_aluno_id_api(id_aluno_informado: int):

    resultado = banco_de_dados.pesquisa_aluno_id(id_aluno_informado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail='Nenhum aluno encontrado.'
        )
    return {"mensagem": "Aluno removido com sucesso."}   

@app.get('/aluno/pesquisa-aluno-nome/{nome_informado}')
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

    quantidade = banco_de_dados.descadastrar_professor(cpf_professor)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='Professor não encontrado.'
        )

    return {'Mensagem': 'Professor descadastrado com sucesso.'}

@app.get('/professor')
def listagem_professor_api():

    resultado = banco_de_dados.listagem_professor()

    listagem = resultado[0]
    total = resultado[1]

    professores = []

    for professor in listagem:
        professores.append({
            "id_professor": professor[0],
            "nome": professor[1],
            "idade": professor[2],
            "cpf": professor[3],
            "especialidade": professor[4]
        })

    return {
        "total": total,
        "professores": professores
    }

@app.get('/professor/prequisa-professor-id/{id_informado}')
def pesquisa_professor_id_api(id_informado: int):

    resultado = banco_de_dados.pesquisa_professor_id(id_informado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail='Professor não encontrado.'
        )
    return resultado

@app.get('professor/pesquisa-professor-nome{nome_informado}')
def pesquisa_professor_nome(nome_informado: str):

    resultado = banco_de_dados.pesquisa_professor_nome(nome_informado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail='Professor não encontrado.'
        )

    return resultado 

#######################################################################
# Mensalidade:

class Mensalidade(BaseModel):
    nome_plano: str = Field(min_length=3)
    valor: int

@app.get('/mensalidade/status-financeiro{ìd_aluno}')
def verificacao_status_financeiro_api(id_aluno: int):

    resultado = banco_de_dados.verificacao_status_financeiro(id_aluno)

    if resultado == 0:
        raise HTTPException(
            status_code=404,
            detail='Não conseguimos verificar as informações do aluno.'
        )

    if resultado[3] == 1:
        status = 'Pago'
    else:
        status = 'Pendente'

    return {
        "nome_plano": resultado[1],
        "valor": resultado[2],
        "status": status
    }