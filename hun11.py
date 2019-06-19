a=input().split()
list=[]
for i in a:
    list.append(i[::-1])
print(*list)    
