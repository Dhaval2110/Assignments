# Bitwise Examples

# 1.Print the no of set bits in an integer

# n = 1
# c=0
# for i in range(0,31):
#     if n & 1<<i :
#         c +=1

# print(c)

# Set,clear and toggle bits

# n = 10
# p=0

# set = n | (1<<p)
# clear = n & ~(1<<p)
# toggle = n ^ (1<<p)

# print(set,clear,toggle)

# check if 2 no have opposite signs
# a = -10
# b = 20

# if a^b < 1 :                                    # ex-or would be less than 1
#     print("Opposite")
# else : 
#     print("Not")



#Swap the bits in integar

n = 761622921

n1 = (n & 0xAAAAAAAA)  >> 1                      # mask all the EVEN bits and right sift 
n2 = (n & 0x5555555) << 1                        # mask all the ODD bits and left shit 

n = n1 | n2                                      # merge them 
print(n)

# # Swap nibbles
# n = 100
# n3 = ( n & 0xF0) >> 4
# n4 = ( n & 0x0F) << 4

# n = n3 | n4
# print(n)

# Python code for swapping given bits of a number
# def swapBits(n, p1, p2):
 
#   # left-shift 1 p1 and p2 times
#   # and using XOR
#   n ^= 1 << p1
#   n ^= 1 << p2
#   return n
 
# # Driver Code
# print("Result =",swapBits(28, 0, 3))
 