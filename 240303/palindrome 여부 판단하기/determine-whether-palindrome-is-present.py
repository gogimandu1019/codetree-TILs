A = list(input())

def palindrome(x):
    length = len(x)
    for i in range(length):
        if x[i] != x[length - 1 - i]:
            return False
        else:
            return True

if palindrome(A):
    print("Yes")
else:
    print("No")