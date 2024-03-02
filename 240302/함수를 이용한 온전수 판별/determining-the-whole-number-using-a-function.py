a, b = map(int, input().split())
perfect_cnt = 0

def chkPerfect(x):
    if x % 2 == 0: #2로나누어떨어짐
        return 0
    else:
        if x % 10 == 5:
            return 0
        else:
            if x % 3 == 0 and x % 9 != 0:   #3으로 나누어 떨어지는데 9로는 나누어떨어지지 않음
                return 0
            else:
                return 1


for i in range(a, b+1):
    perfect_cnt += chkPerfect(i)


print(perfect_cnt)