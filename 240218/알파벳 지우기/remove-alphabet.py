str1 = list(input())
str2 = list(input())
x = ""
y = ""


def getNumber(string):
    answer = ""
    for i in range(len(string)):
        if str.isdigit(string[i]) == True:
            answer = answer + ''.join(string[i])
        else :
            continue;
    return answer

x = getNumber(str1)
y = getNumber(str2)


print(int(x) + int(y))