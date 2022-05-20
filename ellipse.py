from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def midpoint(xc, yc, rx, ry):
    x = 0
    y = ry

    # Initial Decision parameter for region 1

    pa = ry**2 + (rx **2 / 4) - (rx**2 * ry)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)

    symmetricPoints(x, y, xc, yc)
    while(dx < dy):
        if pa < 0:
            x += 1
            dx = dx + (2 * ry * ry)
            pa = pa + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            pa = pa + dx - dy + (ry * ry)
            
        symmetricPoints(x, y, xc, yc)


    # Initial Decision parameter for region 2

    pb = (ry ** 2 * (x + 0.5) ** 2) + (rx ** 2 * (y - 1) ** 2) - (rx ** 2 * ry ** 2)

    while(y  >= 0):
        if pb > 0:
            y -= 1
            dy = dy - (2 * rx * rx)
            pb = pb + (rx * rx) - dy
        else:
            y -= 1;
            x += 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            pb = pb + dx - dy + (rx * rx);
        # x += 1
        symmetricPoints(x, y, xc, yc)

    glEnd()
    glFlush()

def symmetricPoints(x, y, xc, yc):
    four_symmetry_points = [[x + xc, y + yc], [-x + xc,y+yc], [x+xc,-y+yc], [-x+xc,-y+yc]]
    for point in four_symmetry_points:
        glVertex(point[0], point[1])


def main():
    print("Enter the center of ellipse")
    cx = int(input("Enter x-coordinate: "))
    cy = int(input("Enter y-coordinate: "))
    print("Enter the radius along x-axis")
    rx = int(input("x-radius: "))
    print("Enter the radius along y-axis")
    ry = int(input("y-radius: "))
    print("Processing....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Plot Ellipse using Midpoint Algorithm")
    glutDisplayFunc(lambda: midpoint(cx, cy, rx, ry))
    glutIdleFunc(lambda: midpoint(cx, cy, rx, ry))
    init()
    glutMainLoop()

main()
