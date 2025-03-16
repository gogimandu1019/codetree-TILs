arr = list(map(int, input().split()))

n = len(arr)
summ = 0
avg = 0
k = False
num = 0
for i in range(n):
    if arr[i] >= 250:
        k = True
        break;
    else :
        k = False
        num = i+1

if k == False:
    for i in range(n):
        summ = summ + arr[i]
    
    avg = round(summ / n, 1)
else :
    for i in range(num):
        summ = summ + arr[i]
    avg = round(summ / num, 1)

print(f'{summ} {avg}')
