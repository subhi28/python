#subi
p,q=input().split()
p=int(p)
q=int(q)
s=''
u=2
if(p+q<=3):
    for i in range(0,p+q):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,p+q):
        if(i==u):
            s=s+'0'
            if(u==q):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1') 
elif p==1 and q==2: 
     print("011")
else:
    print(s)
