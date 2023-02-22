lista=[]
elem=input()
while elem != '#':
    lista.append(elem)
    elem=input()
newlista=[len(lista)]
newlista[0]=lista[0]
for i in range(1,len(lista),1):
    if (lista[i-1]==lista[i]):
        newlista.append(lista[i])
    elif ((lista[i]=='a' and lista[i-1]=='c') or (lista[i]=='c' and lista[i-1]=='a')):
        newlista.append('t')
    elif ((lista[i]=='a' and lista[i-1]=='t') or (lista[i]=='t' and lista[i-1]=='a')):
        newlista.append('c')
    else:
        newlista.append('a')

for i in range(len(newlista)):
    print(newlista[i])       