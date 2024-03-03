A = list(input())

def havingMoreTwo(X):
    if len(X) == 1:
        return False

    for i in range(len(X)):
        if X[i] != X[0]:
            return True
    
    return False


if havingMoreTwo(A):
    print("Yes")
else:
    print("No")