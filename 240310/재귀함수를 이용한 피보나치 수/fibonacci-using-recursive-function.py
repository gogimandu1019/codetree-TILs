N = int(input())

def f(x):
    result = 0
    if x == 1 or x == 2:
        result = 1
        return result


    result = f(x-1) + f(x-2)
    return result

print(f(N))