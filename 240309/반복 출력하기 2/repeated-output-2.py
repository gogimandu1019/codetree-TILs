n = int(input())

def recursive_print(x):
    if x == 0:
        return

    print("HelloWorld")
    recursive_print(x-1)    

recursive_print(n)