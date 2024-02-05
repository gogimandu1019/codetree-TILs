n = int(input())
cnt = 0
x = 0

for i in range(1, n+1):
    x = int(n / i)
    cnt = cnt+1
    i = i + 1
    n = x
    
    if x == 0:
        print(cnt)
        break;