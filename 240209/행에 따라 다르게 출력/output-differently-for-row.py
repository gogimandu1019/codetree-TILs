n = int(input())
x = 1

for i in range(0, n):
    for j in range(0, n):
        print(x, end = " ")
        if(j != n-1):
            if(i % 2 == 0):
                x = x + 1
            else :
                x = x + 2
    if i % 2 == 0:
        x = x + 2
    else : 
        x = x + 1
    print()