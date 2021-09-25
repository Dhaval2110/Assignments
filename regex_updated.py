# Regex examples

# small Re example 
# import re
# s = "This log is at 25-09-2021 10:11AM"

# m = re.search(r'\d.*\s\d.*',s)
# print(m.group(0))

# import re 
# s = "AT^m89*365423"
# m = re.findall(r'[^a-z*][0-9]+',s)             # only no match
# print(m)

import re
s1 = "Meet me at 11:20 AM"
s2 = "This is at 10:89"
s3 = "We can meet at 10:800"
s4 = " We are 23:15"

m = re.search(r'([012][0123]|[0-9]):[0-5][0-9]',s4)
print(m.group(0))