class Mensalidade:
    def __init__(self, valor):
        self.valor = valor
        self.pago = False

    def to_dict(self):
        return {
        'valor': self.valor,
        'pago': self.pago
        }

    def from_dict(cls, dados):
        return cls (
        dados['valor'],
        dados['pago']
        )