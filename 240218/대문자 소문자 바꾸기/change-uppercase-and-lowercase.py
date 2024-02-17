x = list(input())
for i in range (0,len(x)):
    if x[i].isupper():
        x[i] = x[i].lower()
    else:
        x[i] = x[i].upper()

print(''.join(x))