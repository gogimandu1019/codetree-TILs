n = int(input())

def sayYesOrNo(x):
    a = x // 10 #10의자리
    b = x % 10 #1의자리

    if x % 2 == 0:  #짝수
        if (a+b) % 5 == 0:  #자리합이 5의배수
            print("Yes")
        else:
            print("No")
    else:
        print("No")


sayYesOrNo(n)