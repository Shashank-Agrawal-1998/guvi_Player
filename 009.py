l, r = map(int, input().strip().split())
lis = [1 for i in range(r+1)]
lis[0] = 0
lis[1] = 0
p = 2
for i in range(2,r+1):
    if lis[i]==1:
        for j in range(i+p, r+1, p):
            lis[j] = 0
        for j in range(p+1, r+1):
            if lis[j]==1:
                p=j
                break
c = 0
for i in range(l,r+1):
    if lis[i]==1:
        c+=1
print(c)