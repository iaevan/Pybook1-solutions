x = str(input("enter a string: "))
y = len(x) -1
z = x[y]

for i in range(len(x)-1):

    y = y-1
    z += x[y]
    
if z == x:
    print("the word " + x + " is a palindrome")
else:
    print("the word " + x + " is not a palindrome")
