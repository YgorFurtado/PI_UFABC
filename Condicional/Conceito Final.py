t = [float(input()), float(input()), float(input())]
p = [float(input()), float(input())]
nf = (0.2*(sum(t)/len(t))) + (0.4*(sum(p)))
print("%.2f" % nf)
if (9 <= nf <= 10):
    print("A")
elif (7.5 <= nf < 10):
    print("B")
elif (6 <= nf < 10):
    print("C")
elif (5 <= nf < 10):
    print("D")
else:
    print("F")
