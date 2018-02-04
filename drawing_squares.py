import turtle # Use this to be able to draw on the screen

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('black')
    draw_square()
    draw_circle()
    draw_triangle()
    draw_octagon()

    # this closes the window once you click on it. 
    window.exitonclick()

def draw_square():
    line = turtle.Turtle()
    line.shape('turtle')
    line.color('green')
    draw_square = 0
    while draw_square < 4:
        line.speed(3)
        line.forward(100)
        line.right(90)
        draw_square = draw_square + 1
    
def draw_circle():
    circle = turtle.Turtle()
    circle.shape('turtle')
    circle.color('red')
    circle.seth(180)
    circle.left(45)
    circle.circle(73)

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape('arrow')
    triangle.color('yellow')
    triangle.seth(270)
    make_triangle = 0
    while make_triangle < 3:
        triangle.forward(100)
        triangle.left(120)
        make_triangle = make_triangle + 1

def draw_octagon():
    octagon = turtle.Turtle()
    octagon.shape('turtle')
    octagon.color('blue')
    octagon.seth(180)
    octagon.left(45)
    make_oct = 0
    while make_oct < 8:
        octagon.forward(58)
        octagon.left(45)
        make_oct = make_oct + 1
        
    
        

draw_shapes()        
        
        
        
    
    
    
    

