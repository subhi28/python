#subi
n6=int(input())
ar=list(map(int,input().split()))
sum=0
list1=[]
for i in range(0,len(ar),2):
  sum+=ar[i]
  list1.append(sum)
sum=0
for i in range(1,len(ar),2):
  sum+=ar[i]
  list1.append(sum)
print(max(list1))
