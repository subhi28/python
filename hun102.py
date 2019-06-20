num=int(input())
sum=0
while(num!=0):
    s=num%10
    sum=sum+s**2
    num=num//10
print(sum)    
