import random
nome = [ 'Alisson','Maria','João','Davi','Bruna','Sara','Layse','Felipe','Andrey','Eduarda','Italo','Jonantan','Nara','Candeia','Liliane','Amanda','Anderson','Stefany','Elizete','Gabriele']
sobrenome = ['Paz','Lopes','Park','Oliveira','Martins','Arruda','Silva','Coltinho','Datena''Vidal','Mota','Lobos','Lopes','Arantes','Barroso','Santana','Sales','Barreto','Galvão','Simão','Barata']
nome_completo=[]

quantidade = int(input('Digite a quantidade de nomes aleatorios: \n'))

while quantidade > 0:
    quantidade -= 1 
    ind_nome= random.randint(0,len(nome))
    ind_sobrenome = random.randint(0,len(sobrenome))
    idade = random.randint(1,100)
    print('{} {} {} Anos'.format(nome[ind_nome],sobrenome[ind_sobrenome],idade))
    with open('saida.txt','w') as saida :
        print('NOMES', file= saida)       
            
