from services import alunos_service, professores_service, planos_service, mensalidades_service
from repositories import relatorios_repository
from menus import menu_principal, menu_alunos, menu_planos, menu_mensalidades, menu_professores, menu_relatorios

while True:
    opcao_principal = menu_principal()

    if opcao_principal == 1:
        opcao_alunos = menu_alunos()

        if opcao_alunos == 1:
            nome = input('Informe o nome compelto do novo aluno: ')
            idade = int(input('Informe a idade do aluno: '))
            cpf = input('Informe o CPF do novo aluno: ')
            id_plano = int(input('Informe o ID do plano escolhido: '))
            resultado = alunos_service.cadastro_aluno_service(nome, idade, cpf, id_plano)
            print(resultado)
        elif opcao_alunos == 2:
            resultado = alunos_service.listar_aluno_service()
            print(resultado)
        elif opcao_alunos == 3:
            cpf = input('Informe o CPF do aluno a ser buscado: ')
            resultado = alunos_service.buscar_aluno_service(cpf)
            print(resultado)
        elif opcao_alunos == 4:
            cpf = input('Informe o CPF do aluno em questão: ')
            id_plano = int(input('Informe o ID do novo plano: '))
            resultado = alunos_service.alterar_plano_service(cpf, id_plano)
            print(resultado)
        elif opcao_alunos == 5:
            cpf = input('Informe o CPF do aluno a ser removido da academia: ')
            resultado = alunos_service.excluir_aluno_service(cpf)
            print(resultado)
        elif opcao_alunos == 6:
            cpf = input('Informe o CPF do aluno em questão: ')
            resultado = alunos_service.mostrar_mensalidade_service(cpf)
            print(resultado)
        else:
            break
        

    elif opcao_principal == 2:
        opcao_planos = menu_planos()

    elif opcao_principal == 2:
        opcao_planos = menu_planos()

        if opcao_planos == 1:
            nome_plano = input('Informe o nome do novo plano: ')
            valor = float(input('Informe o valor do plano: '))
            resultado = planos_service.cadastro_plano_service(nome_plano, valor)
            print(resultado)

        elif opcao_planos == 2:
            resultado = planos_service.listar_planos_service()
            print(resultado)
        elif opcao_planos == 3:
            id_plano = int(input('Informe o ID do plano que deseja buscar: '))
            resultado = planos_service.buscar_plano_service(id_plano)
            print(resultado)
        elif opcao_planos == 4:
            id_plano = int(input('Informe o ID do plano que deseja alterar: '))
            cpf = input("Informe o novo CPF do aluno: ")
            resultado = planos_service.alterar_plano_service(id_plano, cpf)
            print(resultado)
        elif opcao_planos == 5:
            id_plano = int(input("Informe o ID do plano que deseja excluir: "))
            resultado = planos_service.excluir_plano_service(id_plano)
            print(resultado)
        else:
            break


    elif opcao_principal == 3:
        opcao_mensalidades = menu_mensalidades()

        if opcao_mensalidades == 1:
            cpf = input('Informe o CPF do aluno: ')
            resultado = mensalidades_service.registrar_mensalidade_service(cpf)
            print(resultado)
        elif opcao_mensalidades == 2:
            cpf = input('Informe o CPF do aluno: ')
            resultado = mensalidades_service.listar_mensalidades_service(cpf)
            print(resultado)
        elif opcao_mensalidades == 3:
            cpf = input('Informe o CPF do aluno: ')
            resultado = mensalidades_service.buscar_pagamento_service(cpf)
            print(resultado)
        elif opcao_mensalidades == 4:
            cpf = input('Informe o CPF do aluno: ')
            mes = int(input('Informe o mês da mensalidade: '))
            ano = int(input('Informe o ano da mensalidade: '))
            resultado = mensalidades_service.consultar_mensalidade_service(cpf, mes, ano)
            print(resultado)
        else:
            break

    elif opcao_principal == 4:
        opcao_professores = menu_professores()

        if opcao_professores == 1:
            nome = input('Informe o nome do professor: ')
            idade = int(input('Informe a idade do professor: '))
            cpf = input('Informe o CPF do professor: ')
            especialidade = input('Informe a especialidade do professor: ')
            resultado = professores_service.cadastrar_professor_service(nome, idade, cpf, especialidade)
            print(resultado)
        elif opcao_professores == 2:
            resultado = professores_service.listar_professores_service()
            print(resultado)
        elif opcao_professores == 3:
            cpf = input('Informe o CPF do professor que deseja buscar: ')
            resultado = professores_service.buscar_professor_service(cpf)
            print(resultado)
        elif opcao_professores == 4:
            id_professor = input('Informe o CPF do professor que deseja alterar: ')
            nome = input('Informe o novo nome do professor: ')
            idade = int(input('Informe a nova idade do professor: '))
            especialidade = input('Informe a nova especialidade do professor: ')
            resultado = professores_service.alterar_professor_service(id_professor, nome, idade, especialidade)
            print(resultado)
        elif opcao_professores == 5:
            cpf = input('Informe o CPF do professor que deseja excluir: ')
            resultado = professores_service.excluir_professor_service(cpf)
            print(resultado)
        else:
            break

    elif opcao_principal == 5:
        opcao_relatorios = menu_relatorios()

        if opcao_relatorios == 1:
            opcao_relatorios_alunos = menu_relatorios_alunos()

            if opcao_relatorios_alunos == 1:
                resultado = relatorios_repository.alunos_plano()

                print(resultado)

            elif opcao_relatorios_alunos == 2:
                resultado = relatorios_repository.ordem_alfabetica_alunos()

                print(resultado)

            elif opcao_relatorios_alunos == 3:
                resultado = relatorios_repository.alunos_mensalidades_pendentes()

                print(resultado)

            elif opcao_relatorios_alunos == 4:
                resultado = relatorios_repository.quantidade_alunos_plano()

                print(resultado)

        elif opcao_relatorios == 2:
            opcao_relatorios_financeiros = menu_relatorios_financeiros()

            if opcao_relatorios_financeiros == 1:
                resultado = relatorios_repository.receital_total()

                print(resultado)

            elif opcao_relatorios_financeiros == 2:
                resultado = relatorios_repository.receital_periodo()

                print(resultado)

            elif opcao_relatorios_financeiros == 3:
                resultado = relatorios_repository.mensalidades_pagas()

                print(resultado)

            elif opcao_relatorios_financeiros == 4:
                resultado = relatorios_repository.mensalidades_pendentes()

                print(resultado)

            elif opcao_relatorios_financeiros == 5:
                resultado = relatorios_repository.total_pendente()

                print(resultado)

        elif opcao_relatorios == 3:
            opcao_relatorios_professores = menu_relatorios_professores()

            if opcao_relatorios_professores == 1:
                resultado = relatorios_repository.ordem_alfabetica_professores()

                print(resultado)

            elif opcao_relatorios_professores == 2:
                resultado = relatorios_repository.professor_especialidade()

                print(resultado)

        elif opcao_relatorios == 4:
            opcao_relatorios_mensalidades = menu_relatorios_mensalidades()

            if opcao_relatorios_mensalidades == 1:
                resultado = relatorios_repository.mensalidades_mes()

                print(resultado)

            elif opcao_relatorios_mensalidades == 2:
                resultado = relatorios_repository.mensalidades_pagas()

                print(resultado)

            elif opcao_relatorios_mensalidades == 3:
                resultado = relatorios_repository.mensalidades_pendentes()

                print(resultado)

            elif opcao_relatorios_mensalidades == 4:
                resultado = relatorios_repository.percentual_inadimplencia()

                print(resultado)

    else:
        break
