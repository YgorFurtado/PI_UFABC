n = int(input())
i = 1
v = 0
while(i<=n):
    j = 1
    while(j<=8):
        v = v + ((i+1)*j)
        j = j + 1
    i = i + 1
print(v)