from datetime import datetime

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
    casa = []
    t1 = Tarefa('Lavar os pratos')
    t2 = Tarefa('Lavar roupa')
    t3 = Tarefa('Escovar os dentes')

    print(t1)

    casa.append(t1)
    casa.append(t2)
    
    for tarefa in casa:
        if tarefa.descricao == 'Lavar roupa':
            tarefa.concluir()

    for i in casa:
        print(i)
            
            
           
            
        
    

if __name__ == '__main__' :
    main()
