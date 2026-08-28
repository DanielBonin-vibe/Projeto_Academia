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

    resultado = alunos_repository.registrar_mensalidade(id_aluno, id_plano, valor, data_vencimento)

    if resultado == 0:
        return 'Não foi possível registrar a mensalidade.'