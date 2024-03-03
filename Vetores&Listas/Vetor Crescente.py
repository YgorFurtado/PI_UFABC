n = int(input())
v = [0] * n
teste = 0

itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])

for i in range(0,n-1):
    if v[i] > v[i+1]:
        teste = 1
        break
if teste == 1:
    print("NAO")
else:
    print("SIM")