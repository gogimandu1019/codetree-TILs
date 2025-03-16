N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = ""
summ = 0
avg = 0
cnt = 0
for i in range(N):
    summ = 0
    avg = 0
    for j in range(4):
        summ = summ + arr[i][j]
    avg = summ / 4
    if avg >= 60:
        result = "pass"
        cnt += 1
    else:
        result = "fail"
    print(result)
print(cnt)