def embaralhar(nome):
    import random

    palavra = list(nome)
    random.shuffle(palavra)
    return (''.join(map(str, palavra)))



