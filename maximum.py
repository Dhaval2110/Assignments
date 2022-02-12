#max

l = [1,3,4,5,7,9,11,2,5,10,6]

#print(max(l))
max = l[0]

def ma(l):
    global max
    for i in l:
        if i>max:
            max = i
        else:
            pass
    return max
max=ma(l)
print(max)
