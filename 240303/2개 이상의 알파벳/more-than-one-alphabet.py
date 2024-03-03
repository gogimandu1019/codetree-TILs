A = list(input())
ascii = [0] * 26

#ord('a')=97, ord('z')=122
def asciiChk(X):
    result = False
    for char in X:
        ascii[ord(char) - 97] += 1
        if ascii[ord(char) - 97] == 2:
            result = True
            return result
            break;
    
    return result


if asciiChk(A):
    print("Yes")
else:
    print("No")