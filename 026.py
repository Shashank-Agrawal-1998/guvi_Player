def quicksort1(arr, f, l):
    if f<l:
        k = partition(arr, f, l)
        quicksort1(arr,f,k-1)
        quicksort1(arr,k+1,l)
        
def partition(arr, f, l):
    i = f-1
    pivot = arr[l]
    for j in range(f,l):
        if arr[j]<=pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[l] = arr[l], arr[i+1]
    return i+1
    
n = int(input())
arr = list(map(int, input().strip().split()))
quicksort1(arr, 0, n-1)
for i in range(n):
    print(arr[i], end=' ')
