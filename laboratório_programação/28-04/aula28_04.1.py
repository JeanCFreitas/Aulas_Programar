class calculadora:
    def somar(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c
        
calc = calculadora()
print(calc.somar(2, 3))
print(calc.somar(2, 3, 4))