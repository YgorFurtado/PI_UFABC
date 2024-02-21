def obter_valor_funcao(a, b, c):
    d = 1
    v = 0
    while(d<=b):
        v = v + (c*d)
        d = d+1
    r = a+v
    return r