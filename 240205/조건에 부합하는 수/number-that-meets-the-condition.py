a = int(input())

for i in range (1, a+1):
    if i % 2 == 0 and i % 4 != 0:
        continue;
    elif int(i // 8) % 2 == 0:
        continue;
    elif i % 7 < 4:
        continue;
    else:
        print(f"{i}", end = " ")