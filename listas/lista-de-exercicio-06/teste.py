def copia(argumento1,argumento2):
    with open(argumento1) as arquivo1:
        with open(argumento2, 'w') as arquivo2:
            for linha in arquivo1:
                if '//' not in linha:
                    print(linha , file = arquivo2)

copia("aquirvo1.txt","deucertos")