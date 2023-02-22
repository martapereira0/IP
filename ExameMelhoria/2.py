def valida(s):
    if len(s)<11:
        return False
    else:
        contador=0
        for i in range(len(s)):
            if s[i].isdigit():
                contador+=1
        if contador!=9:
            return False
        for i in range(9,len(s)):
            if s[9]!=" ":
                return False
            else:
                if s[10].islower():
                    return False
        return True
def filtra():
    lista=[]
    m=int(input())
    for i in range(m):
        s=input()
        if valida(s)==True:
            str=""
            for j in range(9):
                str+=s[j]
            lista.append(str)
    return lista

print(filtra())