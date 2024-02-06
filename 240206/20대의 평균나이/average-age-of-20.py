age = list(range(100))
sum = 0
average = 0
cnt = 0
for i in range(0, 100):
    age[i] = int(input())
    

    if ((age[i] >= 30) or (age[i] < 20)):
        break;
    else :
        sum = sum + age[i]
        cnt = cnt + 1



average =round(sum / cnt,2)

print(f'{average:.2f}')