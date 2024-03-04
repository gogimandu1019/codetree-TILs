arr = [list(input().split()) for _ in range(5)]
answer = [[0,0,0]] * 5

for i in range(5):
    for j in range(3):
        answer[i][j] = arr[i][j].upper()
        print(answer[i][j], end = ' ')
    print()