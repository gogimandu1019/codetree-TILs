arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    summ = 0
    avg = 0
    for j in range(4):
        summ += arr[i][j]
        if j == 3:
            avg = summ / 4
            print(avg, end = " ")

print()

for j in range(4):
    summ = 0
    avg = 0
    for i in range(2):
        summ += arr[i][j]
        if i == 1:
            avg = summ / 2
            print(avg, end = " ")

print()

summ = 0
avg = 0
for i in range(2):
    for j in range(4):
        summ += arr[i][j]
avg = summ / 8
print(avg)