n, m = map(int, input().split())
A = list(map(int, input().split()))
answer = 0

while m >= 1:
    answer += A[m-1]
    if m % 2 == 0:
        m = m // 2
    else :
        m = m - 1
    

print(answer)