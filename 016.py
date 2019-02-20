n = int(input())
arr = list(map(int, input().strip().split()))
d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
for i in d:
    if d[i] == 1:
        print(i)
        break