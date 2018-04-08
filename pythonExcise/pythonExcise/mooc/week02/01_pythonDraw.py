import turtle

turtle.setup(800,350, 200, 200)     # (width, height, startx, starty)

turtle.penup()                      # raise the pen up so the next line won't draw
turtle.fd(-250)                     # moving to the right  
turtle.pendown()                    # put the pen back to the paint cloth, the window
turtle.pensize(25)
turtle.pencolor("purple")

turtle.seth(-40)                    # moving to the angle of 

for i in range (4):
    turtle.circle(40, 80)           # (radius, arc), the center of the circle is to the left of the turtle at the current position. 
    turtle.circle(-40, 80)

turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
turtle.done()