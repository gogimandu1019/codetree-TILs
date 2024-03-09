n,m = map(int, input().split())
A = list(map(int, input().split()))

def getSum(a,b):
    summ = 0
    for i in range(a-1, b):
        summ += A[i]

    return summ

for _ in range(m):
    a1, a2 = map(int, input().split())

    print(getSum(a1,a2))