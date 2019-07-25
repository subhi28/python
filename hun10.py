p,q=map(int,input().split())
r={int(r) for r in input().split()}
s={int(s) for s in input().split()}
if (s.issubset(r)):
 print('YES')
else:
 print('NO')
