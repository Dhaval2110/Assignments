# anargram

s1= "bad"
s2 = "dad"


def anagram_logic1(s1,s2):
    flag = 0
    for i in s1:                                                               # check char by char
        if i not in s2:                                                        # check till character of string doesn't match with another string
            flag = 1
    if flag == 1 or len(s1) != len(s2) :                                       # Length of string should also be the same
        print("Strings are not anagram\n")  
    else : 
        print("Strings are anagarma\n")

def anagram_logic2(s1,s2):
    if sorted(s1) == sorted(s2):
        print("Strings are anagram")
    else:
        print("Strings are not anagram") 

anagram_logic1(s1,s2)
anagram_logic2(s1,s2)