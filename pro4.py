#subi
p,q=map(str,input().split())
r=0
if len(p)>len(q):
    p,q=q,p
s=0
while s<len(p):
      r+=(ord(q[s])-ord(p[s]))
      s+=1
for s in range(s,len(q)):
      r+=ord(q[s])-ord('a')+1
print(r)
