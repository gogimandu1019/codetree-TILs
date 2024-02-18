str1 = list(input())
str2 = list(input())
x = ""
y = ""

for i in range(len(str1)):
    if str.isdigit(str1[i]) == True:
        x = x + ''.join(str1[i])
    else :
        continue;


for i in range(len(str2)):
    if str.isdigit(str2[i]) == True:
        y = y + ''.join(str2[i])
    else :
        continue;


print(x+y)