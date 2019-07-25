#subi
p=int(input())
c=0
d=list(map(int,input().split()))
for y in range(0,p):
  for x in range(0,y):
    if(d[x]<d[y]):
      c=c+d[x]
print(c)
