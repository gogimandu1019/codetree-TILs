N = int(input())
X = list(map(int, input().split()))

def divid2(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)

divid2(X)

for k in X:
    print(k, end = " ")