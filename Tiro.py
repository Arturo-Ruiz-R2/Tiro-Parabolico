"""Cannon, hitting targets with projectiles.


Exercises
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""
#Codigo modificado por:
#Autor: Arturo Cuauhtemoc Ruiz Leyva
#Autor: Andrea Vianey Diaz Alvarez

"""Se importan las librerias que se usan en el codigo"""
from random import randrange
from turtle import *
from freegames import vector


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """
    Respond to screen tap.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """
    Return True if xy within screen.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """
    Draw ball and targets.
    """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """
    Move ball and targets.
    """
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    #condicion para que las pelotas vuelvan a aparecer desde el principio (si no les diste)
    for target in targets:
        if not inside(target):
            target.x=-target.x
            goto(target.x,target.y)
            
    ontimer(move, 10)   #Velocidad del juego

setup(420, 420, 370, 100) #Posicion donde aparece la ventana y de que tamaño
hideturtle() #Esconde el cursor
up() #No dibuja durante el juego
tracer(False) #Que el cursor no sea una tortuga
onscreenclick(tap) #Hace que funcione el juego cuando le des  un click
move() #Hace que empiece el juego
done() #Termina el programa
