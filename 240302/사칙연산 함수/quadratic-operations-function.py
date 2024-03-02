a, o, c = tuple(input().split())
a = int(a)
c = int(c)
answer = 0
def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiple(x,y):
    return x * y

def divide(x,y):
    return int(x/y)

if o == "+":
    answer = plus(a,c)
    print(f'{a} + {c} = {answer}')
elif o == "-":
    answer = minus(a,c)
    print(f'{a} - {c} = {answer}')
elif o == "*":
    answer = multiple(a,c)
    print(f'{a} * {c} = {answer}')
elif o == "/":
    answer = divide(a,c)
    print(f'{a} / {c} = {answer}')
else:
    print("False")