n = int(input())
x = 0
for i in range(1, n+1, 1):
    for j in range(n, 0, -1):
        print(i*j, end = " ")
    print()