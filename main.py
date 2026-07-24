from models import Professor, Mensalidade, Academia, Aluno


mensalidade = Mensalidade(200)
academia = Academia()
academia.cadastrar_aluno('Bonin', 20, 70939995492, 'Plus')
academia.cadatsrar_professor('Daniel', 'Musculação')


#################################################################
# Alunos:

    if opcao == @:
        lista_alunos = academia.listar_alunos()                       # Cria a  variavel 'lista_alunos' sendo igual ao chamamento da função listar_alunos

        if len(lista_alunos) == 0:                                    # Se o tamanho do que for escrito for 0, já retorne que n existe
            print('Nenhum aluno encontrado') 

        else:                                                         # Se for mairo que 0:
            for aluno in lista_alunos:                                # Para aluno na variavel 'lista_alunos'
                print(aluno)                                          # Retorna todos os alunos, já que é um laço de reptição


    if opcao == @:
        academia.cadastrar_aluno(nome, idade, cpf, plano)             #  Quero revisar esse cadastro Depois
        print('Aluno cadastrado com sucesso')                         # 

    if opcao == @:
        academia.remover_aluno(cpf)                                   # Revisar
        print('Aluno Removido')

    if opcao == @:
            academia.buscar_aluno(cpf)
            print(f'O {aluno.nome} é listado em nossa academia')

####################################################################
# Professores:

    if opcao == @:
        nova_especialidade = input('Digite a nova especialidade do professor: ')
        professor.alterar_especialidade(nova_especialidade)
        print('Especialidade alterada com sucesso!')

    if opcao == @:
        lista_professores = academia.listar_professores()             # Criamos a variável 'lista_professores' e armazenamos o a função listar_professores()

        for professor in lista_professores                            # Para cada professor na variável que armazena a função listar_professores()
            print(professor)                                          # Retorna todos os professores, já que é um laço de repetição.
#####################################################################
# Mensalidade:

    if opcao == @:
        mensalidade.realizar_pagamento()
        print('O Pagamento foi realizado.')


    if opcao == @:
        mensalidade.cancelar_pagamento()
        print('O Pagamento foi cancelado.')

    
        