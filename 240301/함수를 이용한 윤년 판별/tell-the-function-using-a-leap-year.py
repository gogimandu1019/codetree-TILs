y = int(input())
leapyn = "false"

def chkLeapYear(x):
    if x % 4 == 0:
        leapyn = "true"
    else:
        leapyn = "false"
    

    if x % 100 == 0 and x % 400 != 0:
        leapyn = "false"

    return leapyn


print(chkLeapYear(y))