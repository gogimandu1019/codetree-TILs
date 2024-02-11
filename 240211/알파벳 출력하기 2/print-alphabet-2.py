n = int(input())
x = ord('A')

for i in range(n):
    for j in range(n):
        if i <= j:        
            print(chr(x), end= " ")
            x = x + 1
            if x > ord('Z'):
                x = ord('A')
        else :
            print("", end = "  ")
    print()