n = int(input())

for i in range(1, n):
    if i == 1:
        for _ in range (n):
            print("*", end = " ")
        print()
    elif i == 2:
        print("*", end = " ")
        print()
    else :
        for j in range(1, n-1):
            for k in range(n-j):
                print("*", end = " ")
            print()
print()