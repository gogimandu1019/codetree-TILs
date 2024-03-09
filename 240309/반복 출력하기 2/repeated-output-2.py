n = int(input())

def recursive_print(x):
    if x == 0:
        return

    recursive_print(x-1)    
    print("HelloWorld")

recursive_print(4)