'''def is_prime1(n):
    if n<2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divided by", x)
            prime = False
            return prime
    return prime

def is_prime2(n):
    if n<2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divided by", x)
            prime = False
            return prime
    return prime

def is_prime3(n):
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
    return prime'''

import math

def is_prime4(n):
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



while True:
    number = input("please input a number(not 0 you bitch!): ")
    number = int(number)

    if number == 0:
        break
    prime = is_prime4(number)
    if prime is True:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime")
