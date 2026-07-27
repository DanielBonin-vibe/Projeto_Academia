class Plano:
    def __init__(self, nome_plano):
        self.nome_plano = nome_plano
      

    while True:
        print()
        print('=' * 20, 'SELEÇÃO PLANO', '=' * 20)
        print()
        print('1 - Plano Básico')
        print('2 - Plano Intermediário')
        print('3 - Plano Premium')
        print('4 - Sair')
        print('=' * 40)
        opcao = input('Digite o plano desejado: ')

        if opcao == '1':
            mensalidade = 100
            nome_plano = 'Básico'

            plano = Plano('Básico')
            mensalidade = Mensalidade(100)
            


        elif opcao == '2':
            mensalidade = 200
            nome_plano = 'intermediário'

            plano = Plano('Intermediário')
            mensalidade =  Mensalidade(200)

        elif opcao == '3':
            mensalidade = 300
            nome_plano = 'Premium'

            plano = Plano('Premium')
            mensalidade = Mensalidade(300)
        else:
            print('Saindo...')
            break

