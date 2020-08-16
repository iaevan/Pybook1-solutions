x = str(input("enter a string: "))
a =''
l = 1
a += x[l]


for i in x:
    a += x[l-1]
    l = l-1
    try:
        a += x[l+3]
        l = l+3
    except:
        break

print(a)
