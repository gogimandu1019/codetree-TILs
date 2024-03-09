N = int(input())


def print_star(x):
    if x == 0:
        return

    print_star(x-1)
    
    print("*" * x)


print_star(N)