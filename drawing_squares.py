import turtle # Use this to be able to draw on the screen
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('black')
    square = turtle.Turtle()
    square.shape('turtle')
    square.color('green')
    for i in range(1,37):
        draw_square(square)
        square.right(10)
            
    triangle = turtle.Turtle()
    triangle.shape('arrow')
    triangle.color('yellow')
    triangle.seth(270)
    for i in range(1,37):
        draw_triangle(triangle)
        triangle.left(10)

    octagon = turtle.Turtle()
    octagon.shape('turtle')
    octagon.color('blue')
    for i in range(1,37):
        draw_octagon(octagon)
        octagon.right(10)

    circle = turtle.Turtle()
    circle.shape('turtle')
    circle.color('red')
    for i in range(1,37):
        draw_circle(circle)
        circle.left(10)
        
    window.exitonclick()

def draw_square(square_turtle):
    draw_square = 0
    while draw_square < 4:
        square_turtle.speed(100)
        square_turtle.forward(225)
        square_turtle.right(90)
        draw_square = draw_square + 1
    
def draw_triangle(triangle_turtle):
    triangle_turtle.speed(100)
    make_triangle = 0
    while make_triangle < 3:
        triangle_turtle.forward(185)
        triangle_turtle.left(120)
        make_triangle = make_triangle + 1

def draw_octagon(octo_turtle):
    make_oct = 0
    octo_turtle.speed(350)
    while make_oct < 8:
        octo_turtle.forward(50)
        octo_turtle.left(45)
        make_oct = make_oct + 1

def draw_circle(circle_turtle):
    circle_turtle.speed(150)
    circle_turtle.circle(160)

draw_shapes()        
        
        
        
    
    
    
    

