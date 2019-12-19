class Lixeira:
    def __init__ (self, lixo):
        self.lixo = lixo

    def adicionar_lixo(self, lixo):
        self.lixo.append(lixo)

    def esvasiar_lixeira(self):
        self.lixo = []

    def ver_lixeira(self):
        print(self.lixo)

    def quantidade_de_lixo(self):
        return len(self.lixo)

"""
#TESTE
x= Lixeira(['folha','caneta velha'])
x.ver_lixeira()
x.adicionar_lixo('lata de refrigerante')
print(x.quantidade_de_lixo())
"""
        
