# How to find perticular pattern from the file having list of strings
import re

path = r"D:/Assignments/temp.txt"
l=[]

with open(path) as fd:
    l=fd.readlines()

for i in l :
    m = re.search(r'\d+-\w+\W\d+',i).group(0)                                  # Try to match complete pattern with the string provided 
    print(m)


## FILE CONTENT ###
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021
# This log is from 24-Aug 2021