#su
import math
p,q=map(int,input().split())
r=[]
s=list(map(int,input().split()))
for i in range(0,q):
    u,v=map(int,input().split())
    r.append([u,v])
for i in r:
    x=i[0]-1
    y=i[1]-1
    print(math.gcd(s[x],s[y]))
