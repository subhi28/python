x,y=map(int,input().split())
z=list(map(int,input().split()))
for i in range(y):
    a,b=map(int,input().split())
    c=lis[a-1:b]
    print(min(c))
