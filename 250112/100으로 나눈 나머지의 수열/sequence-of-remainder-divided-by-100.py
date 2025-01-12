N = int(input())

# Write your code here!
def re(N, a=2, b=4, i=3):
    while (i > 2):
        if i==N:
            return (a*b)%100

        return re(N, b, (a*b)%100, i+1)

print(re(N))
