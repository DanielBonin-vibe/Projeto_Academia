from .mensalidade import Mensalidade

class Aluno:
    def __init__(self, nome, idade, cpf, plano, mensalidade):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.plano = plano
        self.mensalidade = mensalidade 
        self.status_do_contrato = True
        

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Plano: {self.plano.nome_plano}')
              
        if self.status_do_contrato:
            print('Status: Ativo')
        else: 
            print('Status: Desativado')

    def desativar(self):
        self.status_do_contrato = False
        print('Aluno desativado!')

    def ativar(self):

        if self.mensalidade.pago:                       # Verifica se a mensalidade do aluno está paga.
            self.status_de_contrato = True              # Ativa o contrato do aluno caso a mensalidade esteja em dia.
            print('Aluno Ativo')

        else:
            print('Não é possível ativar o aluno. Mensalidade pendente.')



        
