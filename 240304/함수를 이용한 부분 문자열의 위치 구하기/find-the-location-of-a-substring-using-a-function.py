X = input()
Y = input()

def chkIdx():
    flag = False
    for i in range(len(X)):
        if X[i:i+len(Y)] == Y:
            flag = True
            print(i)
    if flag == False:
        print(-1)

chkIdx()