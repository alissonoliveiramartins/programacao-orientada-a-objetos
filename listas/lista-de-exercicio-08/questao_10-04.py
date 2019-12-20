class Queijo:
  def __init__ (self, kilo, valor_kilo):
    self.kilo = kilo
    self.valor_kilo = valor_kilo

  def preco(self):
    self.preso = self.kilo * self.valor_kilo
    return self.preso
  
  def mudar_valor(self, novo_valor):
    self.valor_kilo = novo_valor

  def mudar_kilo(self, novo_kilo):
    self.kilo = novo_kilo
  
  def ver_caracteristicas(self):
    print(f'Peso: {self.kilo}kg, Valor por kilo: {self.valor_kilo:.2f}R$, Valor do Queijo: {self.preso:.2F}R$')

"""
#Teste
x = Queijo(1, 15)
print(x.preco())
x.ver_caracteristicas()
"""