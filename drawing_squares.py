import turtle # Use this to be able to draw on the screen

def draw_square():
# this creates a surface for the turtle to draw on 
    window = turtle.Screen()

# this changes the surface's background color
    window.bgcolor('blue')

# this renames the turtle so you can call it later on    
    line = turtle.Turtle()

# this changes the shape of the turtle(can initially only be certain polygonal shapes or the turtle)
    line.shape('turtle')

# change the color of the turtle
    line.color('yellow')

# making turtle draw a square below
    line.speed(1)
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    
# this closes the window once you click on it. 
    window.exitonclick()
    
draw_square()
    
