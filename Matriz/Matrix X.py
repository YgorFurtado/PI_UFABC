def obter_matriz_x(n):
    vet = [["🟥"] * n for i in range(n)]
    for i in range(len(vet)):
        for j in range(len(vet)):
            if j == i:
                vet[i][j] = "🟦"
            if j + i == (len(vet) - 1):
                vet[i][j] = "🟪"
    return vet
print('\n'.join([' '.join([str(max) for max in linha]) for linha in obter_matriz_x(5)]))