#subi
t6=int(input())
s6=list(map(int,input().split()))
cc=[]
nn=1
for i in s6:
  if i not in cc:
    cc.append(i)
for i in range(0,len(cc)-1):
  if cc[i]<cc[i+1]:
    nn+=1
print(nn)
