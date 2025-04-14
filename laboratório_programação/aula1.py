#1.crie uma superclasse funcionario com atributos nome, salario_basico e metodo calcular_salario 
#2. crie uma subclasse gerente com atributo bonus
#3. crie uma subclasse vendedor com atributo comissão e vendas
#4. crie uma subclasse desenvolvedor com atributo nivel_experiencia
#5. Implemente o método calcular_salario de forma diferente em cada subclasse considerando seus atributos especificos

class funcionario:
    def __init__ (self, nome, salario_basico):
        self.nome = nome
        self.salario_basico = salario_basico
    def salário(self):
        print(self.salario_basico)
        
class gerente(funcionario):
    def __init__ (self, nome, salario_basico, bonus):
        super().__init__ (nome, salario_basico)
        self.bonus = bonus
    def salario(self):
        salario = self.salario_basico + self.bonus
        return salario
    
class vendedor(funcionario):
    def __init__ (self, nome, comissão, vendas, salario_basico):
        super().__init__ (nome, salario_basico)
        self.comissão = comissão
        self.vendas = vendas
    def salario(self):
        salario = self.comissão * self.vendas
        return salario

class desenvolvedor(funcionario):
    def __init__ (self, nome, salario_basico, nivel_experiencia):
        super().__init__ (nome, salario_basico)
        self.nivel_experiencia = nivel_experiencia #nivel_experiencia
    def salario(self):
        salario = self.salario_basico * (self.nivel_experiencia/2)
            
        return salario
    
a = gerente("Gui", 3000, 200)
b = vendedor("André", 200, 10, 0)
c = desenvolvedor("J", 100, 200)
print(a.nome,a.salario())
print(b.nome,b.salario())
print(c.nome,c.salario())