class Macaco:
    
    def __init__ (self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
    
    def mostrar_nome(self):
        print('Meu nome é {}'.format(self.nome))
    
    def comer(self, comida):
        self.bucho.append(comida)
        
    def ver_bucho (self):
        print(self.bucho)
    
    def digerir(self):
        self.bucho = []

 
#Faça um programa ou teste interativamente...
resposta = 1
while resposta > 0:
    nome= input('De um nome ao macaco:\n')
    estomago= input('Diga qual alimento o seu macaco tem no bucho:\n')
    bucho= []
    bucho.append(estomago)
    macaco= Macaco(nome,bucho)
    
    
    while resposta != 0:
        print('\n')
        print('Digite o que deseja fazer com seu Macaco\n DAR COMIDA(1),\n PERGUNTAR O NOME DELE(2),\n VER O ESTOMAGO DELE(3)')
        print('Comecar com outro macaco digie ZERO(0)')
        print('Encerrar o programa dite MENOS UM(-1)')
        resposta= int(input())
        
        if resposta == 1:
            comida = input('DIGITE A COMIDA DO MACACO:\n')
            macaco.comer(comida)
            
        elif resposta == 2:
             macaco.mostrar_nome()
             
        elif resposta == 3:
            macaco.ver_bucho()
        
        elif resposta < 0:
            break 
            
    if resposta < 0:
        break