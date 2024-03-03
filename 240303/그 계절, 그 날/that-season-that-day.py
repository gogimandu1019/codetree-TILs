Y,M,D = map(int, input().split())

def chkLeapYear(k):
    leapyn = True
    if k % 4 == 0:
        if k % 100 == 0:
            if k % 400 == 0:
                leapyn = True
            else:
                leapyn = False
        else:
            leapyn = True
    else:
        leapyn = False    

    return leapyn

def chkExistDate(x, y, z):
    result = True

    if y < 1 or y > 12:
        result = False
    
    if z < 1 or z > 31:
        result = False
    
    if y == 2 :
        if z > 29:
            result = False
        else:
            if chkLeapYear(x) == True:
                if z >= 30:
                    result = False
                else:
                    result = True
            else:
                if z >= 29:
                    result = False
                else:
                    result = True                
    
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        if z < 1 or z > 31:
            result = False
        else :
            result = True
    elif y == 4 or y == 6 or y == 9 or y == 11:
        if z < 1 or z > 30:
            result = False
        else:
            result = True
    
    return result


def chkSeason(x,y,z):
    if chkExistDate(x,y,z) == True :
        if y >= 3 and y <= 5:
            print("Spring")
        elif y >= 6 and y <= 8 :
            print("Summer")
        elif y >= 9 and y <= 11:
            print("Fall")
        elif y == 12 or y == 1 or y == 2:
            print("Winter")
        else:
            print(-1)
    else:
        print(-1)



chkSeason(Y,M,D)