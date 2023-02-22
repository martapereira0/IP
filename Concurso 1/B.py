duration=int(input())
hi1,hf1 = map(int,input().split())
hi2,hf2 = map(int,input().split())
intervalo1=hf1-hi1
intervalo2=hf2-hi2
if hi1<9 or hi2<9 or hi1>19 or hi2>19 or hf1>19 or hf2>19 or hf1-hi2<duration or intervalo1 < duration or intervalo2 < duration:
    print("Impossivel")

elif (hi1==hi2 and hf1==hf2 and intervalo1==duration) or hi2 <= hi1 and (intervalo1 == duration or hf2-hi1==duration):
    print(hi1)

elif hi1 <= hi2 and (intervalo2 == duration or hf1-hi2==duration):
    print(hi2)

else:
    if (hi1==hi2 and hf1==hf2 and intervalo1>=duration) or (hi1>hi2 and hf1>hf2) or (hi1==hi2 and hf1>hf2) or (hf1==hf2 and hi1>hi2):
        print(hi1,hf2-duration)
    elif (hi1<hi2 and hf1<hf2) or (hi1==hi2 and hf1<hf2) or (hf1==hf2 and hi1<hi2):
        print(hi2,hf1-duration)
    elif hi2 > hi1 and hf2 < hf1:
        print(hi2,hf2-duration)
    elif hi2 < hi1 and hf2 > hf1:
        print(hi1,hf1-duration)

