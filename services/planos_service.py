from repositories import planos_repository, alunos_repository

def cadastro_plano_service(nome_plano, valor):

    if nome_plano is None or not nome_plano.strip():
        return 'Preencha o campo nome plano.'

    if valor is None:
        return 'Preencha o campo valor.'

    if valor <= 0:
        return 'O valor é inválido.'

    plano = planos_repository.buscar_plano(nome_plano, valor)

    if plano is None:
        return 'Erro ao retornar os planos.'

    resultado = planos_repository.cadastro_plano(nome_plano, valor)

    if resultado == 0:
        return 'Não foi possível realizar o cadastro'

    return 'Plano cadastrado com sucesso.'


def listar_planos_service():

    resultado = planos_repository.listar_planos()

    if not resultado:
        return 'Não foi possível realizar a listagem.'

    return resultado

def buscar_plano_service(id_plano):

    if id_plano is None:
        return 'Preencha o campo ID plano.'

    resultado = planos_repository.buscar_plano(id_plano)

    if resultado is None:
        return 'Não foi possível buscar o plano.'

    return resultado

def alterar_plano_service(id_plano, cpf):

    if id_plano is None:
        return 'Peeencha o campo ID plano.'

    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'


    plano = planos_repository.buscar_plano(id_plano)

    if plano is None:
        return ' Plano não encontrado.'


    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'Aluno não encontrado.'
    

    resultado = planos_repository.alterar_plano(id_plano, cpf)

    if resultado == 0:
        return 'Não foi possível alterar o plano.'

    return resultado

def excluir_plano_service(id_plano):
    if id_plano is None:
        return 'Preencha o campo ID plano.'

    plano = planos_repository.buscar_plano(id_plano)

    if plano is None:
        return 'Não foi possível localizar o ID plano.'


    resultado = planos_repository.excluir_plano(id_plano)

    if resultado == 0:
        return 'Não foi possível excluir o plano.'
    
    return resultado