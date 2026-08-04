from models import Mensalidade, Academia


mensalidade = Mensalidade(200)
academia = Academia()
academia.cadastrar_aluno('Bonin', 20, 70939995492, 'Plus')
academia.cadatsrar_professor('Daniel', 'Musculação')

while True:
    
    opcao_inicial = academia.menu_inicial()

    if opcao_inicial == '1':
         opcao_coordenador = academia.menu_coordenador()

    elif opcao_inicial == '2':
         opcao_aluno = academia.menu_aluno()

    else:
         break
    

#########################################################################################################
# Coordenador
    if opcao_coordenador == '1':
        academia.listar_alunos()

    elif opcao_coordenador == '2':
        nome = input('Informe o nome compelto do novo aluno: ')
        idade = input('Informe a idade: ')
        cpf = input('Informe o CPF (Sem pontuação): ')
        opcao_plano = academia.selecao_plano()
        academia.matricular_aluno(nome, idade, cpf, opcao_plano)  
            
    elif opcao_coordenador == '3':
        cpf = input('Informe o CPF (Sem pontuação): ')
        academia.desmatricular_aluno(cpf)

    elif opcao_coordenador == '4':
        cpf = input('Informe o CPF (Sem pontuação): ')
        academia.buscar_aluno(cpf)

    elif opcao_coordenador == '5':
        academia.listar_professores()

#################################################################
# Aluno

        elif opcao == '8':       # Buscar sua matrícula
            academia.buscar_aluno(cpf)
            print(f'O {aluno.nome} está vinculado a esse  cpf')

        elif opcao == '9':
            lista_professores = academia.listar_professores()             # Criamos a variável 'lista_professores' e armazenamos o a função listar_professores()

            for professor in lista_professores:                           # Para cada professor na variável que armazena a função listar_professores(
                print(professor)  
                                    
        elif opcao == '10':
            mensalidade.realizar_pagamento()                              # Do objeto 'mensalidade.' chamamos a função 'realizar_pagamento()'
            print('O Pagamento foi realizado.')
        
        elif opcao == '11':
            mensalidade.cancelar_pagamento()                              # Do objeto 'mensalidade.' chamamos a função 'cancelar_pagamento()'
            print('O Pagamento foi cancelado.')

        elif opcao == '11':
            cpf = input('Informe o cpf da conta em questão: ')
            status = academia.verificar_status_financeiro(cpf) 
            print(status)

        else:
            break
            