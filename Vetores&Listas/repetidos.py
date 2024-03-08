from collections import OrderedDict
n = int(input())
lista = [0] * n
lista2 = []

itens_linha = input().split(" ")
for i in range(n):
    lista[i] = int(itens_linha[i])
    
def desrepetir(l):
    l2 = []
    [l2.append(i) for i in l if not l2.count(i)]
    return l2
print(desrepetir(lista))