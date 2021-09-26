#second largest :


l = [10,21,1,5,3,89]

m = max(l[0],l[1])
s = min(l[0],l[1])

for i in range(2,len(l)):
    if l[i] > m :
        s= m
        m = l[i]

    elif l[i] > s:
        s = l[i]

print(s)


