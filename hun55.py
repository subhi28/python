num1,num2=map(int,input().split())
value=list(map(int,input().split()))
for i in range(num2):
    value.append(value[0])
    value.remove(value[0])
print(*value)    
