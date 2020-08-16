x = str(input("enter a string: "))
up = ''
lo = ''
num = ''
oth = ''
for a in x:
    if (a.isupper()) == True:
        up += a
    elif (a.islower()) == True:
        lo += a
    elif (a.isdigit()) == True:
        num += a
    else:
        oth += a

print(up)
print(lo)
print(num)
print(oth)
