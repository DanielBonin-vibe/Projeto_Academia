from Projeto_Academia.utils import banco_de_dados

class Academia:                  

    def __init__(self):
        ...
###########################################
# Cadastros:

    def matricular_aluno(self, nome, idade, cpf, id_plano):    
        banco_de_dados.cadastro_aluno(nome, idade, cpf, id_plano)
        print('Matrícula concluída com sucesso.')

    def desmatricular_aluno(self, id_aluno):
        banco_de_dados.descadastrar_aluno(id_aluno)

    def cadastrar_professor(self, nome, idade, cpf, especialidade):
        banco_de_dados.cadastro_professor(nome, idade, cpf, especialidade)
        print('Professor cadastrado com sucesso.')

    def desmatricular_professor(self, cpf_professor):
        banco_de_dados.descadastrar_professor(cpf_professor)
        print('Remoção do professor concluída.')

###################################################
# Ações:

    def listar_alunos(self):
        banco_de_dados.listagem_alunos()

    def buscar_aluno_id(self, id_aluno_informado):
        banco_de_dados.pesquisa_aluno_id(id_aluno_informado)
        
    def buscar_aluno_nome(nome_informado):
        banco_de_dados.pesquisa_aluno_nome(nome_informado)

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
        print('2 - Buscar aluno pela matrícula')
        print('3 - Buscar aluno pelo nome')
        print('4 - Cadastrar professor')
        print('5 - Buscar professor pelo ID')
        print('6 - Buscar professor pelo nome')
        print('7 - Descadastrar professor')
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

        
        