from linked_list import *
import subprocess

class Item_Menu:
    def __init__(self, name:str, description:str, quote:float):
        self.name=name
        self.desp=description
        self.pric=quote

    def display_item(self):
        width_win=subprocess.run(["tput","cols"],capture_output=True,text=True)
        width_win=width_win.stdout.strip()
        print("="*int(width_win))
        print("Nome do produto: {}\nDescrição: {}\nPreco: {}".format(self.name,self.desp,self.pric))

class Menu:
    def __init__(self):
        default_values=[Item_Menu("pizza","e uma pizza muito gostosa",10),Item_Menu("xtudo","um podrao da pessada",30),Item_Menu("cerebro de macaco","macaco",40),Item_Menu("salada para idiotas","e uma salada normal, so coloquei porque SIM",1)]
        self.menu=Linked_List()
        for i in default_values:
            self.menu.insert(i)
    def display_itens(self):
        self.menu.go_init()
        print(self.menu.head.prev.value.display_item())
        while not self.menu.in_end():
            print(self.menu.get_value().display_item())

class Wish:
    def __init__(self, cliente:"cliente", itens_pedido:"itemcardapio", status:str):
        self._cliente = cliente
        self._itens_pedido = itens_pedido
        self._status = status

        def exibir_detalhes(self):
            print("d")

class customer:
    def __init__(self, nome:str, telefone:str):
        self._nome = nome
        self._telefone = telefone

        def exibir_detalhes(self):
            print("d")

if "__main__" == __name__:
    test=Menu()
    test.display_itens()
