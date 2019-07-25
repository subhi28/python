#subi
n6=int(input())
l6=list(map(int,input().split()))
l6.sort()
s=0
c=0
for i in range(len(l6)):
    if l6[i]>=s:
        c=c+1
    s=s+l6[i]
print(c)
