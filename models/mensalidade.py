class Mensalidade:
    def __init__(self, valor):
        self.valor = valor
        self.pago = False

    def realizar_pagamento(self):
        self.pago = True
        return "Tudo pago"

    def cancelar_pagamento(self):
        self.pago = False
        return "Pagamento pendente"


    def to_dict(self):
        return {
        'valor': self.valor,
        'pago': self.pago
        }