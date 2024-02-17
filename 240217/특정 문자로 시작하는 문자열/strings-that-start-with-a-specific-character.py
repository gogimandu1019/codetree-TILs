n = int(input())
str1 = input()
str2 = input()
str3 = input()
str4 = input()
cond = input()

cnt = 0
lensum = 0

if str1.startswith(cond):
    cnt = cnt + 1
    lensum = lensum + len(str1)

if str2.startswith(cond):
    cnt = cnt + 1
    lensum = lensum + len(str2)

if str3.startswith(cond):
    cnt = cnt + 1
    lensum = lensum + len(str3)

if str4.startswith(cond):
    cnt = cnt + 1
    lensum = lensum + len(str4)
    

print(f'{cnt} {lensum/cnt :.2f}')