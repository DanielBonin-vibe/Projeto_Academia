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