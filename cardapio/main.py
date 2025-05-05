class itemcardapio:
    def __init__(self, nome:str, descrição:str, preço:float):
        self._nome = nome
        self._descrição = descrição
        self._preço = preço

    def exibir_detalhes(self):
        print (f"d")

class Pedido:
    def __init__(self, cliente:"cliente", itens_pedido:"itemcardapio", status:str):
        self._cliente = cliente
        self._itens_pedido = itens_pedido
        self._status = status

        def exibir_detalhes(self):
            print("d")

class cliente:
    def __init__(self, nome:str, telefone:str):
        self._nome = nome
        self._telefone = telefone

        def exibir_detalhes(self):
            print("d")

if "__main__" == __name__:
    True