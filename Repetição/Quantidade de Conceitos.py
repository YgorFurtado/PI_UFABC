from statistics import mean
n = int(input())
g = 0
grupo = [] 
a,b,c,d,f = (0,0,0,0,0)
while(g<n):
    grupo.append(int(input()))
    if grupo[g]<5:
        f = f +1
    elif grupo[g]<7:
        d = d + 1
    elif grupo[g]<8:
        c = c + 1
    elif grupo[g]<9:
        b = b + 1
    else:
        a = a + 1
    g = g +1
print("A: %i"%a)
print("B: %i"%b)    
print("C: %i"%c)    
print("D: %i"%d)    
print("F: %i"%f)    
print("Media: %.2f"%mean(grupo))