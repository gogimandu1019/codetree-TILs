n = int(input())
cnt = 0

for i in range(1, n+1):
    cnt = cnt+1
    n = int(n // cnt)
    
    if n <= 1:
        break;

print(i)