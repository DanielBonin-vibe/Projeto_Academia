class Aluno:
    def __init__(self, nome, idade, cpf, plano, ativo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.plano = plano
        self.ativo = True

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Plano: {self.plano}')
        print(f'Status: {self.ativo}')

    def desativar(self):
        self.ativo = False
        print('Aluno desativado!')
