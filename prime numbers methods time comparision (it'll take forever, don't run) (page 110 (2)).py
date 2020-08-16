import math

def is_prime1(n=1013):
    if n<2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divided by", x)
            prime = False
            return prime
    return prime

def is_prime2(n=1013):
    if n<2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divided by", x)
            prime = False
            return prime
    return prime

def is_prime3(n=1013):
    if n == 2:
        return True
    if n % 2 == 0:
        print(n, "is divisable by 2")
        return False
    if n < 2:
        return False
    prime = True
    for x in range(3,n,2):
        if n % x == 0:
            print(n, "is divisabel by", x)
            prime = False
            return prime
    return prime

def is_prime4(n=1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        print(n, "is divisable by 2")
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3,m,2):
        if n % x == 0:
            return False
    return True

import timeit
t1 = timeit.timeit(is_prime1)
t2 = timeit.timeit(is_prime2)
t3 = timeit.timeit(is_prime3)
t4 = timeit.timeit(is_prime4)

print("it took", t1, "seconds to run the 1st one")
print("it took", t2, "seconds to run the 2nd one")
print("it took", t3, "seconds to run the 3rd one")
print("it took", t4, "seconds to run the 4th one")