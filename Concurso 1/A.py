call,elev1,elev2 = map(int,input().split())
dist1 = elev1 - call
dist2 = elev2 - call
if elev1 < call:
    dist1=dist1*(-1)
if elev2 < call:
    dist2=dist2*(-1)
if elev1 == 999 and elev2 == 999: print("0")
elif elev1 == 999 or (dist1 == dist2 and elev1 < elev2) or dist2 < dist1: print("2")
elif elev2 == 999 or elev1 == elev2 or (dist1 == dist2 and elev1 > elev2) or dist1 < dist2: print("1")