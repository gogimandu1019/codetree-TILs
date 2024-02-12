n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
k = 1

for i in range(n):
    i = n - i #지금 채울 열 번호
    if n % 2 == i % 2:
        for j in range(n):
            j = n - j
            arr[j-1][i-1] = k            
            k = k + 1
    else:
        for j in range(n):
            arr[j][i-1] = k            
            k = k + 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()