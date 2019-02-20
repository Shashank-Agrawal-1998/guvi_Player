n = int(input())
arr = list(map(int, input().strip().split()))
max = arr[0]
for i in range(n):
    if arr[i]>max:
        max = arr[i]
print(max)