n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
k = k%n
arr1 = arr[n-k: ] + arr[:n-k]
for i in range(n):
    print(arr1[i], end=' ')