# Rotate the list in clockwise

l=[4,5,6,1,2,3]
import time
print(l)
for i in range(1,len(l)+1):
	l=l[i:]+l[:i]
	time.sleep(2)
