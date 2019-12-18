class Aluno:
    
    def __init__ (self, nome, curso, media, situacao):
        self.nome = nome
        self.curso = curso
        self.media = media
        self.situacao = situacao
        
    def motrar_aluno(self):
        print(f'Nome: {self.nome}, Curso: {self.curso}')
        print(self.situacao.upper())
        
    def mudar_media(self, nova_media):
        self.media = nova_media 
        if self.media >= 7:
            self.situacao = 'Aprovado'
        else:
            self.situacao = 'Reprovado'
    