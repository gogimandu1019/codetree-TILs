n = int(input())
x= 0
concat = ""
for i in range(n, 0 , -1): 
    for j in range(1, i+1):
        x = n-i+1
        if j != i:
            concat = "/ "
        else:
            concat = ""
        print(f'{x} * {j} = {x*j} ', end = concat)
        

    print()