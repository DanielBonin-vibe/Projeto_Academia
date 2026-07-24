import Aluno

class Professor:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def exibir_dados(self):
        print(f'Nome do professor: {self.nome}')
        print(f'Especialidade do professor: {self.especialidade}')

    def alterar_especialidade(self, especialidade):      # Especialidade recebe um valor que estará no main.py
        self.especialidade = especialidade               # self.especialidade é o atributo que pertence ao objeto
        