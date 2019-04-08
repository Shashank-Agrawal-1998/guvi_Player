n1 = int(input())
arr = list(map(int, input().strip().split()))
flag = 0 
for i in range(0, n1-1):
    for j in range(0, n1-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = 1
    if flag==0:
        break
for i in range(n1):
    print(arr[i], end=' ')
