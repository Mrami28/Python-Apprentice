import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 50,30,50 ]
lefts = [ 45,90,45 ]
colors = [ "red" ]

for  i in range(8):

    forward = [ 50,30,50 ]
    left = [ 45,90,45 ]
    color = [ "red" ]


    tina.color("red")
    tina.forward(50,30,50)
    tina.left( 45,90,45)

turtle.exitonclick()  

