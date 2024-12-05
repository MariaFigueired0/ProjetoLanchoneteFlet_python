class Produto:

    def __init__(self, parCod, parDescricao, parPreco, parQtd):
        self.cod=parCod
        self.descricao=parDescricao
        self.preco=parPreco
        self.qtd=parQtd

    def listar(self):
        print(  f" Cod: {self.cod}"+
                f" | Produto: {self.descricao[:20]:<20}"
                f" | Preço: {self.preco}"+
                f" | Qtd: {self.qtd}")

    def alterar(self, descricao, preco, quantidade):
        self.descricao=descricao
        self.preco=preco
        self.qtd=quantidade