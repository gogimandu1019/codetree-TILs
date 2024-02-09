n = int(input())
for i in range (n, 0, -1):
    for j in range(i, n+1):
        if(j >= i):
            print(j, end = " ")
    print()