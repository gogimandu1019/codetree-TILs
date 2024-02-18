n = int(input())
arr = [0]*n
summ = 0
answer = ""
summ_str = ""

for i in range(n):
    arr[i] = int(input())
    summ += arr[i]

summ_str = str(summ)

for j in range(0, len(summ_str), 1):
    answer = summ_str[1:] + summ_str[0]

print(answer)