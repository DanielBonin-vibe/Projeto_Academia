from repositories import alunos_repository, planos_repository

def cadastro_aluno_service(nome, idade, cpf, id_plano):
    if nome is None or not nome.strip():
        return 'Preencha o campo nome.'

    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'

    if idade is None:
        return 'Preencha o campo idade.'

    if id_plano is None:
        return 'Preencha o campo plano'

    if idade < 14:
        return 'Não é possível cadastrar um aluno menor de 14 anos.'
    

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is not None:
        return 'CPF já cadastrado.'


    plano = planos_repository.buscar_plano(id_plano)

    if plano is None:
        return 'Plano não encontrado.'


    resultado = alunos_repository.cadastro_aluno(nome, idade, cpf, id_plano)

    if resultado == 0:
        return 'Erro ao realizar o cadastro.'

    return 'Cadastro realziado com sucesso.'


def listar_aluno_service():
    alunos, total = alunos_repository.listar_alunos()

    if total == 0:
        return 'Nada a listar.'

    return alunos, total


def buscar_aluno_service(cpf):
    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'Não foi possível localizar o CPF informado.'

    return aluno 

def alterar_plano_service(cpf, id_plano):

    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'


    plano = planos_repository.buscar_plano(id_plano)

    if plano is None:
        return 'Plano não encontrado.'


    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'Não foi possível localizar nenhum aluno com o CPF informado.'


    resultado = alunos_repository.alterar_plano(cpf, id_plano)

    if resultado == 0:
        return 'Não foi possível alterar o plano.'

    return resultado


def excluir_aluno_service(cpf):
    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'Não foi possível localizar o CPF infromado.'


    mensalidade = alunos_repository.mostrar_mensalidade(cpf)

    if mensalidade:
        return 'È necessário realizar o pagamento de mensalidades pendentes.'
    

    resultado = alunos_repository.excluir_aluno(cpf)

    if resultado == 0:
        return 'Não foi possível realizado a exclusão do aluno.'

    return 'Exclusão concluída com sucesso.'


def mostrar_mensalidade_service(cpf):
    if cpf is None or not cpf.strip():
        return 'Preencha o campo CPF.'

    aluno = alunos_repository.buscar_aluno(cpf)

    if aluno is None:
        return 'Não foi possível localizar o aluno vinulado a este CPF.'

    resultado = alunos_repository.mostrar_mensalidade(cpf)

    if not resultado:
        return 'Não foi possivel localizar nenhuma mensalidade.'

    return resultado