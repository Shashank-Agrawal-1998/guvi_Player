n = int(input())
arr = list(map(int, input().strip().split()))
flag = 0 
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = 1
    if flag==0:
        break
median = n//2
print(arr[median], end='')
