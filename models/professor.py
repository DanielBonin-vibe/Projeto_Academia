
class Professor:
    def __init__(self, nome, cpf, especialidade):
        self.nome = nome
        self.cpf = cpf
        self.especialidade = especialidade

    def exibir_dados(self):
        print(f'Nome do professor: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Especialidade do professor: {self.especialidade}')

    def to_dict(self):
        return {
        'nome': self.nome, 
        'cpf': self.cpf,    
        'especialidade': self.especialidade
        }

    @classmethod
    def from_dict(cls, dados):  # Ensina a montar o objeto novamente 

        professor = cls(      
        dados['nome'],
        dados['cpf'],
        dados['especialidade']
        )

        return professor
        