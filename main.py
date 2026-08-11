from models.academia import Academia


academia = Academia()

while True:
    
    opcao_inicial = academia.menu_inicial()

    if opcao_inicial == 1:
        nome = input('Informe o seu nome completo: ')
        idade = int(input('Informe a sua idade: '))
        cpf = input('Informe o seu CPF(Sem pontuação): ')
        id_plano = academia.selecao_plano()
        academia.matricular_aluno(nome, idade, cpf, id_plano)

    elif opcao_inicial == 2:
        opcao_aluno = academia.menu_aluno()

        if opcao_aluno == 1:
            ...
        elif opcao_aluno == 2:
            ...
        elif opcao_aluno == 3:
            ...
        elif opcao_aluno == 4:
            ...
    elif opcao_inicial == 3:
        opcao_coordenador = academia.menu_coordenador()

        if opcao_coordenador == 1:
            ...
        elif opcao_coordenador == 2:
            nome = input('Informe o nome completo do professor: ')
            idade = int(input('Informe a idade do professor: '))
            cpf = input('Informe o CPF do professor(Sem pontuação): ')
            especialidade = input('Informe a especialidade do professor: ')
            academia.cadastrar_professor(nome, idade, cpf, especialidade)
            
        elif opcao_coordenador == 3:
            ...
        elif opcao_coordenador == 4:
            ...