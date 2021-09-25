# prime no

def prime(n):
    c = 1
    for i in range(2,n):
        if n % i == 0 :
            c = 0

    if c == 1:
        print("Prime")
    else:
        print("Not")

    
prime(11)