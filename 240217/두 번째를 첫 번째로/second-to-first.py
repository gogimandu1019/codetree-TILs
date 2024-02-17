strr = input()
frst = strr[0]
scnd = strr[1]


for i in range(0, len(strr), 1):
    if strr[i] == scnd:
        strr = strr[:i] + strr[0] + strr[i + 1:]


print(strr)