M, D = map(int, input().split())

def chkExistDate2021(x, y):
    result = True

    if x < 1 or x > 12:
        result = False
    
    if y < 1 or y > 31:
        result = False
    
    if x == 2 and y > 29: #2월은 28일까지
        result = False
    
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        if y < 1 or y > 31:
            result = False
    elif x == 4 or x == 6 or x == 9 or x == 11:
        if y < 1 or y > 30:
            result = False
    
    return result


if chkExistDate2021(M,D) :
    print("Yes")
else:
    print("No")