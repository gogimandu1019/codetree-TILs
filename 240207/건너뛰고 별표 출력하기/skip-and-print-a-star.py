n = int(input())
cnt = 0

for i in range (1, n+1):
    cnt = i;
    for j in range(cnt):
        print("*", end = "")
    print()
    print()

for i in range(n-1, 0, -1):
    cnt = i;
    for j in range(cnt):
        print("*", end = "")
    print()
    print()