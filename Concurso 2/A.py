cols,rows=map(int,input().split())
cverm=0
cverde=0
cazul=0
nquadriculasverm=1 #numero de quadriculas vermelhas inicias
nquadriculasverdes=3 #numero de quadriculas verdes inicias
nquadriculasa=5 #numero de quadriculas azuis inicias
indexv=0
if rows <= cols:
    for i in range(0,rows,1):
        if i==0 or i%3==0:   #vermelhos
            cverm = cverm + nquadriculasverm
            nquadriculasverm += 6
            flag = 0
        elif i==1 or i-indexv==3:
            indexv=i
            cverde = cverde + nquadriculasverdes
            nquadriculasverdes += 6
            flag = 1
        else:
            cazul = cazul + nquadriculasa
            nquadriculasa += 6
            flag = 2
    falta_preencher = cols - rows
    for i in range (0,falta_preencher,1):
        if flag == 0:
            cverde = cverde + rows
            flag = 1
        elif flag == 1:
            cazul = cazul + rows
            flag = 2
        else:
            cverm = cverm + rows
            flag = 0
if rows > cols:
    for i in range(0,cols,1):
        if i==0 or i%3==0:   #vermelhos
            cverm = cverm + nquadriculasverm
            nquadriculasverm += 6
            flag = 0
        elif i==1 or i-indexv==3:
            indexv=i
            cverde = cverde + nquadriculasverdes
            nquadriculasverdes += 6
            flag = 1
        else:
            cazul = cazul + nquadriculasa
            nquadriculasa += 6
            flag = 2
    falta_preencher = rows - cols
    # a flag vai nos dizer qual a última cor que foi "pintada"
    for i in range (0,falta_preencher,1):
        if flag == 0:
            cverde = cverde + cols
            flag = 1
        elif flag == 1:
            cazul = cazul + cols
            flag = 2
        else:
            cverm = cverm + cols
            flag = 0
print("%d %d %d" %(cverm,cverde,cazul))