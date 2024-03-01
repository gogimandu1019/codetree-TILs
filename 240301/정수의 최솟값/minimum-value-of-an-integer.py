a, b, c = map(int, input().split())


def getMin(x,y,z):
    answer = 0
    answer = min(x,y,z)

    return answer


print(getMin(a,b,c))