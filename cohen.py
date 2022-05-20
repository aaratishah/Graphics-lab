from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)

x_min = 50
y_min = 50
x_max =100
y_max =100

inside = 0
top = 1
bottom = 2
right = 4
left = 8

def computeCode(x, y):
   code = inside
   if x < x_min:      # left of rectangle
       code |= left
   elif x > x_max:    # right of rectangle
       code |= right
   if y < y_min:      # below
       code |= bottom
   elif y > y_max:    # above
       code |= top
   return code

def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
 
       if code1 == 0 and code2 == 0:
           accept = True
           break
        
       elif (code1 & code2) != 0:
           break
 
       else:
 
           x = 1.0
           y = 1.0
           if code1 != 0:
               code_out = code1
           else:
               code_out = code2
  
           if code_out & top:
 
               x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
               y = y_max
           elif code_out & bottom:
 
               x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
               y = y_min
           elif code_out & right:
                
       
               y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
               x = x_max
           elif code_out & left:
   
               y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
               x = x_min
 
           if code_out == code1:
               x1 = x
               y1 = y
               code1 = computeCode(x1, y1)
           else:
               x2 = x
               y2 = y
               code2 = computeCode(x2, y2)
    if accept:
        glColor3f(1.0, 0.0, 0.0);
        glBegin(GL_LINE_LOOP);
        glVertex2f(x_min+200, y_min+200)
        glVertex2f(x_max+200, y_min+200)
        glVertex2f(x_max+200, y_max+200)
        glVertex2f(x_min+200, y_max+200)
        glEnd()
        glColor3f(0.0,0.0,1.0); #draw blue colored clipped line
        glBegin(GL_LINES)
        glVertex2d (x1+200, y1+200)
        glVertex2d (x2+200, y2+200)

        glEnd()
  
    else:
       return None

def display(): 
    x1=120
    y1=10
    x2=40
    y2=130
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2d (x1, y1)
    glVertex2d (x2, y2)
    glVertex2d (10,70)
    glVertex2d (250,90)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)

    glVertex2d(x_min, y_min)
    glVertex2d(x_max, y_min)
    glVertex2d(x_max, y_max)
    glVertex2d(x_min, y_max)
    glEnd()
    cohenSutherlandClip(x1,y1,x2,y2)
    cohenSutherlandClip(10,70,250,90)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Cohen Sutherland Line Clipping Algorithm")
    glutDisplayFunc(lambda: display())
    glutIdleFunc(lambda: display())
    init()
    glutMainLoop()

main()


# def line_clip(lines,window_frame):
   
#     lines = [
#         [(100,0),(200,300)],
#         [(100,0),(50,130)],
#         [(0,0),(200,0)],
#     ]

#     for line in lines:
#         p1,p2 = line[0],line[1]
#         x1, y1 = p1
#         x2, y2 = p2
#         clipped_point = cohenSutherlandClip(x1, y1, x2, y2)
#         clipped_points.append(clipped_point)
    
#     return clipped_points

