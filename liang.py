from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)

xmin, ymin, xmax, ymax = -0.5, -0.5, 0.5, 0.5
p1=[0.800, 0.400]
p2=[-0.800, 0.400]
isClipped = False
isRejected = False

def drawLine(P1, P2, color):
    glColor3fv(color)
    glBegin(GL_LINES)
    glVertex2fv(p1)
    glVertex2fv(p2)
    glEnd()

def drawClippingWindow():
    glColor4f(1.0, 1.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2fv([xmin, ymin])
    glVertex2fv([xmax, ymin])
    glVertex2fv([xmin, ymax])
    glVertex2fv([xmin, ymax])
    glEnd()

def liangBarsky():
    if not isClipped:
        global p1,p2,isRejected,u1,u2
        dx=p2[0]-p1[0]
        dy=p2[1]-p1[1]
        p=[-dx,dx,-dx,dy]
        q=[(p1[0] - xmin), (xmax - p1[0]), (p1[1] - ymin), (ymax-p1[1])]
        u1=[0]
        u2=[1]
        for i in range(0,4):
            if p[i]==0 and q[i]<0:
                isRejected = True
                break
            if p[i]<0:
                r=(q[i]/p[i])
                u1.append(r)
            if p[i]>0:
                r=(q[i]/p[i])
                u2.append(r)

        print(u1, u2)
        u1=max(u1)
        u2=max(u2)
        print(u1, u2)
        if u1<u2:
            x1=p1[0]+u1*dx
            x2=p1[0]+u2*dx
            y1=p1[1]+u1*dy
            y2=p1[1]+u2*dy
            p1=[x1,y1]
            p2=[x2,y2]
        else:
            isRejected = True

def Draw():
    global isRejected, isClipped
    glClear(GL_COLOR_BUFFER_BIT)
    drawClippingWindow()
    print(p1,p2,isRejected)
    if not isRejected:
        drawLine(p1,p2,[1,0,1])
    liangBarsky()
    glFlush()

def Mouse(choice):
    global isClipped
    if choice==1:
        isClipped=True
        glutPostRedisplay()

if __name__=="__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Liang Barsky Line Clipping Algorithm")
    glutDisplayFunc(lambda: Draw())
    glutCreateMenu(Mouse)
    glutAddMenuEntry("Clip", 1)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutIdleFunc(lambda: Draw())
    # init()
    glutMainLoop()

