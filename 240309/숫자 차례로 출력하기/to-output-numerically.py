N = int(input())

def recursive_print_down(x):
    if x == 0:
        print()
        return
    print(x, end = ' ')
    recursive_print_down(x-1)

def recursive_print_up(x):
    if x == 0:
        return
    
    recursive_print_up(x-1)
    
    if x == N:
        print(x)
    else:
        print(x, end = ' ')


recursive_print_up(N)
recursive_print_down(N)