linha=input().split(" ")
count=0
maximo=0
minimo=0
while linha[0]!="0":
    count+=1
    if linha[0]=="2":
        if linha[1]=="piupiu" or linha[1]=="cocorocoo" or linha[1]=="cacaraca" or linha[1]=="quaqua":
            maximo+=1
        else:
            minimo+=1
    linha=input().split(" ")
maximo+=minimo
print("%d %d %d"%(count,minimo,maximo))
