a,b = map(int, input().split())
cnt = 0

def having369(x):
    if '3' in str(x) or '6' in str(x) or '9' in str(x) or x % 3 == 0:
        return 1
    else:
        return 0

for i in range(a, b+1):
    cnt += having369(i)


print(cnt)