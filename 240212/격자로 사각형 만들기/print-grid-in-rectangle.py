n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0,n):
    for j in range(0,n):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else :
            arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]


for a in range(0, n):
    for b in range(0, n):
        print(arr[a][b], end= " ")
    print()