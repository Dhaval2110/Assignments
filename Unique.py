# Find the unique number from the sequence

lList = [7,2,1,2,1,3,7]
res = lList[0]                                                                 # Suppose first element is uniqe 

for i in range(1,len(lList)):
    res = res ^ lList[i]

# X-or of number with number is 0.
# X-or of number with 0 is number.

print(res)


