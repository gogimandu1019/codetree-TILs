import sys
n = int(input())
arr = list(map(int, input().split()))
arr.append(-sys.maxsize)

def findMax(x):
    if x == 1 :
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]


    if findMax(x-1) > arr[x]:
        return findMax(x-1)
    else:
        return arr[x]
    

print(findMax(n))