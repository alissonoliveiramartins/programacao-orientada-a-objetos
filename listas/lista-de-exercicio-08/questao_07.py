class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, ano):
        self.idade += ano
        if self.idade < 21:
            self.altura += 0.5
        
    def engordar(self, mais_peso):
        self.peso += mais_peso
    
    def emagrecer (self, menos_peso):
        self.peso -= menos_peso
    
    def crescer(self, mais_altura):
        self.altura += mais_alura
 
""" 
#TESTE        
x= Pessoa('alisson',18 , 75, 1.68)
x.envelhecer(2)
print(x.idade)
print(x.altura)
x.emagrecer(1)
print(x.peso)
x.engordar(2)
print(x.peso)
"""