#Krista and Rosemary
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 2:
        jack.color("blue")
    if side == 3:
        jack.color("violet")
    jack.forward(100)
    jack.right(90)

    
