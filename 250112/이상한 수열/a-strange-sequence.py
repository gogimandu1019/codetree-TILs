N = int(input())

# Write your code here!
def f(x):
    y = 0
    if x = 1:
        y = 1
    elif  x = 2 :
        y = 2
    else :
        y = f(int(x/3)) + f(x-1)
    
    return y

f(N)