str1 = list(input())
str2 = list(input())
x = ""
for i in range(len(str1)):
    if int(str1[i]) >= 0 and int(str1[i]) <= 9:
        x = ''.join(str1[i])
        print(x)
    else :
        continue;