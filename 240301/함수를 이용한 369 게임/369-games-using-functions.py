a,b = map(int, input().split())
cnt = 0

def having369(x):
    k = x // 10
    l = x % 10
    if k == 3 or k == 6 or k == 9 or l == 3 or l == 6 or l == 9 or x % 3 == 0:
        return 1
    else:
        return 0

for i in range(a, b+1):
    cnt += having369(i)


print(cnt)