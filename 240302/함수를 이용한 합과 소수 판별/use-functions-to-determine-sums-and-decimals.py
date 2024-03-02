import math
a, b = map(int, input().split())
answer = 0

def chkFunc(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    sumnum = 0
    while x != 0:
        sumnum += x % 10
        x = x // 10
    
    if sumnum % 2 != 0:
        return False
    else:
        return True



for j in range(a, b+1):
    if chkFunc(j) == True:
        answer += 1
    
print(answer)