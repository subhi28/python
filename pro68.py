num1,num2=input().split()
num1=int(num1)
num2=int(num2)
if(num2<num1-num2):
    print(1,num2+1)
else:
    print(1,num1-num2)
