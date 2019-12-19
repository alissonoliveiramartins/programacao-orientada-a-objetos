class Macaco:
    def __init__ (self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
    
    def mostrar_nome(self):
        print(self.nome)
    
    def comer(self, comida):
        self.bucho.append(comida)
        
    def ver_bucho (self):
        print(self.bucho)
    
    def digerir(self):
        del self.bucho[0]

 
#Faça um programa ou teste interativamente...
resposta = 1
while resposta >= 0:
    escolhido = 0
    
    print('\nVAMOS LÁ !\n')
    
    print('VOCÊ ACABOU DE GANHAR DOIS MACACOS !\n\t DIVIRTASE!')
    nome= input('De um nome ao macaco canibal:\n')
    estomago= input('Diga qual alimento o seu macaco canibal tem no bucho:\n')
    bucho= []
    bucho.append(estomago)
    macaco= Macaco(nome,bucho)
    
    nome2= input('De um nome ao macaco comum:\n')
    estomago2= input('Diga qual alimento o seu macaco comum tem no bucho:\n')
    bucho2= []
    bucho2.append(estomago2)
    macaco2= Macaco(nome2,bucho2)
    
    
    while resposta != 0:
        print('\n',('-'*75))
        print('Digite o que deseja fazer com seu Macaco:\n DAR COMIDA(1)\n PERGUNTAR O NOME DELE(2)\n VER O ESTOMAGO DELE(3)\n DIGERIR (4)\n')
        print('Ver o que aconteceu com os macacos e Comecar com outro macaco (0)')
        print('Encerrar o programa(-1)')
        print('-'*75)
        resposta= int(input())
        
        if resposta <= 0:
            break
        
        escolhido = int(input('QUAL DOS MACACOS ?\t CANIBAL (1)\t COMUM(2):\n'))
        
        if escolhido == 1 :
            
            if resposta == 1:
                comida = input('DIGITE A COMIDA DO MACACO {}:\n'.format(macaco.nome.upper()))
                macaco.comer(comida)
                
            elif resposta == 2:
                 macaco.mostrar_nome()
                 
            elif resposta == 3:
                print('BUCHO: ')
                macaco.ver_bucho()
                
            elif resposta == 4:
                macaco.digerir()

        if escolhido == 2:
            
            if resposta == 1:
                comida = input('DIGITE A COMIDA DO MACACO :\n'.format(macaco.nome.upper()))
                macaco2.comer(comida)
                
            elif resposta == 2:
                 macaco2.mostrar_nome()
                 
            elif resposta == 3:
                print('BUCHO: ')
                macaco2.ver_bucho()
                
            elif resposta == 4:
                macaco2.digerir()
    
    if len(macaco.bucho) > len(macaco2.bucho):
        print('Parabens você cuidou muito bem dos macacos!')
        
    else:
        macaco.comer(macaco2)
        
        print(f'\aOps... Parece que você não alimentou o {macaco.nome.upper()} e ele acabou comendo {macaco2.nome.upper()}' )
        print('Olhe o bucho do seu macaco :') 
        macaco.ver_bucho()
        
          
    
