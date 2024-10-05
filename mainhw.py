import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(800 , 800)
turtle.title("Rectangle")
Rectangle = turtle.Turtle()

length = 200
width = 100


for i in range(2):
    turtle.forward(length)   
    turtle.right(90)         
    turtle.forward(width)   
    turtle.right(90)         

turtle.done()
