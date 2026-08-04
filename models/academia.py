from .aluno import Aluno
from .professor import Professor
from .mensalidade import Mensalidade
from .plano import Plano


class Academia:                                 # Classe

    total_alunos = 0                            # Valor inicial do contador
    total_professores = 0

    def __init__(self):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self, nome, idade, cpf, opcao_plano):     # opcao_plano é utiliziado para puxar as opções no main.py

        self.selecao_plano()

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

    @classmethod                                            # MÉTODO DE CLASSE  ; representa a classe inteira
    def total_alunos(cls):
        print(cls.total_alunos)                             

    def remover_aluno(self, cpf):
        for aluno in self.alunos:                           # Para o objeto 'aluno' na lista 'self.alunos' faça: -> Pecorre a lista
            if aluno.cpf == cpf:                            # Se o cpf do objeto for igual ao cpf informado, faça:
                self.alunos.remove(aluno)                   # Remove o objeto 'aluno' da lista 'self.alunos'
                break                          
 
    def buscar_aluno(self, cpf):                            # Buscamos o aluno pelo seu cpf, já que é único
        for aluno in self.alunos:                           # Para o objeto 'aluno' que está na lista 'self.alunos'
            if aluno.cpf == cpf:                            # Se o cpf estiver listado em algum dos objetos 'aluno' for igual ao cpf informado, faça:
                return aluno                                # Retorne o nome que estiver no objeto 'aluno' que foi identificado

    def listar_alunos(self):
        return self.alunos

    def verificar_status_financeiro(self, cpf):
        for aluno in self.alunos:                          # Para cada aluno na lista de alunos
            if aluno.cpf == cpf:                           # Se o cpf informado for igual ao cpf de algum aluno na lista de alunos, faça:

                if aluno.mensalidade.pago:
                    return('Tudo certo!')
                
                else: 
                    return 'Provável Atraso'
                
            else:
                return 'Aluno não encontrado'

                
            
##################################################################################################################################################

    def cadastrar_professor(self, nome, especialidade):
        professor = Professor(nome, especialidade)
        Professor.total_professores += 1
        self.professores.append(professor)


    def buscar_professor(self, nome):
        for professor in self.professores:                  # Para o objeto 'professor' que está na lista 'self.professores', faça:
            if professor.nome == nome:                      # Se o nome que estiver no objeto 
                return professor 

    def listar_professores(self):                           # Para o objeto 'professor' na lista 'self.professores', faça: 
        return self.professores                             # Retorna a lista 'self.professores'

    @classmethod                             # Método de classe  
    def total_professores(cls):              # 'cls' é convenção, == 'classe'
        print(cls.total.professores)
    
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
        print('5 - Listar nossos profissionais')
        print('5 - Mudar a especialidade de um profissional')
        return print('Selecione a Opção que você deseja em nossa academia: ')

    def menu_aluno(self):
        print()
        print('=' * 20, 'MENU ALUNO', '=' * 20)
        print()
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('5 - ')
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

        
        