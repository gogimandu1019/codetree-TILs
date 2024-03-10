n = int(input())
arr = list(map(int, input().split()))

def findMax(x):
    maxi = 0
    if x == 1 :
        return arr[0]

    cache = int(findMax(x-1))
    if cache > arr[x-1]:
        return cache
    else:
        return arr[x-1]
    

print(findMax(n))