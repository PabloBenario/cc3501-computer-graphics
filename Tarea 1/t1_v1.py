from pyglet.window import Window, key, mouse
from pyglet.shapes import Circle, Star
from pyglet.app import run
from pyglet.graphics import Batch
import pyglet
import random
import numpy as np
WIDTH = 500
HEIGHT = 500
WINDOW_TITLE = 'Tarea 1'
FULL_SCREEN = False
NUMBER_OF_STARS = 300

ventana = Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable=True)

star = Batch()
star_array = np.empty(NUMBER_OF_STARS, dtype=object)


def StarShip(x , y ):
    return Star( x= x , y=y , outer_radius= 20 , inner_radius= 10, rotation = 3 , num_spikes=3 , color= (255, 255, 255) , batch=star ,  )
    
shipi1  =  StarShip(WIDTH/2 , HEIGHT/2)

for i in range(NUMBER_OF_STARS):
    randX = random.randint(0,  WIDTH)
    randY = random.randint(0, HEIGHT)
    star_array[i]= (Circle(randX, randY, radius=4, color = (255, 255, 255), batch = star ))




def update(dt):
    for i in range(NUMBER_OF_STARS):
        staruwu = star_array[i]
        staruwu.y -= 200*dt
        if staruwu.y<=0:
            randomX = random.randint(0,WIDTH)
            star_array[i] = (Circle(randomX, HEIGHT, radius=4, color = (255, 255, 255), batch = star ))
        



@ventana.event
def on_draw():
    ventana.clear()
    star.draw()

pyglet.clock.schedule_interval(update, 1/60.0)

run()