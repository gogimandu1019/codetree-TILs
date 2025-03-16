arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    if arr[i] == 0:
        arr.pop()

arr = arr[::-1]
n = len(arr)
for i in range(n):
    print(arr[i], end = " ")