def reverso(numero):
    numero= str(numero)
    numero= list(numero)
    numero.reverse()
    return (''.join(map(str, numero)))

