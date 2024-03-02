n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def chkContinuePart(x,y,Z,Q):
    flag = False

    for i in range(x):
        if x < y:
            flag = False
            break;
        else:
            if Z[i] == Q[0]:
                for j in range(0, y):
                    if Z[i] == Q[j]:
                        flag = True
                    else:
                        i += 1
            else:
                if i < x:
                    i += 1
                    continue;
                else:
                    flag = False
                    break;
        
    if flag == False:
        print("No")
    elif flag == True:
        print("Yes")



chkContinuePart(n1,n2,A,B)