from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def midpoint(cx, cy, r):
    x = 0
    y = r

    p = 1 - r

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)

    symmetricPoints(x, y, cx, cy)
    while(x < y):
        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * (x - y) + 1
            y -= 1
        x += 1
        symmetricPoints(x, y, cx, cy)

    glEnd()
    glFlush()

def symmetricPoints(x, y, cx, cy):
    eight_symmetry_points = [[x,y], [-x,y], [x,-y], [-x,-y], [y,x], [y,-x], [-y,x], [-y,-x]]
    for point in eight_symmetry_points:
        glVertex(point[0]+cx, point[1]+cy)


def main():
    print("Enter the center of circle")
    cx = int(input("Enter x-coordinate: "))
    cy = int(input("Enter y-coordinate: "))
    print("Enter the radius of circle")
    r = int(input("radius: "))
    print("Processing....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Plot Circle using Midpoint Algorithm")
    glutDisplayFunc(lambda: midpoint(cx,cy,r))
    glutIdleFunc(lambda: midpoint(cx,cy,r))
    init()
    glutMainLoop()

main()
