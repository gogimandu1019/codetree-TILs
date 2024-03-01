N = int(input())


def sum1ton(x):
    summ = 0
    for i in range(1, x+1):
        summ += i

    summ = summ // 10

    return summ


print(sum1ton(N))