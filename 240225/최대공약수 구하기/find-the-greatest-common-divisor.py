n, m = map(int, input().split())


def maxi(x, y):
    i = 1
    k = 0
    for _ in range(1, min(x,y) + 1):
        if (x % i == 0) and (y % i == 0):
            k = i
            i += 1
        else:
            i += 1

        if i > min(x,y):
            break;

    return k


print(maxi(n, m))