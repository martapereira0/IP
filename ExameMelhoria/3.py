def verifica(x):
    nlinhas=len(x)
    ncols=len(x[0])
    sacima=0
    sabaixo=0
    if nlinhas!=ncols:
        raise RuntimeError ("não quadrada")
    else:
        for i in range(nlinhas-1):
            sacima+=x[i][i+1]
        for j in range(1,ncols):
            sabaixo+=x[j][j-1]
        print("soma acima: %d \nsoma abaixo:%d" %(sacima,sabaixo))
        if sabaixo<sacima:
            return True
        else:
            return False
print(verifica([[7,5,3],[2,1,0],[4,3,4]]))
