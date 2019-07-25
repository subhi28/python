#subi
p = int(input())
l6 = list(map(int, input().split()))
n = int(len(l6)/2)
if sum(l6[:n])//len(l6[:n]) == sum(l6[n:])//len(l6[n:]):
    print('yes')
else:
    print('no')
