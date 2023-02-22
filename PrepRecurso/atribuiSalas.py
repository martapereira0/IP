salas={"FC1 120":[40,False],"FC1 219":[65,False],"FC1 227":[57,False],"FC6 008":[50,True]}

def atribuiSalas(lugares,salas):
    capmax=0 # sala com a capacidade minima
    id=0
    res=[]#lista que vai ser retornada
    while lugares!=0:   
        for i in salas:
            if salas[i][1]==False and salas[i][0]>=capmax:
                capmax=salas[i][0]
                id=i
        if capmax>lugares:
            for i in salas:
                if salas[i][1]==False and salas[i][0]<capmax and salas[i][0]>=lugares:
                    capmax=salas[i][0]
                    id=i
        salas[id][1]=True #passa a estar ocupada
        res.append((capmax,id))
        lugares-=capmax
    return res
def suficiente(lugares,salas):
    soma=0
    for i in salas:
        if salas[i][1]==False:
            soma+=salas[i][0]
    return soma>=lugares


def programa():
    nsalas=int(input())
    for i in range(nsalas):
        idsala=int(input())
        capsala=int(input())
        salas[idsala]=[capsala,False]
    nex=int(input())
    for j in range(nex):
        iduc,nlug=map(input().split())
        if suficiente(nlug,salas):
            res = atribuiSalas(lugares,salas)
            for t in res:
                codigo+=" "+str(t)
        else:
            codigo="Impossivel reservar salas para o exame de "+codigo
        print(codigo)
