num=int(input())
list=[]
for i in range(num):
    list.append(input())
minlen=len(min(list,key=len))
for i in range(len(list)-1):
    for j in range(minlen):
        if list[i][:j+1] in list[i+1]:
            s=list[i][:j+1]
print(s)            
