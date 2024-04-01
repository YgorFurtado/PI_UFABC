def criaVetor(n_linhas,n_colunas):
    matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
    for linha in range(n_linhas):
        itens_linha = input().split(" ")
        for coluna in range(n_colunas):
            matriz[linha][coluna] = float(itens_linha[coluna])  
    return matriz

def lerBomba(vet,linha,coluna):
    bombas = 0
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if vet[coluna+i][linha+j] == 1:
                    bombas +=1
            except IndexError:
                continue
    if vet[linha][coluna] == 1:
        bombas -= 1
    return bombas
campo = criaVetor(int(input()),int(input()))
bomba = lerBomba(campo,int(input()),int(input()))
print(bomba)