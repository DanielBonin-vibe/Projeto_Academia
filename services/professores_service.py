from repositories import professores_repository


def cadastrar_professor_service(nome, idade, cpf, especialidade):

    if nome is None or not nome.strip():
        return 'Preencha o campo "Nome".'

    if idade is None:
        return 'Preencha o campo "Idade".'

    if cpf is None or not cpf.strip():
        return 'Preencha o campo "CPF".'

    if especialidade is None or not especialidade.strip():
        return 'Preencha o campo "Especialidade".'

    if idade < 18:
        return 'Nossos professores devem ser maiores de idade.'

    professor = professores_repository.buscar_professor(cpf)

    if professor is not None:
        return 'O CPF já está cadastrado.'

    resultado = professores_repository.cadastrar_professor(
        nome,
        idade,
        cpf,
        especialidade
    )

    if resultado == 0:
        return 'Não foi possível cadastrar o professor.'

    return resultado


def listar_professores_service():

    resultado = professores_repository.listar_professores()

    if resultado == 0:
        return 'Não foi possível listar os professores.'

    return resultado


def buscar_professor_service(cpf):

    if cpf is None or not cpf.strip():
        return 'Preencha o campo "CPF".'

    resultado = professores_repository.buscar_professor(cpf)

    if resultado is None:
        return 'Não foi possível localizar o professor.'

    return resultado


def alterar_professor_service(id_professor, nome, idade, cpf, especialidade):

    if id_professor is None:
        return 'Preencha o campo "ID Professor".'

    if nome is None or not nome.strip():
        return 'Preencha o campo "Nome".'

    if idade is None:
        return 'Preencha o campo "Idade".'

    if cpf is None or not cpf.strip():
        return 'Preencha o campo "CPF".'

    if especialidade is None or not especialidade.strip():
        return 'Preencha o campo "Especialidade".'

    if idade < 18:
        return 'Nossos professores devem ser maiores de idade.'

    resultado = professores_repository.alterar_professor(
        id_professor,
        nome,
        idade,
        cpf,
        especialidade
    )

    if resultado == 0:
        return 'Não foi possível alterar as informações do professor.'

    return resultado


def excluir_professor_service(cpf):

    if cpf is None or not cpf.strip():
        return 'Preencha o campo "CPF".'

    professor = professores_repository.buscar_professor(cpf)

    if professor is None:
        return 'O CPF informado não está vinculado a nenhum professor.'

    resultado = professores_repository.excluir_professor(cpf)

    if resultado == 0:
        return 'Erro ao remover professor.'

    return resultado