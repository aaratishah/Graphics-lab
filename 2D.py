from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)

edges = [[100, 220], [180, 120], [210, 190]]

def drawPolygon():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)

    for edge in edges:
        glVertex2f(edge[0], edge[1])

    glEnd()
    # glFlush()

def translation():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    for edge in edges:
        glVertex2f(edge[0] + tx, edge[1] + ty)

    glEnd()
    # glFlush()

def scalling():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    for edge in range(edges):
        glVertex2f(edge[0] * sx, edge[1] * sy)

    glEnd()
    glFlush()

def reflection():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    if reflectionAxis == 'x' or reflectionAxis == 'X':
        for edge in range(edges):
            glVertex2f(edge[0], edge[1] * -1)
    elif reflectionAxis == 'y' or reflectionAxis == 'Y':
        for edge in range(edges):
            glVertex2f(edge[0] - 1, edge[1])

    glEnd()
    # glFlush()

def rotation():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    angleRad = angle * math.pi / 180

    for edge in range(edges):
        glVertex2f((edge[0] * math.cos(angleRad) - edge[1] * math.sin(angleRad)), (edge[0] * math.sin(angleRad) - edge[1] * math.cos(angleRad)))

    glEnd()
    # glFlush()

def shear():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)

    if shearAxis == 'x' or shearAxis == 'X':
        for edge in range(edges):
            glVertex2f(edge[0] + shx * edge[1], edge[1])
    elif shearAxis == 'y' or shearAxis == 'Y':
        for edge in range(edges):
            glVertex2f(edge[0], edge[1] + shy * edge[0])

    glEnd()
    # glFlush()

def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    if (choice == 1):
        drawPolygon()
        translation()
    
    elif (choice == 2):
        drawPolygon()
        scalling()
    
    elif (choice == 3):
        drawPolygon()
        rotation()
    
    elif (choice == 4):
        drawPolygon()
        reflection()
    
    elif (choice == 5):
        drawPolygon()
        shear()

    glFlush()

def main():

    global choice, tx, ty, sx, sy, angle, reflectionAxis, shearAxis, shx, shy

    print("Enter your choice:")
    choice = int(input("1. Translation \n2. Scaling \n3. Rotation \n4. Mirror Reflection \n5. Shearing \n6. Exit\n"))
    if (choice > 5 or choice < 1):
        return

    if choice == 1:
        tx = int(input("Enter X translation factor: "))
        ty = int(input("Enter Y translation factor: "))
    elif choice == 2:
        sx = input("Enter X scalling factor: ")
        sy = input("Enter Y scalling factor: ")
    elif choice == 3:
        angle = input("Enter the angle for rotation in degree: ")
    elif choice == 4:
        reflectionAxis = input("Enter reflection axis ( x or y ): ")
    elif choice == 5:
        shearAxis = input("Enter shearing axis ( x or y ): ")
        if(shearAxis == 'x' or shearAxis == 'X'):
            shx = input("Enter X shearing factor: ")
        elif(shearAxis == 'y' or shearAxis == 'Y'):
            shy = input("Enter Y shearing factor: ")

    print("Processing....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("2D tranformations")
    glutDisplayFunc(mydisplay)
    #glutIdleFunc(mydisplay)
    init()
    glutMainLoop()

main()
