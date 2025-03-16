arr = list(map(int, input().split()))
summ = 0
cnt = 0

for i in range(10):
    if arr[i] == 0:
        break;
    else:
        if arr[i] % 2 == 0:
            cnt += 1
            summ += arr[i]


print(f'{cnt} {summ}')

    
