def checar_primo(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return 0
        else:
            return(num)
    else:
        return(0)

def contar_primo(quantidade):
    n = 0
    i = 1
    while(n < quantidade):
        if checar_primo(i) == 0:
            i = i + 1
        else:
            print(checar_primo(i))
            i = i + 1
            n = n + 1
    return 0

contar_primo(int(input()))