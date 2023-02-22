n = int(input())
cazul=0
camarelo=0
cverde=0
while n != -1:
    if n<=10 and n>=1:
       cazul+=1
    elif n<=23 and n>=11:
        cverde+=1
    elif n>=24 and n<=40:
        camarelo+=1
    n = int(input())
print("azul: %d" %cazul)
print("amarelo: %d" %camarelo)
print("verde: %d" %cverde)