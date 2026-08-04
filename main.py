from models.academia import Academia
from models.mensalidade import Mensalidade

academia = Academia()

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
        nome = input('Informe o nome completo do profissional a ser adicionado: ')
        cpf = input('Informe o CPF do profissional: ')
        especialidade = input('Informe a especialidade que o mesmo atuará: ')
        academia.cadastrar_professor(nome, cpf, especialidade)
        

    elif opcao_coordenador == '6':
        academia.listar_professores()

#################################################################
# Aluno

    if opcao_aluno == '1':
        cpf = input('Informe o CPF a ser pesquisado: ')
        academia.buscar_aluno(cpf)

    elif opcao_aluno == '2':
        academia.listar_professores()
                                    
    elif opcao_aluno == '3':
        academia.realizar_pagamento(cpf)                            
        
    elif opcao_aluno == '4':
        academia.cancelar_pagamento(cpf)                              

    elif opcao_aluno == '5':
        cpf = input('Informe o cpf da conta em questão: ')
        status = academia.verificar_status_financeiro(cpf) 
        print(status)

    else: 
        break
            