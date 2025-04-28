# Abstrata

from abc import ABC, abstractmethod

class formageometica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class retangulo(formageometica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class circulo(formageometica):
    def __init__(self,raio):
        self.raio = raio
    def calcular_area(self):
        import math
        return math.pi * self.raio**2
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.raio

ret = retangulo(5, 10)
circ = circulo(7)

print(f"Area do retângulo: {ret.calcular_area()}")
print(f"Perimetro do circulo: {circ.calcular_perimetro()}")