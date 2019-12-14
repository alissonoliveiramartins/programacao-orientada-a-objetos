class Televisao:
    def __init__ (self, volume=1, canal=1):
        self.volume = volume
        self.canal = canal
    
    def mudar_volume(self):
        self.volume += 1 
        
    def subir_volume(self):
        if self.volume < 100:
            self.volume += 1
        
    def descer_volume(self):
        if self.volume > 1:
            self.volume -= 1  
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
    
    def subir_canal(self):
        if self.canal < 100:
            self.canal += 1
        
    def descer_canal(self):
        if self.canal > 1:
            self.canal = self.canal - 1
            
    def mostrar_volume(self):
        print(self.volume)
        
    def mostrar_canal(self):
        print(self.canal)

"""
#TESTE        
x= Televisao(56,30)
x.descer_canal()
x.mostrar_canal()
x.mudar_volume()
x.mostrar_volume()
x.subir_volume()
x.mostrar_volume()
"""
