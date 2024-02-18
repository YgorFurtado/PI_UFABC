from textwrap import wrap
serial = wrap(input(), 2)
plan = ["Marte", "Saturno", "Netuno", "HD21749b"]
cod_plan = ["80", "81", "90", "91"]
mod = ["A6000", "B7500", "C9000"]
cod_mod = ["60", "61", "62"]
n = 0
while (n <= 3):
    if serial[0] == cod_plan[n]:
        print(plan[n])
        n = 0
        break
    n = n+1
while (n <= 3):
    if serial[1] == cod_plan[n]:
        print(plan[n])
        n = 0
        break
    n = n+1
while (n <= 2):
    if serial[2] == cod_mod[n]:
        print(mod[n])
        n = 0
        break
    n = n+1