from cmu_graphics import *

app.background = 'green'

# Variables
circle_rover = Circle(200, 200, 10, fill='pink')

# Goal 1
Line(100, 50, 300, 50, lineWidth=6, fill='white')
Line(100, 50, 100, 0, lineWidth=6, fill='white')
Line(300, 50, 300, 0, lineWidth=6, fill='white')

# Goal 2
Line(100, 350, 300, 350, lineWidth=6, fill='white')
Line(100, 350, 100, 400, lineWidth=6, fill='white')
Line(300, 350, 300, 400, lineWidth=6, fill='white')

# Midfield
Line(0, 200, 400, 200, lineWidth=4.5, fill='white')
Circle(200, 200, 50, fill=None, border='white', borderWidth=4.5)


# Function 1
def onMousePress(mouseX, mouseY):
    circle_rover.centerX = mouseX
    circle_rover.centerY = mouseY


# Runs the program
cmu_graphics.run()
