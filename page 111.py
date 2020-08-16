import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3,m,2):
        if n % x == 0:
            return False
    return True

prime_numbers = []

n1 = int(input("give me thi first number: "))
n2 = int(input("give me the last number: "))

if n1 > n2:
    print("FBI OPEN UP!")

for i in range(n1,n2):
    if is_prime(i) == True:
        prime_numbers.append(i)

print(prime_numbers)
