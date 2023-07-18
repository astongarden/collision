import sys
import pygame
from pygame.locals import *
import gjk
import math
import numpy as np

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

robot_link1 = 200
robot_link2 = 200
robot_thickness = 20

q1 = 0
q2 = 0


def run():


    link_1 = (
    (robot_thickness*math.sin(q1),-robot_thickness*math.cos(q1)),
    (-robot_thickness*math.sin(q1),robot_thickness*math.cos(q1)),
    (-robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),robot_thickness*math.cos(q1)+robot_link1*math.sin(q1)),
    (robot_thickness*math.sin(q1)+robot_link1*math.cos(q1),-robot_thickness*math.cos(q1)+robot_link1*math.sin(q1))
    )

    link_2 = (
    (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)),
    (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)),
    (robot_link1*math.cos(q1)-robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)+robot_thickness*math.cos(q2)+robot_link2*math.sin(q2)),
    (robot_link1*math.cos(q1)+robot_thickness*math.sin(q2)+robot_link2*math.cos(q2),robot_link1*math.sin(q1)-robot_thickness*math.cos(q2)+robot_link2*math.sin(q2))
    )

    circle1 = ((100, 100), 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass



        SCREEN.fill(WHITE)

        collide_1 = gjk.collidePolyCircle(link_1, circle1)
        polygon(link_1)
        circle(circle1)
        collide_2 = gjk.collidePolyCircle(link_2, circle1)
        polygon(link_2)
        circle(circle1)

        print('True' if (collide_1 or collide_2) else 'fail')

        pygame.display.flip()

        CLOCK.tick(1)


def pairs(points):
    for i, j in enumerate(range(-1, len(points) - 1)):
        yield (points[i], points[j])

def circles(cs, color=BLACK, camera=(0, 0)):
    for c in cs:
        circle(c, color, camera)

def circle(c, color=BLACK, camera=(0, 0)):
    pygame.draw.circle(SCREEN, color, add(c[0], camera), c[1])

def polygon(points, color=BLACK, camera=(0, 0)):
    for a, b in pairs(points):
        line(a, b, color, camera)

def line(start, end, color=BLACK, camera=(0, 0)):
    pygame.draw.line(SCREEN, color, add(start, camera), add(end, camera))

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

if __name__ == '__main__':
    run()



