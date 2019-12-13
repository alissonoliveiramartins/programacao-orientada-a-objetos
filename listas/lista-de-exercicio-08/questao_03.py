class Quadrado:
    def __init__ (self, tamanho_do_lado):
        self.tamanho_do_lado= tamanho_do_lado
    
    def mudar_valor_lado(self, mudar_valor):
        self.mudar_valor = mudar_valor
        self.tamanho_do_lado = (mudar_valor)
    
    def retornar_valor_lado (self):
        return self.tamanho_do_lado
    
    def calcular_area(self):
        area = self.tamanho_do_lado * self.tamanho_do_lado
        return area


#TESTE 

x = Quadrado(5)
print(x.retornar_valor_lado())
x.mudar_valor_lado(10)
print(x.retornar_valor_lado())
print(x.calcular_area())