from utils import banco_de_dados

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
# Coordenador

    def listar_alunos(self):
        banco_de_dados.listagem_alunos()

    def buscar_aluno_id(self, id_aluno_informado):
        banco_de_dados.pesquisa_aluno_id(id_aluno_informado)
        
    def buscar_aluno_nome(nome_informado):
        banco_de_dados.pesquisa_aluno_nome(nome_informado)

    def listar_professores(self):
        banco_de_dados.listagem_professor()

    def buscar_professor_id(self, id_informado):
        banco_de_dados.pesquisa_professor_id(id_informado)

    def buscar_professor_nome(self, nome_informado):
        banco_de_dados.pesquisa_professor_nome(nome_informado)

###################################################################
# Aluno
    def verificar_status_financeiro(self, cpf):
        resultado = banco_de_dados.verificacao_status_financeiro(cpf)
        print(resultado)



        
        