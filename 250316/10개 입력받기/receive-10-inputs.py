arr = list(map(int, input().split()))
n = len(arr)
summ = 0
avg = 0
k = 0
j = 0
for i in range(n):
    if arr[i] == 0:
        k = i
        break;
    else :
        summ += arr[i]
        k = k + 1
if k != 0:
    avg = round(summ / k, 1)
    
print(f'{summ} {avg}')