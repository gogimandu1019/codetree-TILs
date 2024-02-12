n = int(input())

arr = [ [0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = j * n + i + 1
        print(arr[i][j], end = " ")
    print()