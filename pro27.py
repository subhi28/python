#subi
p,q=map(int,input().split())
r=list(map(int,input().split()))
s=list(map(int,input().split()))
tan=[]
cin=0
for i in range(p):
    x=s[i]/r[i]
    tan.append(x)
while q>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if q>=r[mindex]:
        cin=cin+s[mindex]
        q=q-r[mindex]
    r.pop(mindex)
    s.pop(mindex)
    tan.pop(mindex)
print(cin)
