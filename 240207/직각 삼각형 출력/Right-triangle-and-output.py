n = int(input())
cnt = 0

for i in range (n):
    cnt = i * 2 + 1;
    for j in range(cnt):
        print("*", end = "")
    print()