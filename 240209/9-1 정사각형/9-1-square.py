n = int(input())
k = 9
for i in range(1, n+1, 1):
    for j in range(0, n, 1):
        print(k, end = "")
        k = k-1
        if k == 0:
            k = 9
    print()