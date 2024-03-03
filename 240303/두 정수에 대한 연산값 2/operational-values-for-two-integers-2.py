a, b = map(int, input().split())

def modify(x,y):
    if x < y:
        x = x + 10
        y = y * 2
    else:
        x = x * 2
        y = y + 10

    return x,y

a, b = modify(a, b)
print(f'{a} {b}')