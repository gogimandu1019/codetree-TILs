n = int(input())


# 모양에 맞게 별을 출력합니다.
for i in range(n):
    for _ in range(n - i):
        print("*", end="")
    for _ in range(2 * i):
        print(" ", end="")
    for _ in range(n - i):
        print("*", end="")
    print()