class Carro:
    def __init__ (self,velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        nova = self.velocidade_atual + delta
        if nova <= self.velocidade_maxima:
            self.velocidade_atual = nova
        else:
            self.velocidade_atual = 180

        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        if nova < 0:
            self.velocidade_atual= 0
        else:
            self.velocidade_atual = nova
        
        return self.velocidade_atual
    

if __name__ == '__main__':
    #Velocidade Maxima
    c1 = Carro(180)

#    for _ in range(25):
#        print(c1.acelerar(8),'km')

 #   for _ in range(10):
 #       print(c1.frear(20),'km')

    def menu(tam=20):
        me = ['ACELERAR','FREAR']
        print('='*tam)
        print('Menu'.upper().center(tam, '_'))

        for i in range(len(me)):
            print('{} => {}'.format(i+1, me[i]))
            
        print('='*tam)

    op = 1    
    while 1 <= op <= 2:
        menu(30)
        op = int(input(' > '))
        if op == 1:
            for _ in range(25):
                print(c1.acelerar(8),'km')
        
        elif op == 2:
            for _ in range(10):
                print(c1.frear(20),'km')


