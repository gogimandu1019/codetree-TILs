n, m = map(int, input().split())

def prt_square(x,y):
    for _ in range(x):
        for _ in range(y):
            print("1", end="")
        print()


prt_square(n,m)