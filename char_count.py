# Count char in file
l = []
with open (r'D:\Assignments\temp.txt') as fd:
    l = fd.readlines()
lenth = 0
for i in l :
    lenth += len(i)

print(lenth)