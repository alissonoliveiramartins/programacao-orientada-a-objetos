class Computador:
    def __init__ (self, marca, modelo, componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor

    def mostrar_marca(self):
        print(self.marca)

    def adicionar_componentes(self, componente_novo):
        self.componentes.append(componente_novo)

    def mostrar_componentes(self):
        print(self.componentes)

    def mostrar_anos_uso(self):

        if (self.anos_uso < 6):
            print(self.anos_uso)
        else :
            print('Seu computador está tão velho que tem que juntar... juntar tudo e jogar fora...')
    
    def envelhecer(self, anos_a_mais):
        self.anos_a_mais = anos_a_mais
        self.anos_uso = self.anos_uso + anos_a_mais


"""
#TESTE

x = Computador('Dell', '7.7', ["monitor", "mouse"], 15, 'azul')
x.mostrar_marca()
x.adicionar_componentes("teclado")
x.mostrar_componentes()
x.envelhecer(2)
x.mostrar_anos_uso()
"""
