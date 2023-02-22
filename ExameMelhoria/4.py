def analisar():
    n=int(input())
    x=int(input())
    contadorf=0
    contadori=0
    while x!=0:
        if x%2!=0:
            contadori+=1
        else:
            print("Contadori:%d" %contadori)
            if contadori<=n:
                contadorf=contadori
            contadori=0
            print("Contadorf:%d" %contadorf)
        x=int(input())
    return contadorf
print(analisar())