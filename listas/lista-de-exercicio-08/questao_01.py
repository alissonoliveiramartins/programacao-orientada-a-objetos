class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor= cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cornova):
        self.cor = cornova

    def mostrar_cor(self):
        print(self.cor)

"""
#TESTE    
x= Bola('amarelo', '25', 'plastico')
x.mostrar_cor()

x.trocar_cor('azul')
x.mostrar_cor()
"""