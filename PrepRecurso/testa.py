def testa(x):
    tam = len(x)
    if tam>1:
        for i in range(tam-1):
            if x[i].isdigit()==True and x[i+1].isalpha()==False:
                return False
        return True
    else:
        return False


print(testa(""))
print(testa("8A7krt7g/5M8A7K"))
print(testa("AaBcG"))
print(testa("@7A$8A-?9aA"))
print("\n")
print(testa("8"))
print(testa("m875kgr"))
print(testa("B5Aa7"))