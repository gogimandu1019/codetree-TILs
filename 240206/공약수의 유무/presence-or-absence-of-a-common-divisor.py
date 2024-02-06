a, b = map(int, input().split())

gys = 0

for i in range(a, b+1):
    if ((1920 % i == 0) and (2880 % i == 0)):
        gys = i
        break;
    else : 
        gys = 0

if gys == 0:
    print(0)
else :
    print(1)