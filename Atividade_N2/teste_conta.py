def cria_conta(numero, titular, saldo, limite):
    """Função responsavel por criar a conta"""
    conta={"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta

def deposita(conta, valor):
    """Funçaõ adiciona o valor a conta"""
    conta['saldo'] += valor
    
def saca(conta,	valor):
    """Função subtrai o valor da conta"""
    conta['saldo'] -= valor
   
def extrato(conta):
    """Esta função imprimi o extrato da conta"""
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))
