import random
import time #Biblioteca do tempo.


ganha=['7','11']
continua= ['4','5','6','8','9','10']
perde = ['2','3','12']

meta_ponto= 0
situacao= ''
novo_ponto=0

numero1 = random.randint(1,6)
numero2 = random.randint(1,6)
ponto = numero1 + numero2
meta_ponto = ponto
print('='*25)
print('1º DADO : ({}) DADO : ({})'.format(numero1,numero2))
print('SEU PONTO É :',ponto)
if str(ponto) in ganha:
    print('"Natural" VOCÊ GANHOU !')
    print('='*25)
    
elif str(ponto) in continua:
    print('"PONTO"')
    print('='*25)
            
    while meta_ponto != novo_ponto:        
        numero1 = random.randint(1,6)
        numero2 = random.randint(1,6)
        novo_ponto = numero1 + numero2
        x = time.sleep(0.4)
        print('1º DADO: ({}) 2º DADO: ({})'.format(numero1,numero2))
        print('SOMA = {}\n'.format(novo_ponto))
        
        if novo_ponto == meta_ponto:
            print("VOCE GANHOU!")
        elif novo_ponto == 7:
            print('VOCE PERDEU!')
            break
        else:
            continue
        
elif str(ponto) in perde:
    print('"CRAPS" VOCÊ PERDEU !')
    print('='*25)
    
          
            
