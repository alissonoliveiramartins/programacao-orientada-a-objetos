class Tamagotchi:
    
    def __init__ (self, nome):
        self.nome = nome
        self.fome = 10
        self.saude = 10
        self.idade = 0
        
    def alterar_nome (self, novo_nome):
        self.nome = novo_nome
    
    def retornar_fome(self):
        return self.fome
        
    def retornar_saude(self):
        return self.saude
        
    def retornar_idade(self):
        return self.idade
    
    def comer(self):
        if self.fome > 0:
            self.fome -= 1
    
    def tomar_injecao(self):
        if self.saude < 10:
            self.saude += 1
        
    def envelhecer(self):
        if self.saude > 0:
            self.saude -= 1 
        self.idade += 1
  
"""  
#TESTE            
x= Tamagotchi('Alisson')
x.comer()
print(x.retornar_fome())
print(x.saude)
x.envelhecer()
print(x.retornar_saude())
x.tomar_injecao()
print(x.retornar_saude())
"""
            