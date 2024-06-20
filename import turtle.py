import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra(radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color("navy")
    turtle.width(2)
    turtle.circle(radius)
    
    # Draw 24 spokes
    for _ in range(24):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.left(15)

def draw_indian_flag():
    screen = turtle.Screen()
    screen.title("Flag of India")
    screen.setup(width=800, height=600)

    turtle.speed(0)  # Speed up the drawing

    # Width and height of the flag
    width = 600
    height = 400
    stripe_height = height / 3

    # Starting coordinates
    start_x = -300
    start_y = 200

    # Draw saffron stripe
    draw_rectangle("orange", start_x, start_y, width, stripe_height)

    # Draw white stripe
    draw_rectangle("white", start_x, start_y - stripe_height, width, stripe_height)

    # Draw green stripe
    draw_rectangle("green", start_x, start_y - 2 * stripe_height, width, stripe_height)

    # Draw Ashoka Chakra
    chakra_radius = stripe_height / 2.5
    draw_chakra(chakra_radius, start_x + width / 2, start_y - height / 2)

    turtle.hideturtle()
    turtle.done()

draw_indian_flag()