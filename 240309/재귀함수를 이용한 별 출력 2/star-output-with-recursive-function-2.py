N = int(input())

def recursive_print(x):
    if x == 0:
        return
    print("* " * x, end = ' ')
    print()
    recursive_print(x-1)
    print("* " * x, end = ' ')
    print()

recursive_print(N)