with open('usuarios.txt' ) as prova:
    with open("relatorio.txt", "w") as saida:

        def conversao(numero_byts):
            return (int(numero_byts) /1024 / 1024)
     
       
        lista_dados = []
        lista_nomes =[]
        lista_percentual= []

        soma = 0
        numeracao = 1
       
        for x in prova:
            x = x.strip()
            nomes ,dados = x.split()
            lista_dados.append(dados)
            lista_nomes.append(nomes)
            percentual = (int(dados)*100 )
            lista_percentual.append(percentual)
            soma += int(dados)
           
        print('ACME Inc.           Uso do espeço em disco pelos usuários\n{}\nNr.        Usuario        Espaço Utilizado        % do uso\n'.format('-'*60), file=saida)

        
        for indice in range(0,len(lista_nomes)):
            print('{:<3}      {:<10}       {:>8.2f}MB         {:>6.2f} %'.format(indice+1,lista_nomes[indice].center(15),conversao(lista_dados[indice]),int(lista_percentual[indice])/soma), file=saida)        
        soma = (soma/1024/1024)
        print(' ', file=saida)
        print('Espaço total ocupado: {:.2f} MB'.format(soma), file=saida)  
        print('Espaço médio ocupado: {:.2f} MB'.format(soma/len(lista_nomes)), file=saida)
 
