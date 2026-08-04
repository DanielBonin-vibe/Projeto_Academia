from .aluno import Aluno
from .professor import Professor
from .mensalidade import Mensalidade
from .plano import Plano
from utils import persistencia


class Academia:                                 # Classe

    total_alunos = 0                            # Valor inicial do contador
    total_professores = 0

    def __init__(self):
        self.alunos = []
        self.professores = []

    def matricular_aluno(self, nome, idade, cpf, opcao_plano):    

        if opcao_plano == '1':   
            plano = Plano('Básico')                           # Cria o objeto 'Plano' que é aguardado na variável 'plano', esse objeto 'Valor' guarda o valor de acordo com a opcao_plano
            mensalidade = Mensalidade(100)                    # Cria o objeto 'Mensalidade' que guarda o valor '100', que tudo é guardado na variável 'mensalidade'

        elif opcao_plano == '2':
            plano = Plano('intermediário')                    

        elif opcao_plano == '3':        
            plano = Plano('Premium')                           
            mensalidade = Mensalidade(300)

        else: 
            print('Plano Inválido')
            return

        aluno = Aluno(nome, idade, cpf, plano, mensalidade)
        Aluno.total_alunos += 1
        self.alunos.append(aluno)
        persistencia.salavar_aluno(self.alunos)

######################################################

    def desmatricular_aluno(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                self.alunos.remover(aluno)
            else:
                print('Não foi possível encontrar o aluno no nosso banco de dados.')
        return 'Sucesso'                          


    def buscar_aluno(self, cpf):                            
        for aluno in self.alunos:                           
            if aluno.cpf == cpf:                            
                return aluno  
            else:
                print('Não foi possível encontrar o aluno no nosso banco de dados.')
                break

                                
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    def buscar_aluno(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                return aluno

    def listar_professoress(self):
        for professor in self.professores:
            print(professor)

    def cadastrar_professor(self, nome, cpf, especialidade):
        professor = Professor(nome, cpf, especialidade)
        self.professores.append(professor)
        return 'Professor cadastrado'

    def verificar_status_financeiro(self, cpf):
        for aluno in self.alunos:                          # Para cada aluno na lista de alunos
            if aluno.cpf == cpf:                           # Se o cpf informado for igual ao cpf de algum aluno na lista de alunos, faça:

                if aluno.mensalidade.pago:
                    return('Tudo certo!')
                
                else: 
                    return 'Provável Atraso'
                
            else:
                return 'Aluno não encontrado'

    def realizar_pagamento(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                aluno.mensalidade.pago = True
                return 'Tudo pago'
            
        return ('Este CPF não está no nosso banco de dados.')

    def cancelar_pagamento(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                aluno.mensalidade.pago = False
                return 'Pagamento pendente'
            
        return ('Este CPF não está no nosso banco de dados.')

###########################################################################################

    def menu_inicial(self):
        print('=' * 40)
        print('' * 20, 'MENU', ' * 20')
        print('=' * 40)
        print()
        print()
        print('1 - Coordenador ')
        print('2 - Aluno')
        print('0 - Sair')
        return input('Digite a seleção desejada: ')

    def menu_coordenador(self):
        print()
        print('=' * 20, 'MENU COORDENADOR', '=' * 20)
        print()
        print('1 - Listar alunos')
        print('2 - Matricular aluno em nossa unidade')
        print('3 - Desmatricular aluno de nossa unidade')
        print('4 - Buscar matrícula')
        print('5 - Cadastrar professor na unidade')
        print('6 - Listar nossos profissionais')
        return print('Selecione a Opção que você deseja em nossa academia: ')

    def menu_aluno(self):
        print()
        print('=' * 20, 'MENU ALUNO', '=' * 20)
        print()
        print('1 - Buscar sua matrícula')
        print('2 - Conhecer nossos professores')
        print('3 - Pagar mensalidade')
        print('4 - Cancelar pagamento')
        print('5 - Verificar status financeiro')

        return input('Selecione a Opção que você deseja em nossa academia: ') 

    def selecao_plano(self):
        print()
        print('=' * 20, 'SELEÇÃO PLANO', '=' * 20)
        print()
        print('1 - Plano Básico')
        print('2 - Plano Intermediário')
        print('3 - Plano Premium')
        print('4 - Sair')
        print('=' * 40)
        print()
        return input('Digite o plano desejado: ')

        
        