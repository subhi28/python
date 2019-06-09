num1,num2=map(int,input().split())
num3=lost(map(int,input().split()))
num4=[]
for i in range(num1-num2,num1):
    num4.append(num3[i])
print(*num4)    
