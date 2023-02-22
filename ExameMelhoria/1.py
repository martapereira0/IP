def tabela(v,p):
    m=len(v)
    for k in range(0,m,p):
        r=0
        for t in range(k):
            r=v[t]+r
        print(r,k,v[k])

tabela([5,9,-2,3,1,4],2)