from Projeto_Academia.utils import banco_de_dados

class Academia:                  

    def __init__(self):
###########################################
# Cadastros:

    def matricular_aluno(self, nome, idade, cpf, id_plano):    
        banco_de_dados.cadastro_aluno(nome, idade, cpf, id_plano)

    def desmatricular_aluno(self, cpf):
        ...  

    def cadastrar_professor(self, nome, idade, cpf, especialidade):
        banco_de_dados.cadastro_professor(nome, idade, cpf, especialidade)

    def desmatricular_aluno(self, cpf):
        ...

###################################################
# Ações:

    def listar_alunos(self):
        ...
    def buscar_aluno(self, cpf):
        ...
    def listar_professores(self):
        ...
    def verificar_status_financeiro(self, cpf):
        ...
    def realizar_pagamento(self, cpf):
        ...
###########################################################################################

    def menu_inicial(self):
        print('=' * 40)
        print('' * 20, 'ACADEMIA', ' * 20')
        print('=' * 40)
        print()
        print('1 - Matricular-se em nossa academia')
        print('2 - Acesso Aluno ')
        print('3 - Acesso Coordenador')
        print('0 - Sair')
        return int(input('Digite a seleção desejada: '))

    def menu_coordenador(self):
        print()
        print('=' * 20, 'MENU COORDENADOR', '=' * 20)
        print()
        print('1 - Listar alunos')
        print('2 - Buscar matrícula')
        print('3 - Cadastrar professor')
        print('4 - Buscar professor')
        return int(input('Selecione a opção desejada: '))

    def menu_aluno(self):
        print()
        print('=' * 20, 'MENU ALUNO', '=' * 20)
        print()
        print('1 - Buscar sua matrícula')
        print('2 - Pagar mensalidade')
        print('3 - Verificar status financeiro')
        print('4 - Desmatricular-se da nossa academia')
        return int(input('Selecione a opção desejada: '))

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

        
        