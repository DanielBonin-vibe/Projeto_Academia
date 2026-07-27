from models import Mensalidade, Academia


mensalidade = Mensalidade(200)
academia = Academia()
academia.cadastrar_aluno('Bonin', 20, 70939995492, 'Plus')
academia.cadatsrar_professor('Daniel', 'Musculação')

while True:

    print('=' * 40)
    print('' * 20, 'MENU', ' * 20')
    print('=' * 40)
    print()
    opcao_inicial = input('Digite a seleção desejada')
    print()
    print('1 - Coordenador ')
    print('2 - Aluno')
    print('0 - Sair')

    if opcao_inicial == '1': 
        print('=' * 20, 'MENU ADMIN', '=' * 20)
        print()
        opcao = print('Selecione a Opção que você deseja em nossa academia: ')
        print()
        print('1 - Listar alunos')
        print('2 - Matricular aluno em nossa unidade')
        print('3 - Desmatricular aluno de nossa unidade')
        print('4 - Buscar matrícula')
        print('5 - Listar nossos profissionais')
        print('5 - Mudar a especialidade de um profissional')


    elif opcao_inicial == '2':
         lista_alunos_inicial = academia.listar_alunos()
         cpf = input('Informe seu CPF: ')

         if lista_alunos_inicial.cpf == cpf:
              print('=' * 40)
              print('=' * 20, 'MENU ALUNO', '=' * 20)
              print('=' * 40)
              print()
              print()
              print('7 - Buscar sua matrícula')
              print('8 - Conhecer nossos profissionais')
              print('9 - Pagar mensalidade do mês')
              print('10 - Cancelar o pagamento da mensalidade do mês')


         

    if len(opcao) <= 2:
        print('Digite no máximo 2 caracteres')
        break
    else:


#################################################################
# Coordenador

        if opcao == '1':
            lista_alunos = academia.listar_alunos()                       # Cria a  variavel 'lista_alunos' sendo igual ao chamamento da função listar_alunos

            if len(lista_alunos) == 0:                                    # Se o tamanho do que for escrito for 0, já retorne que n existe
                print('Nenhum aluno encontrado') 

            else:                                                         # Se for mairo que 0:
                for aluno in lista_alunos:                                # Para aluno na variavel 'lista_alunos'
                    print(aluno)                                          # Retorna todos os alunos, já que é um laço de reptição


        if opcao == '2':
                      
            nome = input('Digite o nome completo do aluno a ser cadastrado: ')
            idade = input('Digite a idade do aluno: ')
            cpf = input('Digite o CPF do novo aluno: ')
            plano = input('Informe o plano do novo aluno: ')

            academia.cadastrar_aluno(nome, idade, cpf, plano)  

            print('Aluno cadastrado com sucesso')                          

        if opcao == '3':
            academia.remover_aluno(cpf)                                   
            print('Aluno Removido')

        if opcao == '4':
            academia.buscar_aluno(cpf)
            print(f'O {aluno.nome} é listado em nossa academia')

        elif opcao == '5':
                    lista_professores = academia.listar_professores()             # Criamos a variável 'lista_professores' e armazenamos o a função listar_professores() do objeto academia
        
                    for professor in lista_professores:                           # Para cada professor na variável que armazena a função 'listar_professores()'
                        print(professor)  

        if opcao == '6':
            nova_especialidade = input('Digite a nova especialidade do professor: ')         # Criamos um variável e damos um valor a ela
            professor.alterar_especialidade(nova_especialidade)                              # Chama o método alterar_especialidade() do objeto professor, passando a nova especialidade para atualizar a área de atuação do professor.
            print('Especialidade alterada com sucesso!')       

        elif opcao == '7':
            cpf = input('Informe o cpf da conta em questão: ')                     # Criamos a varrávelq ue vai receber o cpf da conta a ser verificada
            status = academia.verificar_status_financeiro(cpf)                     # Criamos status para guardar o valor da função 'verificar_status...' do objeto academia
            print(status)                                                          # Retornamos um texto informando a situação 
                                            

        

    ####################################################################
    # Professores:

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
            