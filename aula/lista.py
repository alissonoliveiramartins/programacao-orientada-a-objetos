from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def procurar(self, descricao):
        for tarefas in self.tarefas:
            if tarefas.descricao == descricao:
                return tarefas

    def pendende(self):
        tarefas_pendentes =[]
        for tarefas in self.tarefas:
            if tarefas.feito == False:
                tarefas_pendentes.append(tarefas)
        return tarefas_pendentes
        
        
class Tarefa:
    def __init__ (self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.feito= True

    def __str__ (self):
        retorno = "Data de criação: "+str(self.criacao)+"Descrição = "+self.descricao+"Status = "+str(self.feito)
        return retorno

def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Lavar os pratos')
    casa.add('Lavar roupa')
    casa.add('Escovar os dentes')
    
    print(casa.procurar('Lavar roupa'))
    
    casa.procurar('Lavar roupa').concluir()

    for tarefa in casa.pendende():
        print(tarefa)
"""
    print(t1)

    casa.append(t1)
    casa.append(t2)
    
    for tarefa in casa:
        if tarefa.descricao == 'Lavar roupa':
            tarefa.concluir()

    for i in casa:
        print(i)
"""            
            
           
            
        
    

if __name__ == '__main__' :
    main()
