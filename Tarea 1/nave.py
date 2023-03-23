from pyglet.window import Window, key, mouse
from pyglet.shapes import Circle, Star, Polygon , Triangle
from pyglet.app import run
from pyglet.graphics import Batch
import pyglet
import random
import numpy as np
WIDTH = 500
HEIGHT = 500
WINDOW_TITLE = 'Tarea 1'
FULL_SCREEN = False

ventana = Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable=True)

nave = Batch()




triangle = Triangle(100, 100 ,200 ,300 ,600 , 700 , (255, 200, 131) , batch=nave )
        




@ventana.event
def on_draw():
    ventana.clear()
    nave.draw()



run()


