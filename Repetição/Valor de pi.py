def calcular_pi(n):
    positivo = 0
    negativo = 0
    quociente_positivo = 1
    quociente_negativo = 3
    if n%2 == 0:
        for i1 in range(0,int(n/2)):
            positivo = positivo + (1/quociente_positivo)
            negativo = negativo + (1/quociente_negativo)
            quociente_negativo = quociente_negativo + 4
            quociente_positivo = quociente_positivo + 4
    else:
        for i1 in range(0,(int(n/2)+1)):
            positivo = positivo + (1/quociente_positivo)
            quociente_positivo = quociente_positivo + 4
        for i1 in range(0,int(n/2)):
            negativo = negativo + (1/quociente_negativo)
            quociente_negativo = quociente_negativo + 4
    return((positivo-negativo)*4)