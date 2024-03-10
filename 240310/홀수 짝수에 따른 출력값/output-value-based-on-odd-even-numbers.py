N = int(input())


def f(x):
    summ = 0

    if x == 1 or x == 2:
        summ = x
        return summ

    summ = f(x-2) + x
    return summ

print(f(N))