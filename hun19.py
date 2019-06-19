x,y=map(int,input().split())
list=[]
for i in range(x):
    z=set(map(int,input().split()))
    list.append(z)
num=z.intersection(*list)
print(*num)
