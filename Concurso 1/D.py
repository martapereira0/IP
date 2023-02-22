h1,m1 = map(int,input().split())
h2,m2 = map(int,input().split())
m1total=h1*60+m1
m2total=h2*60+m2
diffm=m2total-m1total
if diffm < 60:
    if diffm == 1:
        print("Passou apenas 1 minuto!")
    else:
        print("Passaram apenas %d minutos!" %diffm)
    print("De facto!")
else:
    print("Passaram apenas %d minutos!" %diffm)
    ht=diffm//60  #obter a parte da unidade da divisao
    mt=diffm%60 #obter a parte dcimal da divisao
    if ht==1:
        if mt==1:
            print("Queres dizer, %d hora e %d minuto?!" %(ht,mt))
        elif mt==0:
            print("Queres dizer, %d hora?!" %ht)
        else:
            print("Queres dizer, %d hora e %d minutos?!" %(ht,mt))
    else:
        if mt==1:
            print("Queres dizer, %d horas e %d minuto?!" %(ht,mt))
        elif mt==0:
            print("Queres dizer, %d horas?!" %ht)
        else:
            print("Queres dizer, %d horas e %d minutos?!" %(ht,mt))


