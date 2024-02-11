a, b = map(int, input().split())
answer = []
x = 0
for i in range(10):
    
    if i == 0 :
        answer.append(a)
    elif i == 1 :
        answer.append(b)
    else :
        x = 2*answer[i-2] + answer[i-1]
        answer.append(x)
    
    print(f'{answer[i]} ', end="")