from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

width = 800
height = 500

STOP_X = 420            
SPEED = 2               
CAR_W = 80            
GREEN_TIME = 300       
YELLOW_TIME = 100
RED_TIME = 300

light = 0               
lightTimer = 0
spawnTimer = 0
cars = []               
carColors = [(0.85, 0.1, 0.1), (0.1, 0.3, 0.85), (0.95, 0.65, 0.1), (0.55, 0.2, 0.7)]


def drawRectangle(w, h):
    glBegin(GL_QUADS)
    glVertex2f(-w / 2, -h / 2)
    glVertex2f(w / 2, -h / 2)
    glVertex2f(w / 2, h / 2)
    glVertex2f(-w / 2, h / 2)
    glEnd()


def drawTriangle(b, h):
    glBegin(GL_TRIANGLES)
    glVertex2f(-b / 2, -h / 2)
    glVertex2f(b / 2, -h / 2)
    glVertex2f(0, h / 2)
    glEnd()


def drawCircle(r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for angle in range(361):
        theta = math.radians(angle)
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()


def drawCar(color):
    # body
    glPushMatrix()
    glColor3f(color[0], color[1], color[2])
    drawRectangle(CAR_W, 25)
    glPopMatrix()
    # cabin
    glPushMatrix()
    glTranslatef(0, 20, 0)
    glColor3f(color[0] * 0.8, color[1] * 0.8, color[2] * 0.8)
    drawRectangle(44, 18)
    glPopMatrix()
    # window
    glPushMatrix()
    glTranslatef(0, 20, 0)
    glColor3f(0.7, 0.9, 1.0)
    drawRectangle(34, 11)
    glPopMatrix()
    # wheels
    for wx in (-22, 22):
        glPushMatrix()
        glTranslatef(wx, -13, 0)
        glColor3f(0.1, 0.1, 0.1)
        drawCircle(9)
        glPopMatrix()


def drawSignal():
    # pole
    glPushMatrix()
    glTranslatef(STOP_X + 30, 235, 0)
    glColor3f(0.2, 0.2, 0.2)
    drawRectangle(8, 170)
    glPopMatrix()
    # signal box
    glPushMatrix()
    glTranslatef(STOP_X + 30, 330, 0)
    glColor3f(0.1, 0.1, 0.1)
    drawRectangle(44, 120)
    glPopMatrix()
    # three lamps
    lampY = [365, 330, 295]
    onColor = [(1.0, 0.0, 0.0), (1.0, 0.9, 0.0), (0.0, 0.9, 0.0)]
    offColor = (0.25, 0.25, 0.25)
    lampIndex = [2, 1, 0]   
    for i in range(3):
        glPushMatrix()
        glTranslatef(STOP_X + 30, lampY[i], 0)
        if light == lampIndex[i]:
            glColor3f(onColor[i][0], onColor[i][1], onColor[i][2])
        else:
            glColor3f(offColor[0], offColor[1], offColor[2])
        drawCircle(14)
        glPopMatrix()


def drawTree(x, y):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor3f(0.55, 0.27, 0.07)
    drawRectangle(20, 80)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(x, y + 80, 0)
    glColor3f(0.0, 0.6, 0.0)
    drawTriangle(90, 90)
    glPopMatrix()


def drawHouse(x, y):
    # body
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor3f(0.9, 0.65, 0.4)
    drawRectangle(140, 100)
    glPopMatrix()
    # roof
    glPushMatrix()
    glTranslatef(x, y + 85, 0)
    glColor3f(0.75, 0.1, 0.1)
    drawTriangle(180, 70)
    glPopMatrix()
    # door
    glPushMatrix()
    glTranslatef(x, y - 25, 0)
    glColor3f(0.35, 0.2, 0.1)
    drawRectangle(30, 50)
    glPopMatrix()


def drawScene():
    # grass
    glPushMatrix()
    glTranslatef(400, 100, 0)
    glColor3f(0.35, 0.75, 0.3)
    drawRectangle(800, 200)
    glPopMatrix()
    # street
    glPushMatrix()
    glTranslatef(400, 100, 0)
    glColor3f(0.3, 0.3, 0.3)
    drawRectangle(800, 100)
    glPopMatrix()
    # dashed middle line
    for x in range(20, 800, 60):
        glPushMatrix()
        glTranslatef(x, 100, 0)
        glColor3f(1, 1, 1)
        drawRectangle(30, 4)
        glPopMatrix()
    # stop line
    glPushMatrix()
    glTranslatef(STOP_X, 75, 0)
    glColor3f(1, 1, 1)
    drawRectangle(6, 50)
    glPopMatrix()
    # sun
    glPushMatrix()
    glTranslatef(100, 430, 0)
    glColor3f(1.0, 0.85, 0.0)
    drawCircle(40)
    glPopMatrix()

    drawTree(170, 240)
    drawHouse(680, 250)
    drawSignal()

    # all cars
    for car in cars:
        glPushMatrix()
        glTranslatef(car[0], 80, 0)
        drawCar(car[1])
        glPopMatrix()


def update(value):
    global light, lightTimer, spawnTimer

    # 1) change the signal
    lightTimer += 1
    if light == 0 and lightTimer >= GREEN_TIME:
        light = 1
        lightTimer = 0
    elif light == 1 and lightTimer >= YELLOW_TIME:
        light = 2
        lightTimer = 0
    elif light == 2 and lightTimer >= RED_TIME:
        light = 0
        lightTimer = 0

    # 2) create a new car
    spawnTimer += 1
    if spawnTimer >= 120:
        if len(cars) == 0 or min(c[0] for c in cars) > 30:
            cars.append([-60, random.choice(carColors)])
            spawnTimer = 0

    # 3) move the cars 
    cars.sort(key=lambda c: -c[0])
    for i in range(len(cars)):
        nextX = cars[i][0] + SPEED
        front = cars[i][0] + CAR_W / 2
        blocked = False

        # stop before the line when the light is yellow or red
        if light != 0 and front <= STOP_X and front + SPEED > STOP_X:
            blocked = True
        # keep a safe gap from the car 
        if i > 0 and cars[i - 1][0] - nextX < CAR_W + 10:
            blocked = True

        if not blocked:
            cars[i][0] = nextX

    # 4) remove cars that left the screen
    cars[:] = [c for c in cars if c[0] < width + 60]

    glutPostRedisplay()
    glutTimerFunc(15, update, 0)


def showScreen():
    glClearColor(0.53, 0.81, 0.92, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    drawScene()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Traffic Signal Simulation")
glutDisplayFunc(showScreen)
glutTimerFunc(0, update, 0)
glutMainLoop()