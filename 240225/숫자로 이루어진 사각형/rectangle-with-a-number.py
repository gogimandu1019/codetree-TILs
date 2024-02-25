N = int(input())

def prt_square(x):
    i = 1
    for _ in range(x):
        for _ in range(x):
            print(i, end = " ")
            if i < 9 :
                i += 1
            elif i == 9:
                i = 1
            else :
                print("TOO BIG")
        print()


prt_square(N)