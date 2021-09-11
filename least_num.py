# find the least common numbers in the list

a=[1,7,2,1,4,1,2,4,2]

c=len(a)
least = 0
for i in a:
    if a.count(i)<=c:
        c=a.count(i)
        least=i
    
print(least)