class Pokemon:
    def __init__ (self, nome, tipo, descricao, nivel, poder_luta, brilhante):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = []
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante =brilhante
    
    def mostrar_ataques(self):
        print(self.ataques)

    def subir_nivel(self, nivel_a_mais):
        self.nivel_a_mais = nivel_a_mais
        self.nivel += nivel_a_mais
    
    def mostrar_poder_luta (self):
        print(self.poder_luta)
    
    def e_brilhante(self):
        if self.nivel > 100 or self.poder_luta > 1000:
            return True
        else:
            return False
    def adicionar_ataque(self, ataques_novos):
        self.ataques.append(ataques_novos)

"""
#TESTE
x= Pokemon('xuxa', 'RARO', 'FORTE E RAPIDO', 99, 1201, True)
x.adicionar_ataque('CHUTAR')
x.mostrar_ataques()
x.subir_nivel(15)
x.mostrar_poder_luta()
print(x.e_brilhante())
"""