import subprocess
class Item_Menu:
    def __init__(self,name:str,description:str,price:float)->None:
        self.name=name.upper()
        self.desc=description
        self.price=price
    def display_item(self)->None:
        width_win=subprocess.run(["tput","cols"],capture_output=True,text=True)
        width_win=int(width_win.stdout.strip())
        space=(width_win-len(self.name)-len(self.desc)-len(str(self.price)))//2

        print(self.name,end=" "*space)
        print(self.desc,end=" "*space)
        print(self.price)
class Menu:
    def __init__(self)->None:
        self.menu={}
        default_values=[Item_Menu("PIZZA","e uma pizza muito gostosa",10),Item_Menu("XTUDO","um podrao da pessada",30),Item_Menu("CEREBRO DE MACACO","macaco",40),Item_Menu("SALADA PARA IDIOTAS","e uma salada normal, so coloquei porque SIM",1)]
        for i in default_values:
            self.add_item(i)

    def find_item(self,name_item:str)->bool:
        return (name_item.upper() in self.menu.keys())
    def add_item(self,item:"Item_Menu")->None:
        item.name=item.name.upper()
        if self.find_item(item.name):
            print("This item already exist")
            return
        self.menu[item.name]=item
    def get_item(self,name_item:str)->"Item_Menu":
        name_item=name_item.upper()
        if not self.find_item(name_item):
            print("This item doens't exist")
            return
        return self.menu[name_item]
    def rmv_item(self,name_item:str)->None:
        name_item=name_item.upper()
        if not self.find_item(name_item):
            print("This item doens't exist")
            return
        del self.menu[name_item]

    def display_menu(self)->None:
        for i in self.menu.keys():
            item=self.menu[i]
            print("{} | ".format(item.name),end='')
        print("\nThere's {} item in total".format(len(self.menu.keys())))
class Wish:
    def __init__(self,customer:"Custumer"):
        self.list={}
        self.customer=customer
        self.status="active"
    def atribute_customer(self,customer:"Customer"):
        self.customer=customer

    def add_item(self,menu_ref:"Menu",name_item:str,amount:int)->None:
        if not menu_ref.find_item(name_item):
            print("This item doesn't exist in our menu")
            return

        if (name_item in self.list.keys()):
            self.list[name_item]+=amount
            return
        self.list[name_item]=amount
    def rmv_item(self,item_name:str)->None:
        if (item_name in self.list.keys()):
            del self.list[item_name]
            return
        print("This item doesn't exist in out menu")
    def calc_tot(self,menu_ref:"Menu"):
        tot=0
        for i in self.list.keys():
            item=menu_ref.get_item(i)
            tot+=item.price*self.list[i]
        return tot
    def display_infos(self,menu_ref:"Menu"):
        print("Request by {} | {}".format(self.customer.name,self.status))
        for i in self.list.keys():
            item=menu_ref.get_item(i)
            item.display_item()

        width_win=subprocess.run(["tput","cols"],capture_output=True,text=True)
        width_win=int(width_win.stdout.strip())
        print("~"*width_win)
        for j in self.list.keys():
            print("{} x {} ".format(j,self.list[i]))

class Customer:
    def __init__(self,name:str,cellphone:str,wish:"Wish")->None:
        self.name=name
        self.phone=cellphone
        self.wish=wish
    def atribute_wish(self,wish:"Wish"):
        self.wish=wish
    def display_person(self):
        width_win=subprocess.run(["tput","cols"],capture_output=True,text=True)
        width_win=int(width_win.stdout.strip())

        space=width_win-len(self.name)-len(self.phone)
        print(self.name,end='')
        print(" "*space,end='')
        print(self.phone,end='')

        print("~"*width_win)
        if not self.wish :
            print("Empty queue")
            return
        for i in self.wish.list.keys():
            print("{}x{} ".format(i,self.wish.list[i]))
    def finish_wish(self):
        self.wish=None

if __name__=="__main__":
    menu=Menu()
    customer=Customer("Mary",123456789,Wish(None))
    customer.wish.atribute_customer(customer)

    some_products=["pizza","xtudo","cerebro de macaco"]
    for i in some_products:
        customer.wish.add_item(menu,i,1)
    customer.wish.display_infos(menu)
    print(customer.wish.calc_tot(menu))
    customer.finish_wish
