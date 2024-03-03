N = int(input())
X = list(map(int, input().split()))

def getAbs(arr, x):
    for i in range(x):
        if arr[i] < 0:
            arr[i] = abs(arr[i])

getAbs(X, N)

for k in X:
    print(k, end = " ")