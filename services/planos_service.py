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

