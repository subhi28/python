num1,num2,num3=input().split()
n1=int(num1)
n2=int(num2)
n3=int(num3)
if(n1>n2) and (n1>n3):
    print(n1)
elif(n2>n1) and (n2>n3):
    print(n2)
else:
    print(n3)
