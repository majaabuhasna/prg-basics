###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures

length = 100
length_a = 50
length_b = 150

pen.penup()
pen.goto(0,0)
pen.pendown()

figures.draw_square(pen, length)

pen.penup()
pen.goto(200,0)
pen.pendown()

figures.draw_triangle(pen, length)

pen.penup()
pen.goto(400,0)
pen.pendown()

figures.draw_rectangle(pen, length_a, length_b)

pen.penup()
pen.goto(0,400)
pen.pendown()

figures.draw_square(pen, length)

pen.penup()
pen.goto(200,400)
pen.pendown()

figures.draw_triangle(pen, length)

pen.penup()
pen.goto(400,400)
pen.pendown()

figures.draw_rectangle(pen, length_a, length_b)




# Hide the turtle and finish
pen.hideturtle()
window.mainloop()