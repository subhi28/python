import math
su=int(input())
bi=math.radians(su)
if su==90:
    print(1)
else:
    print(round(math.sin(bi),1))
