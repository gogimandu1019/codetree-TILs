n, m= map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
answer =[[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    x = arr[i][0]
    y = arr[i][1]
    answer[x-1][y-1] = x*y

for a in range(n):
    for b in range(n):
        print(answer[a][b], end = ' ')
    print()