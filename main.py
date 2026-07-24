from models import Mensalidade, Academia


mensalidade = Mensalidade(200)
academia = Academia()
academia.cadastrar_aluno('Bonin', 20, 70939995492, 'Plus')
academia.cadatsrar_professor('Daniel', 'Musculação')

while True:

    print('=' * 20, 'MENU', '=' * 20)
    print()
    opcao = print('Selecione a Opção que você deseja em nossa academia: ')
    print()
    print('1 - Listar alunos')
    print('2 - Se Matricular em nossa unidade')
    print('3 - Se desmatricular de nossa unidade')
    print('4 - Buscar sua matrícula')
    print('5 - Conhecer nossos profissionais')
    print('6 - Mudar a especialidade de um profissional')
    print('7 - Pagar a mensalidade do mês')
    print('8 - Cancelar o pagamento do mês')

    if len(opcao) <= 1:
        print('Digite apenas um caractere')
        break
    else:


#################################################################
# Alunos:

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
            academia.remover_aluno(cpf)                                   # Revisar
            print('Aluno Removido')

        if opcao == '4':
                academia.buscar_aluno(cpf)
                print(f'O {aluno.nome} é listado em nossa academia')

    ####################################################################
    # Professores:

        if opcao == '5':
            lista_professores = academia.listar_professores()             # Criamos a variável 'lista_professores' e armazenamos o a função listar_professores()

            for professor in lista_professores:                           # Para cada professor na variável que armazena a função listar_professores(
                print(professor)  

        if opcao == '6':
                nova_especialidade = input('Digite a nova especialidade do professor: ')
                professor.alterar_especialidade(nova_especialidade)
                print('Especialidade alterada com sucesso!')                                        # Retorna todos os professores, já que é um laço de repetição.
    #####################################################################
    # Mensalidade:

        if opcao == '7':
            mensalidade.realizar_pagamento()
            print('O Pagamento foi realizado.')


        if opcao == '8':
            mensalidade.cancelar_pagamento()
            print('O Pagamento foi cancelado.')

    
        