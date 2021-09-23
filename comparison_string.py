# Compare characters of 2 strings 

S1 = "This is Dhaval"
S2 = " I am Mehta"


def compare(a,b):
    for a,b in zip(a,b):
        print(a,b)                                                             # Zip will enclose strings in tuple so that every character will be matched
        # Output Would be
        # T --> Space
        # h --> I
        # i --> Space
        # s --> a ...
        if a == b :
            print(True)
        else:
            print(False)


compare(S1,S2)

