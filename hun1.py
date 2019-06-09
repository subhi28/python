num1=int(input())
num2=list(map(int,input().split()))
num3=[]
for i in num2:
    if(num2.count(i)>1):
        num3.append(i)
A=set(num3)
if len(A)==0:
    print('unique')
else:
    print(*A)
