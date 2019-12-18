class Retangulo:
    
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def mudar_valor_lado(self, novo_lado_a, novo_lado_b):
        self.novo_lado_a = novo_lado_a
        self.novo_lado_b = novo_lado_b
        
    def retornar_valor_lado(self):
        return self.lado_a, self.lado_b
        
    def calcular_area(self):
        self.area = self.lado_a * self.lado_b
        return self.area
        
    def calcular_perimetro(self):
        self.perimetro = (self.lado_a + self.lado_b) * 2
        return self.perimetro
        
base = int(input('Informe uma das medidas em metros : '))
altura = int(input('Informe a outra medida em metros : '))

retangulo = Retangulo(base, altura)      
piso = retangulo.calcular_area()
rodape = retangulo.calcular_perimetro()
print(f'Sera necessarios {piso}m² quadrados para o piso.')  
print(f'Sera necessarios {rodape/2}m² quadrados para o rodapé.')