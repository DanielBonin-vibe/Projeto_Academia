from .aluno import Aluno
from .professor import Professor
from .mensalidade import Mensalidade

class Academia:             # Classe
    def __init__(self):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self, nome, idade, cpf, plano):
        aluno = Aluno(nome, idade, cpf, plano)              # Criamos um objeto chamado 'aluno' que recebe uma classe que irá receber os parâmetros
        self.alunos.append(aluno)                           # Damos um append para adicionar o aluno a lista self.alunos

    def remover_aluno(self, cpf):
        for aluno in self.alunos:                           # Para o objeto 'aluno' na lista 'self.alunos' faça: -> Pecorre a lista
            if aluno.cpf == cpf:                            # Se o cpf do objeto for igual ao cpf informado, faça:
                self.alunos.remove(aluno)                   # Remove o objeto 'aluno' da lista 'self.alunos'
                break                          
 
    def buscar_aluno(self, cpf):                            # Buscamos o aluno pelo seu cpf, já que é único
        for aluno in self.alunos:                           # Para o objeto 'aluno' que está na lista 'self.alunos'
            if aluno.cpf == cpf:                            # Se o cpf estiver listado em algum dos objetos 'aluno' for igual ao cpf informado, faça:
                return aluno                                # Retorne o nome que estiver no objeto 'aluno' que foi identificado

    def listar_alunos(self):
        return self.alunos

    def verificar_status_financeiro(self, cpf):
        for aluno in self.alunos:                          # Para cada aluno na lista de alunos
            if aluno.cpf == cpf:    
                                       # Se o cpf informado for igual ao cpf de algum aluno na lista de alunos, faça:
                if aluno.mensalidade.pago == True:
                    return('Tudo certo!')
                else: 
                    return 'Provável Atraso'
                
            else:
                return 'Aluno não encontrado'

                
            
##################################################################################################################################################

    def cadastrar_professor(self, nome, especialidade):
        professor = Professor(nome, especialidade)
        self.professores.append(professor)


    def buscar_professor(self, nome):
        for professor in self.professores:                  # Para o objeto 'professor' que está na lista 'self.professores', faça:
            if professor.nome == nome:                      # Se o nome que estiver no objeto 
                return professor 

    def listar_professores(self):                           # Para o objeto 'professor' na lista 'self.professores', faça: 
        return self.professores                             # Retorna a lista 'self.professores''

        