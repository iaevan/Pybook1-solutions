import turtle
x = 0
y = 1
z = 0

n = 12

for i in range(n):
    z = x + y
    x = y
    y = z
    print(x)
    for i in range(4):
        turtle.forward(x*10)      
        turtle.left(90)
    turtle.circle(x * 10 , 90)