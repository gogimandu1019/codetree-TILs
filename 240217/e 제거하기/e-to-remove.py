strr = input()
for i in range(len(strr)):
    if strr[i] == "e":
        strr = strr[:i] + strr[i+1:]
        print(strr)
        break;