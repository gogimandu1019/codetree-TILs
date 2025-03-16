arr = list(map(int, input().split()))
n = len(arr)
summ = 0
avg = 0
k = 0
for i in range(n):
    if arr[i] == 0:
        k = i
        break;
    
    summ += arr[i]

avg = round(summ / k, 1)
print(f'{summ} {avg}')