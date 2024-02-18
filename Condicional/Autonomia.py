import math
carga = float(input())
a = [float(input()), float(input())]
b = [float(input()), float(input())]
dist = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
print("%.2f" % dist)
if ((carga <= 50000 and dist <= 18000) or (50001 <= carga <= 200000 and dist <= 9000) or (200001 <= carga <= 250000 and dist <= 3000)):
    print("SIM")
elif ((carga <= 50000 and dist <= 19800) or (50001 <= carga <= 200000 and dist <= 9900) or (200001 <= carga <= 250000 and dist <= 3300)):
    print("TALVEZ")
else:
    print("NAO")
