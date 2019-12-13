class Caneta:
    def __init__ (self, cor, marca, numero_ponta, volume_tinta=50):
        self.cor = cor 
        self.marca  = marca
        self.numero_ponta = numero_ponta
        self.volume_tinta = volume_tinta
    
    def encher_caneta(self):
        self.volume_tinta = 50
    
    def escrever(self, texto):
        self.texto  = texto
        print(texto)
        self.volume_tinta -= 1

    def retornar_marca(self):
        return self.marca
    
    def imprimir_caracteristicas(self):
        print(self.cor, self.marca, self.numero_ponta, self.volume_tinta)



x = Caneta('azul','big','0.7')
x.escrever('alisson oliveira')
x.encher_caneta()
x.imprimir_caracteristicas()
