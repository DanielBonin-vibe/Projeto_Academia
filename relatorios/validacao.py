from utils import menus, banco_de_dados

def senha():
    senha_administrador = 'Boni180506'
    contagem = 0

    while contagem < 3:
        tentativa = input('Informe a senha do administrador: ')

        if tentativa == senha_administrador:
            print('Acesso autorizado.')
            return True
        else:
            contagem += 1
            print('Senha incorreta.')

    print('Número máximo de tentativas atingido.')
    return False

######################################################################
while True:
    opcao_relatorio = menus.menu_relatorios()

    if opcao_relatorio == 1:
        opcao_relatorio_aluno = menus.menu_relatorio_aluno()

        if opcao_relatorio_aluno == 1:
            banco_de_dados.relatorio_aluno_padrao()
        elif opcao_relatorio_aluno == 2:
            banco_de_dados.relatorio_aluno_nome_ordem_alfabetica()
        elif opcao_relatorio_aluno == 3:
            banco_de_dados.relatorio_aluno_media_idade()
        elif opcao_relatorio_aluno == 4:
            banco_de_dados.relatorio_aluno_plano()

    elif opcao_relatorio == 2:
        opcao_relatorio_professor = menus.menu_relatorio_professor()

        if opcao_relatorio_professor == 1:
            banco_de_dados.relatorio_professor_padrao()
        elif opcao_relatorio_professor == 2:
            banco_de_dados.relatorio_professor_nome_ordem_alfabetica()
        elif opcao_relatorio_professor == 3:
            banco_de_dados.relatorio_professor_media_idade()
        elif opcao_relatorio_professor == 4:
            banco_de_dados.relatorio_professor_especialidade()

        
    elif opcao_relatorio == 3:
        opcao_relatorio_mensalidade = menus.menu_relatorio_mensalidade()

        if opcao_relatorio_mensalidade == 1:
            banco_de_dados.relatorio_mensalidade_media()
        elif opcao_relatorio_mensalidade == 2:
            banco_de_dados.relatorio_mensalidade_situacao()
        elif opcao_relatorio_mensalidade == 3:
            banco_de_dados.relatorio_mensalidade_faturamento()