#subi
p,q=map(int,input().split())
pq=[]
for i in range(q):
  pq.append(list(map(int,input().split())))
w=10000000
f=0
for i in range(q):
  if pq[i][0]==1:
    s=pq[i][1]
    c=pq[i][2]
    for j in range(i+1,q):
      if pq[j][0]==s:
        s=pq[j][1]
        c+=pq[j][2]
    if c<w and s==p:
      w=c
      f+=1
if f==0:
  print(-1)
else:
  print(w)
