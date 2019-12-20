class Oculos:
  def __init__ (self, grau, preso, cor, tipo):
    self.grau = grau
    self.preso = preso
    self.cor = cor
    self.tipo  = tipo

  def aumentar_grau(self):
    self.grau += 0.5
  
  def diminuir_grau(self):
    self.grau -= 0.5
  
  def mudar_cor(self, nova_cor):
    self.cor = nova_cor

  def alterar_tipo(self, novo_tipo):
    self.tipo = novo_tipo
  
  def ver_caracteristicas(self):
    print(f'Oculos da cor {self.cor}, com a armaçaõ {self.tipo}, com {self.grau} graus no valor de {self.preso} R$')

"""
#Teste
x = Oculos(1.5, 800.00, 'Preto', 'Esportivo')
x.ver_caracteristicas()
x.aumentar_grau()
x.ver_caracteristicas()
x.mudar_cor('Azul')
x.ver_caracteristicas()
"""