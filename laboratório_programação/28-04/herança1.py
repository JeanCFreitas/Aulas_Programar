class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    def emitir_som(self):
        print("Som genérico de animal")
        
class cachorro(Animal):
    def emitir_som(self):
        print("Au Au")
    
class gato(Animal):
    def emitir_som(self):
        print("Miau")