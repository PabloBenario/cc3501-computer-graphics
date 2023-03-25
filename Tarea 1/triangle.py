import pyglet
import math

# Define the size of the window
width = 640
height = 480

# Create a window with the defined size
window = pyglet.window.Window(width, height)

# Define the color of the triangle in RGB format


# Define the function to create an equilateral triangle
def equiTriangle(x, y, h, left , right , r , g , b):

    # Create the triangle object using the Triangle class
    triangle = pyglet.shapes.Triangle(x-left, y , x+right , y , x , y+h,  color = (r , g , b ))

    # Draw the triangle
    triangle.draw()

# Define the update function
def update(dt):
    pass

# Define the draw function
@window.event
def on_draw():
    window.clear()
    equiTriangle(0, 0, 100, 200 , 100 , 1, 255, 255)  # Example call to equiTriangle function


# Run the application
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
