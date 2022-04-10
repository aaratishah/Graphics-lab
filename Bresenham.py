from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def BLA(x1, y1, x2, y2):

    #Calculate change in X and Y.
    dx = x2 - x1
    dy = y2 - y1

    x = x1
    y = y1

    #calculate slope
    m = dy / dx

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)


    if abs(m) < 1:
        #initial decision parameter
         

        for _ in range(abs(dx)):
            glVertex2f(round(x), round(y))
            if(p < 0):
                p += 2*dy
            else:
                p += (2*dy) - (2*dx)
                y += 1
            x += 1

    else:
        #initial decision parameter
        p = (2*abs(dx)) - abs(dy)

        for _ in range(abs(dy)):
            glVertex2f(round(x), round(y))
            if(p < 0):
                p += 2*abs(dx)
            else:
                if (dx < 0):
                    x -= 1
                else:
                    x += 1
                p += 2 * (abs(dx) - abs(dy))
            if(dy < 0):
                y -= 1
            else:
                y += 1

    glEnd()
    glFlush()


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("Processing....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Plot Line using Bresenham Algorithm")
    glutDisplayFunc(lambda: BLA(x1, y1, x2, y2))
    glutIdleFunc(lambda: BLA(x1, y1, x2, y2))
    init()
    glutMainLoop()

main()
