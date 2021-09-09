# How to print first 10 letters of a file

import os
import sys

l=[]
with open ('C:/Users/Dhaval/Desktop/temp.txt') as fd:
    l = fd.readlines()

print(l[0][:10])                                                               # First 10 only chars
#print(l[0:10])                                                                 # first 10 lines