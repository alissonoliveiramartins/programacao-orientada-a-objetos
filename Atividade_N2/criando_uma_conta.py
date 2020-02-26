def	criar_conta(numero,	titular,	saldo,	limite):
    """Função responsavel por criar a conta"""
    conta={"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return	conta
def	deposita(conta,	valor):
	conta['saldo'] += valor
	"""Funçaõ adiciona o valor a conta"""

def	saca(conta,	valor):
    """Função subtrai o valor da conta"""
    conta['saldo']	-=	valor
   
	
def	extrato(conta):
    """Esta função imrimi o extrado da conta"""
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))