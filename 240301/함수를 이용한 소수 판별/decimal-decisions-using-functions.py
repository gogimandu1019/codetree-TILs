a, b= map(int, input().split())
summ = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(a, b+1):
    if i != 1:
        if is_prime(i):
            summ += i

print(summ)