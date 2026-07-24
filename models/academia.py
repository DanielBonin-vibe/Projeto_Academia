class Academia:
    def __init__(self, ):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self, nome, idade, cpf, plano, ativo):
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.cpf_aluno = cpf
        self.plano_aluno = plano
        self.ativo_aluno = ativo

    def remover_aluno(self):

    def buscar_aluno(self):
        cpf_procurado = input('Digite o CPF do aluno procurado: ')

        if cpf_procurado in self.alunos[cpf]:   # Terminar essa linha!
            print(f'Aluno {self.nome} encontrado')

    def listar_alunos(self):
        for aluno in lista_alunos:
            print(aluno)

    def cadastrar_professor(self, nome, especialidade):
        self.nome_prof = nome
        self.especialidade_prof = especialidade 

        