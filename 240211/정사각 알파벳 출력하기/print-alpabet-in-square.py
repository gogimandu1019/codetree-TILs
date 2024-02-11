n = int(input())
x = ord('A')


for _ in range(n):
    for _ in range(n):
        print(chr(x), end= "")
        x = x + 1
    print()