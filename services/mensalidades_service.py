from repositories import mensalidades_repository, alunos_repository, planos_repository
from datetime import date

def registrar_mensalidade_service(cpf):
    if cpf is None or not cpf.strip():
        return 'Preencha o CPF.'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'O CPF informado não está vinculado a nenhum aluno.'

    id_aluno = aluno[0]
    id_plano = aluno[4]

    plano = planos_repository.buscar_plano(id_plano)

    if plano is None:
        return 'O CPF informado não está vinculado a nenhum plano.'

    valor = plano [2]

    hoje = date.today()

    if hoje.day <= 5:
        data_vencimento = date(hoje.year, hoje.month, 5)

    else:
        if hoje.month == 12:
            data_vencimento = date(hoje.year + 1, 1, 5)

        else:
            data_vencimento = date(
                hoje.year,
                hoje.month + 1,
                5
            )

    resultado = mensalidades_repository.registrar_mensalidade(id_aluno, id_plano, valor, data_vencimento)

    if resultado == 0:
        return 'Não foi possível registrar a mensalidade.'

    return 'Mensalidade registrada com sucesso.'




def listar_mensalidades_service(cpf):

    if cpf is None or not cpf.trip():
        return 'Prrencha o campo CPF.'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'O CPF informado não está vinculado a nenhum aluno.'


    resultado = mensalidades_repository.listar_mensalidades(cpf)

    if not resultado:
        return 'Não foi possível listar as mensalidades'

    return resultado

def buscar_pagamento_service(cpf):

    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'O CPF infroma não está vinculado a nenhum aluno.'


    resultado = mensalidades_repository.buscar_pagamento(cpf)

    if not resultado:
        return 'Não foi possível realiazar a busca.'

    return resultado

def consultar_mensalidade_service(cpf, mes, ano):

    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'

    if mes is None:
        return 'Preencha o campo mês.'

    if ano is None:
        return 'Preencha o campo ano.'

    if mes < 1 or 12 > mes:
        return 'Mês inválido'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'O CPF não está vinculado a nenhum aluno.'

    resultado = mensalidades_repository.consultar_mensalidade(cpf, mes, ano)

    if resultado is None:
        return 'Não foi possível consultar nenhuma mensalidade.'

    return resultado
    