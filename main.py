from models.academia import Academia
from relatorios import validacao
from utils import menus

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
            id_aluno = input('Informe o ID da sua conta: ')
            academia.verificar_status_financeiro(id_aluno)
        elif opcao_aluno == 2:
            id_aluno = input('Informe o seu ID: ')
            academia.desmatricular_aluno(id_aluno)
        else:
            break

    elif opcao_inicial == 3:

        opcao_coordenador = academia.menu_coordenador()

        if opcao_coordenador == 1:
            academia.listar_alunos()

        elif opcao_coordenador == 2:
            id_aluno_informado = input('Informe o ID do aluno: ')
            academia.buscar_aluno_id(id_aluno_informado)
            
        elif opcao_coordenador == 3:
            nome_informado = input('Informe o nome recordado: ')
            academia.buscar_aluno_nome(nome_informado)

        elif opcao_coordenador == 4:
            academia.listar_professores

        elif opcao_coordenador == 5:
            nome = input('Informe o nome completo do professor: ')
            idade = int(input('Informe a idade do professor: '))
            cpf = input('Informe o CPF do professor(Sem pontuação): ')
            especialidade = input('Informe a especialidade do professor: ')
            academia.cadastrar_professor(nome, idade, cpf, especialidade)

        elif opcao_coordenador == 6:
            id_informado = input('Informe o ID do professor: ')
            academia.buscar_professor_id(id_informado)

        elif opcao_coordenador == 7:
            nome_informado = input('Informe o nome recordado: ')
            academia.buscar_professor_nome(nome_informado)

        elif opcao_coordenador == 8:
            cpf_professor = input('Informe o CPF do professor a ser removido: ')
            academia.desmatricular_professor(cpf_professor)
        else:
            break

    elif opcao_inicial == 4:
        acesso = validacao.senha()

        if acesso:
            opcao_relatorio = menus.menu_relatorios()

            if opcao_relatorio == 1:
                opcao_relatorio_aluno = menus.menu_relatorio_aluno()

                if opcao_relatorio_aluno == 1:
                    ...
                elif opcao_relatorio_aluno == 2:
                    ...
                elif opcao_relatorio_aluno == 3:
                    ...
                elif opcao_relatorio_aluno == 4:
                    ...

            elif opcao_relatorio == 2:
                opcao_relatorio_professor = menus.menu_relatorio_professor()

                if opcao_relatorio_professor == 1:
                    ...
                elif opcao_relatorio_professor == 2:
                    ...
                elif opcao_relatorio_professor == 3:
                    ...
                elif opcao_relatorio_professor == 4:
                    ...

        
            elif opcao_relatorio == 3:
           
                opcao_relatorio_mensalidade = menus.menu_relatorio_mensalidade()

                if opcao_relatorio_mensalidade == 1:
                    ...
                elif opcao_relatorio_mensalidade == 2:
                    ...
                elif opcao_relatorio_mensalidade == 3:
                    ...
                
        else:
            print('Acesso negado.')

    else:
        break