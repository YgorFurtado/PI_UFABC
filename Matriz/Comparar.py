def comparar_matrizes(m1, m2):
    for i in range(0, len(m1)):
        for j in range(0, len(m1[1])):
            if m2[i][j] != 2 * (m1[i][j]):
                return False
    return True
