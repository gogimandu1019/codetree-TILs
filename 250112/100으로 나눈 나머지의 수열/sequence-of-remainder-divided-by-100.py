N = int(input())

# Write your code here!
def sequence(n):
    x = 0
    if n == 1:
        x = 2
    elif n == 2:
        x= 4
    else:
        x= (sequence(n-1) * sequence(n-2)) % 100
    
    return x

print(sequence(N))