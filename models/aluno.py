from .mensalidade import Mensalidade
from .plano import Plano

class Aluno:
    def __init__(self, nome, idade, cpf, plano):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.plano = plano
        self.status_do_contrato = True
