str = input()
length = len(str)

if length % 2 == 0:
    for i in range(length-1, 0, -2):
        print(str[i], end = '')
else:
    for i in range(length-1, 0, -2):
        print(str[i-1], end = '')