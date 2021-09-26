# # Power of 2

# n = 1024

# if n & n-1 == 0 :
#     print("Power of 2")
# else :
#     print("Not power of 2 ")

# Rever the number

# n = 123
# s = 0
# while(n):
#    s = s * 10 + n % 10      # remove 10 so it will give sum of the number
#    n = n // 10

# print(s)

#  Reverse Bits of a Number

def reverse_mask(x):
    x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1)
    x = ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)
    x = ((x & 0x0F0F0F0F) << 4) | ((x & 0xF0F0F0F0) >> 4)
    x = ((x & 0x00FF00FF) << 8) | ((x & 0xFF00FF00) >> 8)
    x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16)
    return x

res = reverse_mask(10)
print(res)