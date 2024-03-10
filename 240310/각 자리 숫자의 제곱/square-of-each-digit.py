N = int(input())

def getSquareSum(x):
    summ = 0

    if x < 1:
        return summ
    
    summ = getSquareSum(x // 10) + (x % 10)**2
    return summ

print(getSquareSum(N))