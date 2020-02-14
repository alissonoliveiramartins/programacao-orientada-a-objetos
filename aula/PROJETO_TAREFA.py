#!/usr/local/bin/python3
from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao,vencimento))

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
              
    def pendende(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
       
    def __str__ (self):
        return f'{self.nome} ({len(self.pendende())}) tarefa(s) pendente(s)'

# tona o projeto interavel
    def __iter__(self):
        return self.tarefas.__iter__()

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        # return self.descricao + (' (Concluída)' if self.feito else '')
        status = []
        if self.feito :
            status.append('{Concluida}')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao}'+' '.join(status)

class TerefaRecorrente(Tarefa):
    def __init__ (self, descricao, vencimento, dias=7):
        super().__init__ (descricao, vencimento)
        self.dias = dias

def main():
    projeto1 = Projeto('IFCE')
    projeto1.add('Estudar POO',datetime.now() + timedelta(days=3, seconds=1))
    projeto1.add('Estudar Metodologia')
    print(projeto1)

    projeto1.procurar('Estudar Metodologia').concluir()

    for tarefa in projeto1:
        print(f'- {tarefa} ')

    print(projeto1)

"""    # Desafio -> 'Lavar prato'
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']

    for tarefa in casa:
        print(f'- {tarefa}')"""


if __name__ == '__main__':
    main()
