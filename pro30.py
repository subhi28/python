#subi
p=(input())
q=0
for i in range(0,len(p)):
    r=(p[:i]+p[i+1:])
    if(int(r) % 8==0):
        q=1
        break
if(q==1):
    print("yes")
else:
    print("no")
