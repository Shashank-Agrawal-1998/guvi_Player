n = int(input())
arr = list(map(int, input().strip().split()))
min = arr[0]
for i in range(n):
    if arr[i]<min:
        min = arr[i]
print(min,end='')
