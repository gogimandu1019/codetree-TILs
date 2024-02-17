n = int(input())
arr = []
cnt = 0
lensum = 0
average = 0

for i in range(n):
    inptstring = input()
    arr.append(inptstring)

cond = input()

for i in range(0, n):
    if arr[i][0] == cond:
        cnt += 1
        lensum += len(arr[i])

if cnt != 0:
    average = round(lensum / cnt, 2)
else:
    average = 0
    

print(f'{cnt} {average :.2f}')