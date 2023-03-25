from pyglet.window import Window, key, mouse
from pyglet.shapes import Circle, Star
from pyglet.app import run
from pyglet.graphics import Batch
import pyglet
import random
import numpy as np
import math
#debe usarse una ventana cuadrada
SIZE = 700
WIDTH = SIZE
HEIGHT = SIZE
WINDOW_TITLE = 'Tarea 1'
FULL_SCREEN = False
NUMBER_OF_STARS = 500


ventana = Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable=True)

star = Batch()


star_array = np.empty(NUMBER_OF_STARS, dtype=object)

#initialization of stars
for i in range(NUMBER_OF_STARS):
    randX = random.randint(0,  SIZE)
    #el 2SIZE de la cord Y es aproposito para que se genera aleatoriamente fuera de pantalla y no haga un efecto extraño
    randY = random.randint(0, 2*SIZE)
    star_array[i]= (Circle(randX, randY, radius=SIZE/400, color = (255, 255, 255), batch = star ))



def equiTriangleS(x, y, h, left , right , r , g , b, scale):
    # Create the triangle object using the Triangle class

    xf = x*scale
    yf = y*scale

    v = x - xf
    w = y - yf




    triangle = pyglet.shapes.Triangle(  v +  (x-left)*scale, w+y*scale , v+(x+right)*scale , y*scale+w , v+x*scale , (y+h)*scale+ w,  color = (r , g , b ))

    # Draw the triangle
    triangle.draw()


# Define the function to create an equilateral triangle
def equiTriangle(x, y, h, left , right , r , g , b):
    # Create the triangle object using the Triangle class

    triangle = pyglet.shapes.Triangle(x-left, y , x+right , y , x , y+h,  color = (r , g , b ))

    # Draw the triangle
    triangle.draw()



# t1 = pyglet.shapes.Triangle(
#     SIZE/2-SIZE/50, SIZE/2,
#     SIZE/2 - 2*SIZE/50 , SIZE/2 + SIZE/50,
#     SIZE/2 - 3*SIZE/50 , SIZE/2 - SIZE/15,
#     color=(0,255,0),
#     )

# t2 = pyglet.shapes.Triangle(
#     SIZE/2+SIZE/50, SIZE/2,
#     SIZE/2 + 2*SIZE/50 , SIZE/2 + SIZE/50,
#     SIZE/2 + 3*SIZE/50 , SIZE/2 - SIZE/15,
#     color=(0,255,0),
#     )

def update(dt):
    for i in range(NUMBER_OF_STARS):
        staruwu = star_array[i]
        staruwu.y -= 180*dt
        if staruwu.y<=0:
            randomX = random.randint(0,SIZE)
            randomY = random.randint(SIZE, 2*SIZE)
            star_array[i] = (Circle(randomX,randomY , radius=SIZE/400, color = (255, 255, 255), batch = star ))
        

def showNavePrincipal(x , y ):
    equiTriangle(x, y, SIZE/10, SIZE/50 , SIZE/50 , 0, 255, 0)  
    equiTriangle(x, y , -SIZE/35 , SIZE/50 , SIZE/50 , 0, 255, 0 )

    equiTriangle(x-SIZE/50 , y , SIZE/20 , SIZE/100 , SIZE/100 , 255 , 0 , 0)
    equiTriangle(x+SIZE/50 , y , SIZE/20 , SIZE/100 , SIZE/100 , 255 , 0 , 0)

    equiTriangle(x-SIZE/50 , y , -SIZE/15, SIZE/100 , SIZE/100 , 255 , 0 , 0 )
    equiTriangle(x+SIZE/50 , y , -SIZE/15, SIZE/100 , SIZE/100 , 255 , 0 , 0 )


    t1 = pyglet.shapes.Triangle(
    x-SIZE/50, y,
    x - 2*SIZE/50 , y + SIZE/50,
    x - 3*SIZE/50 , y - SIZE/15,
    color=(0,255,0),
    )

    t2 = pyglet.shapes.Triangle(
    x+SIZE/50, y,
    x + 2*SIZE/50 , y + SIZE/50,
    x + 3*SIZE/50 , y - SIZE/15,
    color=(0,255,0),
    )

    star1 = pyglet.shapes.Star(
        x= x-SIZE/50,
        y= y,
        outer_radius=4*SIZE/400,
        inner_radius=4*SIZE/200,
        num_spikes=4,
        color=(255,255,0)
    )
    star2 = pyglet.shapes.Star(
        x= x+SIZE/50,
        y= y,
        outer_radius=4*SIZE/400,
        inner_radius=4*SIZE/200,
        num_spikes=4,
        color=(255,255,0)
    )
    t1.draw()
    t2.draw()
    star1.draw()
    star2.draw()

def naveChica(x,y): 
    equiTriangle(x,y, 20 , 20 , 20 , 0 , 0, 255)
    equiTriangleS(x,y , 20 , 20 , 20 , 250, 250 , 0 , 0.5)
@ventana.event
def on_draw():
    ventana.clear()
    star.draw()
    #main body nave principal ><
    #verde
    # equiTriangle(SIZE/2, SIZE/2, SIZE/10, SIZE/50 , SIZE/50 , 0, 255, 0)  
    # equiTriangle(SIZE/2, SIZE/2 , -SIZE/35 , SIZE/50 , SIZE/50 , 0, 255, 0 )
    

    # #rojo 
    # equiTriangle(SIZE/2-SIZE/50 , SIZE/2 , SIZE/20 , SIZE/100 , SIZE/100 , 255 , 0 , 0)
    # equiTriangle(SIZE/2+SIZE/50 , SIZE/2 , SIZE/20 , SIZE/100 , SIZE/100 , 255 , 0 , 0)

    # #rojo
    # equiTriangle(SIZE/2-SIZE/50 , SIZE/2 , -SIZE/15, SIZE/100 , SIZE/100 , 255 , 0 , 0 )
    # equiTriangle(SIZE/2+SIZE/50 , SIZE/2 , -SIZE/15, SIZE/100 , SIZE/100 , 255 , 0 , 0 )

    # t1.draw()
    # t2.draw()
    showNavePrincipal(SIZE/2 , SIZE/2*1.25)
    showNavePrincipal(SIZE/2,SIZE/2*1.25 - SIZE/4 )
    
    naveChica(650, 650)
    





















pyglet.clock.schedule_interval(update, 1/60.0)

run()