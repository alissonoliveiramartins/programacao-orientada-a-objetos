#!/usr/local/bin/python3
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    #Adiciona se for obejto Tarefa ou TarefaRecorrente
    def _add_tarefa(self, descricao, **kwags):
        self.tarefas.append(descricao)

    #Adiciona tarefa baseado em uma descrição
    def _add_tarefa_descricao(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento',None)))


    def add(self, descricao_tarefa, vencimento=None, **kwargs):
        fucao_escolhida = self._add_tarefa if isinstance(descricao_tarefa, Tarefa)\
            else self._add_tarefa_descricao
        kwargs['vencimento'] = vencimento
        fucao_escolhida(descricao_tarefa, **kwargs)

            #isinstance (condição) só adiciona se sor uma instacia do que estiver em parentes
   
    #def add(self, descricao, vencimento=None):
    #    self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):

        return [tarefa for tarefa in self.tarefas 
            if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.add(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    casa.add(casa.procurar('Trocar lencois').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()