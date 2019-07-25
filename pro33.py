#subi
p=input()
for i in range(len(p)):
  if (p[i]<p[i+1]):
   print(p[i+1:])
   break
   
