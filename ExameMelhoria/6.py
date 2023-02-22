alunos={"1":("Marta",[("4",12),("8",7)]),"2":("Ana",[("4",19),("8",8)]),"3":("Maria",[("4",12),("9",7)]),"4":("Martim",[("9",12),("8",7),("10",4)]),"5":("Margarida",[("10",12),("8",7)])}
salas={"1010":2,"233":4,"45":5}
registados=["1","2","3","4","5"]
salasEx=["1010","233"]
def atribuirSalas(registados,alunos,salas,salasEx):
    c=0
    d=1
    for i in salasEx:
        capsala=salas[i]
        for j in range(c*capsala,capsala*d,1):
            cod=registados[j]
            nome=alunos[cod][0]
            idsala=i
            print("%s;%s;%s" %(cod,nome,idsala))
        c+=1
        d+=1
    return 
atribuirSalas(registados,alunos,salas,salasEx)

def troca(registados,codigoUC,alunos):
    for i in range(len(registados)):
        nmec=registados[i]
        infoaluno=alunos[nmec]
        for m in range(len(infoaluno[1])):
            if infoaluno[1][m][0]==codigoUC:
                if infoaluno[1][m][1]>=10:
                    registados.remove(nmec)
                    registados.insert(0,nmec)
    return registados


