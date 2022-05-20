import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0, 0, 0),
    (0, 5, 0),
    (1, 0, 0),
    (1, 5, 0),
    (1, 2, 0),
    (1, 3, 0),
    (2, 2.5, 0),
    (3, 0, 0),
    (3, 5, 0),
    (3, 1.4, 0),
    (3.7, 4.3, 0),
    (4.8, 3.2, 0),
    (5.5, 2.5, 0),
    (0, 0, 0.5),
    (0, 5, 0.5),
    (1, 0, 0.5),
    (1, 5, 0.5),
    (1, 2, 0.5),
    (1, 3, 0.5),
    (2, 2.5, 0.5),
    (3, 0, 0.5),
    (3, 5, 0.5),
    (3, 1.4, 0.5),
    (3.7, 4.3, 0.5),
    (4.8, 3.2, 0.5),
    (5.5, 2.5, 0.5),
    )

edges = (
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4,5),
    (5, 8),
    (8, 10),
    (10, 6),
    (6, 9),
    (9, 11),
    (11, 12),
    (12, 7),
    (7, 4),
    (0, 13),
    (1, 14),
    (2, 15),
    (3, 16),
    (4, 17),
    (5, 18),
    (6, 19),
    (7, 20),
    (8, 21),
    (9, 22),
    (10, 23),
    (11, 24),
    (12, 25),
    (13, 15),
    (13, 14),
    (15, 16),
    (14, 16),
    (17, 18),
    (21, 23),
    (24, 25),
    (18, 21),
    (19, 22),
    (19, 23),
    (22, 24),
    (20, 25),
    (17, 20)
    )

surfaces = (
    (13, 14, 16, 15),
    (18, 21, 23, 19,22, 24, 25, 20, 17),
    (19, 22, 20, 17),
    (18, 17, 19)
    )

def Logo():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3f(0, 0, 1)
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            # glColor3f(1, 0.482, 0)
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1000,700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(100, 1, 0, 50.0)

    glTranslatef(0.0,0.0, -12)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Logo()
        pygame.display.flip()
        pygame.time.wait(10)

main()