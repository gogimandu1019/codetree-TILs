a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if a % 3 == 0:
    if b % 3 == 0:
        if c % 3 == 0:
            if d % 3 == 0:
                if e % 3 == 0:
                    print(1)
                else:
                    print(0)
            else:
                print(0)
        else:
            print(0)
    else :
        print(0)
else :
    print(0)