def mult(i):
    for x in range(1,11):
        print(i, "X" ,x ,"=" ,i*x)
try:
    mult(float(input("Enter a number for multiplication table:")))
except:
    mult(1)
