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


# small Re example 
# import re
# s = "This log is at 25-09-2021 10:11AM"

# m = re.search(r'\d.*\s\d.*',s)
# print(m.group(0))

# import re 
# s = "AT^m89*365423"
# m = re.findall(r'[^a-z*][0-9]+',s)             # only no match
# print(m)