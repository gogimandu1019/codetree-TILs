N = int(input())

def getSumm(x):
    summ = 0

    if x == 0:
        return summ 
    
    summ = getSumm(x-1) + x
    return summ


print(getSumm(N))