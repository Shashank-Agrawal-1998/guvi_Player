n = int(input())
fac = []
for i in range(2,n+1):
    if n%i==0:
        fac.append(i)
        while(n%i==0):
            n = n//i
for i in fac:
    print(i,end=' ')