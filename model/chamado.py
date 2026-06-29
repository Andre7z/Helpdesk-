class Chamado:
    def __init__(
        self,
        cliente,
        descricao,
        prioridade,
        status='Aberto',
        statusfinal=False
    ):
        self.cliente = cliente
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.statusfinal = statusfinal