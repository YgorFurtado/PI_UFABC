altura = int(input())
largura = (altura*2)-1
linha = 1
num = 1
for i in range(0,altura):
    hif = largura - num
    contador_hif = 0
    contador_num = 0
    while(contador_hif<hif/2):
        print("-",end="")
        contador_hif = contador_hif + 1
    while(contador_num<num):
        print("1",end="")
        contador_num = contador_num + 1
    while(contador_hif<hif):
        print("-",end="")
        contador_hif = contador_hif + 1
    print("")
    num = num + 2
    linha = linha + 1