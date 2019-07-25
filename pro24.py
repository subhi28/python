#subi
n6 = int(input())
r6 = []
for i in range(pow(2, n6)):
    r6.append(bin(i)[2:].zfill(n6))
r6.sort(key=(lambda x: x.count('1')))
for i in r6:
    print(i)
