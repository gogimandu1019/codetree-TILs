#L : 맨 앞글자를 맨 뒤로
#R : 맨 뒷글자를 맨 앞으로

strr = input()
command = input()
x = len(strr)
for i in range(len(command)):
    if command[i] == "L":
        strr = strr[1:] + strr[0]
    elif command[i] == "R":
        strr = strr[x-1] + strr[0:x-1]
    else:
        print("NO")
    
print(strr)