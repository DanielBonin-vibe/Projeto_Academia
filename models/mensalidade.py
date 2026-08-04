class Mensalidade:
    def __init__(self, valor):
        self.valor = valor
        self.pago = False

    def to_dict(self):
        return {
        'valor': self.valor,
        'pago': self.pago
        }