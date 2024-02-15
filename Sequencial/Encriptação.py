num = input()
lista = [int(n) for n in num]
i = 0
while i<=3:
    lista[i] = str((lista[i]+1)%10)
    i = i+1
print("".join(lista))