from data_struct.linked_list import *
import subprocess

class Item_Menu:
    def __init__(self, name:str, description:str, quote:float)->None:
        self.name=name
        self.desp=description
        self.pric=quote

    def display_item(self)->None:
        width_win=subprocess.run(["tput","cols"],capture_output=True,text=True)
        width_win=int(width_win.stdout.strip())

        space=(width_win-len(self.name))//2
        print("~"*space,end='')
        print(self.name,end='')
        print("~"*space,end='')
        print("Description: {}\nPrice: {}".format(self.desp,self.pric))

class Menu:
    def __init__(self)->None:
        default_values=[Item_Menu("PIZZA","e uma pizza muito gostosa",10),Item_Menu("XTUDO","um podrao da pessada",30),Item_Menu("CEREBRO DE MACACO","macaco",40),Item_Menu("SALADA PARA IDIOTAS","e uma salada normal, so coloquei porque SIM",1)]
        self.menu=Linked_List()
        for i in default_values:
            self.menu.insert_at_index(i,-1)
        self.menu.go_init()
    def get_index_item(self,name_item:str)->int:
        temp=self.menu.init
        index=0
        while temp!=self.menu.last:
            if not temp.value:
                continue
            if temp.value.name==name_item or temp == None:
                break
            temp=temp.next
            index+=1
        if (temp == self.menu.last and temp.value!=name_item) or temp == None:
            return -1
        return index
    def add_item(self,item:"Item_Menu")->None:
        new_item=item
        if self.get_index_item(item.name) != -1:
            print("We can't add a exist item...")
            return
        self.menu.insert_at_index(new_item,-1)
        self.menu.go_init()
    def remove_item(self,name_item:str):
        if (res:=self.get_index_item(name_item)) == -1:
            return
        print(self.menu.head.value.name)
        self.menu.remove_at_index(res)
        self.menu.go_init()

    def display_itens(self):
        self.menu.go_init()
        while not self.menu.in_end():
            self.menu.head.value.display_item()
            self.menu.forward()
        self.menu.head.value.display_item()

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
    tst=Menu()
    tst.remove_item("CEREBRO DE MACACO")
    tst.add_item(Item_Menu("Tralaleo Tralala","shark",700))
    tst.display_itens()
