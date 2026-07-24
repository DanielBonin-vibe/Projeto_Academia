class Mensalidade:
    def __init__(self, valor):
        self.valor = valor
        self.pago = True

    def realizar_pagamento(self):
        self.pago = True

    def cancelar_pagamento(self):
        self.pago = False