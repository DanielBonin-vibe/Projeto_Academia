def menu_inicial(self):
    print('=' * 40)
    print('' * 20, 'ACADEMIA', ' * 20')
    print('=' * 40)
    print()
    print('1 - Matricular-se em nossa academia')
    print('2 - Acesso Aluno ')
    print('3 - Acesso Coordenador')
    print('4 - Relatórios')
    print('0 - Exit')
    return int(input('Digite a seleção desejada: '))

def menu_coordenador(self):
    print()
    print('=' * 20, 'MENU COORDENADOR', '=' * 20)
    print()
    print('1 - Listar alunos')
    print('2 - Buscar aluno pela matrícula')
    print('3 - Buscar aluno pelo nome')
    print('4 - Listar professores')
    print('5 - Cadastrar professor')
    print('6 - Buscar professor pelo ID')
    print('7 - Buscar professor pelo nome')
    print('8 - Descadastrar professor')
    print('0 - Exit')
    return int(input('Selecione a opção desejada: '))

def menu_aluno(self):
    print()
    print('=' * 20, 'MENU ALUNO', '=' * 20)
    print()
    print('1 - Verificar status financeiro')
    print('2 - Desmatricular-se da nossa academia')
    print('0 - Exit')
    return int(input('Selecione a opção desejada: '))

def selecao_plano(self):
    print()
    print('=' * 20, 'SELEÇÃO PLANO', '=' * 20)
    print()
    print('1 - Plano Básico')
    print('2 - Plano Interprise')
    print('3 - Plano Deluxe')
    print('0 - Sair')
    print('=' * 40)
    print()
    return input('Digite o plano desejado: ')

def menu_relatorios(self):
    print()
    print('=' * 50)
    print('=' * 20, 'RELATÓRIOS', '=' * 20)
    print('=' * 50)
    print('1 - Relatório dos alunos')
    print('2 - Relatório dos professores')
    print('3 - Relatório das mensalidades')
    print('4 - Relatório dos planos')

def menu_relatorio_aluno():
    print()
    print('=' * 50)
    print('=' * 20, 'RELATÓRIO DOS ALUNOS', '=' * 20)
    print('=' * 50)
    print('1 - Relatório padrão (Por ID)')
    print('2 - Relatório de nomes em ordem alfabética')
    print('4 - Relatório por média de idade')
    print('5 - Relatório por plano')
    print('6 - Exit')
    return 'Informe a ação requerida'

def menu_relatorio_professor():
    print()
    print('=' * 50)
    print('=' * 20, 'RELATÓRIO DOS PROFESSORES', '=' * 20)
    print('=' * 50) 
    print()
    print('1 - Relatório padrão (Por ID)')
    print('2 - Relatório de nomes em ordem alfabética') 
    print('3 - Relatório por média de idade') 
    print('4 - Relatório por especialidade')
    print('5 - Exit') 
    return 'Informe a ação requerida'

def menu_relatorio_mensalidade():
    print()
    print('=' * 50)
    print('=' * 20, 'RELATÓRIO DAS MENSALIDADES', '=' * 20)
    print('=' * 50) 
    print()
    print('1 - Relatório por média de mensalidade')
    print('2 - Relatório por mensalidade paga/pendente')
    print('3 - Relatório de faturamento')
    print('4 - Exit')
    return 'Informe a ação requerida'
