def ler_analisar():
    v=0
    n=0
    x=int(input())
    while x!=0:
        if x%2!=0:
            n+=1
            if x<0:
                v=x
        x=int(input())
    return (v,n)

x=[[1,2],[3,2],[4,7]]
print(type('a'))
