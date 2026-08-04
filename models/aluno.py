from .mensalidade import Mensalidade
from .plano import Plano

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

    def to_dict(self):
        return {
        'nome': self.nome, 
        'idade': self.idade,
        'cpf': self.cpf,
        'plano': self.plano.to_dict(),
        'mensalidade': self.mensalidade.to_dict(),
        'status_do_contrato': self.status_do_contrato
        }

    @classmethod
    def from_dict(cls, dados):   # Mesma coisa de fazer Aluno.from_dict(Aluno)
        plano = Plano.from_dict(dados['plano'])
        mensalidade = Mensalidade.from_dict(dados['mensalidade'])

        aluno = cls(    # Criamos um novo objeto chamado Aluno
        dados['nome'],
        dados['idade'],
        dados['cpf'],
        plano,
        mensalidade
        )

        return aluno

        
