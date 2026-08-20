from utils import banco_de_dados

class Academia:                  

###########################################
# Cadastros:

    def matricular_aluno(self, nome, idade, cpf, id_plano):    
        banco_de_dados.cadastro_aluno(nome, idade, cpf, id_plano)
        print('Matrícula concluída com sucesso.')

    def desmatricular_aluno(self, cpf):
        banco_de_dados.descadastrar_aluno(cpf)
        print('Desmatricula concluída.')

    def cadastrar_professor(self, nome, idade, cpf, especialidade):
        banco_de_dados.cadastro_professor(nome, idade, cpf, especialidade)
        print('Professor cadastrado com sucesso.')

    def desmatricular_professor(self, cpf_professor):
        banco_de_dados.descadastrar_professor(cpf_professor)
        print('Remoção do professor concluída.')

###################################################
# Coordenador

    def listar_alunos(self):
        listagem, = banco_de_dados.listagem_alunos()
        print(listagem)

    def buscar_aluno_id(self, id_aluno_informado):
        resultado = banco_de_dados.pesquisa_aluno_id(id_aluno_informado)
        print(resultado)
        
    def buscar_aluno_nome(nome_informado):
        listagem = banco_de_dados.pesquisa_aluno_nome(nome_informado)
        print(listagem)

    def listar_professores(self):
        resultado = banco_de_dados.listagem_professor()
        print(resultado)

    def buscar_professor_id(self, id_informado):
        resultado = banco_de_dados.pesquisa_professor_id(id_informado)
        print(resultado)

    def buscar_professor_nome(self, nome_professor_informado):
        resultado = banco_de_dados.pesquisa_professor_nome(nome_professor_informado)
        print(resultado)

###################################################################
# Aluno
    def verificar_status_financeiro(self, cpf):
        resultado = banco_de_dados.verificacao_status_financeiro(cpf)
        print(resultado)



        
        