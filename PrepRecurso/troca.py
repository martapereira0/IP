def troca(mat,i,j):
    nlinhas=len(mat)
    ncols=len(mat[0])
    if nlinhas!=ncols:
        raise ValueError ("matriz deve ser quadrada")
    elif type(i)!=int or type(j)!=int or i<0 or j<0 or i>=nlinhas or j>=ncols:
        raise IndexError
    else:
        for m in range(nlinhas):
            var=mat[m][j]
            mat[m][j]=mat[i][m]
            mat[i][m]=var
    return mat
print(troca([[3,5,4],[2,1,0],[1,7,8]],6,0))

