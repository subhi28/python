s,b=map(str,input().split())
u=0
for i in range(0,len(s)):
    for j in range(0,len(b)):
        if s[i]==s[j]:
            u=u+1
if u>=2:
    print('yes')
else:
    print('no')
        
        
        
