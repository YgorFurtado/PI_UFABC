n = int(input())
vet1 = [0]*n
vet2 = [0]*n
vet3 = [0]*n

itens_linha = input().split(" ")
for i in range(n):
    vet1[i] = int(itens_linha[i])
itens_linha = input().split(" ")

for i in range(n):
    vet2[i] = int(itens_linha[i])

for i in range(0,n):
    vet3[i] = vet1[i]/vet2[i]
    
if(len(set(vet3))) == 1:
    print("SIM")
else:
    print("NAO")