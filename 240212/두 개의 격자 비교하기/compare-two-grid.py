n , m = map(int, input().split())

lst1 = [list(map(int,input().split())) for i in range(n)]
lst2 = [list(map(int,input().split())) for i in range(n)]
lst_answer = [[0 for i in range(n)] for i in range(m)]

for i in range(n):
    for j in range(m):
        if lst1[i][j] == lst2[i][j]:
            lst_answer[i][j] = 0
        else :
            lst_answer[i][j] = 1
        print(lst_answer[i][j], end = " ")       
    print()