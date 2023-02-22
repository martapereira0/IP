def valida(x,n):
    c=0
    for i in range(len(x)):
        if x[i].isupper():
            c+=1
    if c!=n:
        return False
    else:
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i]==x[j]:
                    return False
    return True
print(valida("MortPo",2))