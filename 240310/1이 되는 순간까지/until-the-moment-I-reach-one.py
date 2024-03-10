N = int(input())


def f(x):
    cnt = 0

    if x == 1:
        return cnt
    
    if x % 2 == 0:
        cnt = f(x // 2) + 1
    else:
        cnt = f(x // 3) + 1
    return cnt




print(f(N))