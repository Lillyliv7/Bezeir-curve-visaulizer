#
# Calculates and displays a Bézeir surface with pygame
# by Lilly
#

import pygame
from math import cos, sin, pi
import numpy as np
from numpy import matrix
from time import sleep
from random import randint

WIDTH = 500
HEIGHT = 500

pygame.init()
display = pygame.display
surface = display.set_mode((WIDTH, HEIGHT))
display.set_caption("3D Bezeir Viewer")

points = [ # points in 3d space (x, y, z)
    # (50,50,50),(-50,-50,-50)
]
lines = [ # lines between point indexes (p1, p2, color)
    # (0,1,"0xff0000")
]



# triangle points
point_a3 = (np.array((-200,0,100)))
point_b3 = (np.array((0,200,50)))
point_y3 = (np.array((200,0,50)))
point_a2b = (np.array((180,50,0)))
point_ab2 = (np.array((50,150,0)))
point_b2 = (np.array((0,200,0)))
point_y = (np.array((200,0,0)))
point_by2 = (np.array((150,50,0)))
point_ay2 = (np.array((100,-25,0)))
point_a2y = (np.array((-25,50,0)))
point_aby = (np.array((25,100,0)))

def generate_bezier_triangle():
    print("generating")

    resolution = 100

    for s in range(1,resolution+1):
        s_norm = s/resolution
        for t in range(1,resolution+1):
            t_norm = t/resolution
            for u in range(1,resolution+1):
                u_norm = u/resolution
                if(s_norm+t_norm+u_norm == 1):
                    # print((s_norm,t_norm,u_norm))
                    # print(s_norm+t_norm+u_norm)

                    P = point_b3*pow(t_norm,3)+3*point_ab2*s_norm*pow(t_norm,2)+3*point_b2*point_y*pow(t_norm,2)*u_norm+3*point_a2b*pow(s_norm,2)*t_norm+6*point_aby*s_norm*t_norm*u_norm+3*point_by2*t_norm*pow(u_norm,2)+point_a3*pow(s_norm,3)+3*point_a2y*pow(s_norm,2)*u_norm*t_norm*3*point_a2y*pow(s_norm,2)*u_norm*t_norm*3*point_ay2*s_norm*pow(u_norm,2)+point_y3*pow(u_norm,3)
                    # print(P[2])
                    if(P[0] > 200 or P[0] < -200 or P[1] > 200 or P[1] < -200 or P[2] > 200 or P[2] < -200):
                        print(P)
                    points.append(P)
generate_bezier_triangle()
# print(points)
    # B_past = point1Arr
    # for times in range(0, 1000):
    #     # t = time/100
    #     # B(t) = (1-t)[(1-t)p0+tp1]+t[(1-t)p1+tp2]
    #     t = times/1000
    #     B = (1-t)*((1-t)*point1+t*controlPoint)+t*((1-t)*controlPoint+t*point2)
    #     # window.set_at((round(B[0]), round(B[1])), 0xff0000)
    #     pygame.draw.line(window, 0xff0000, B, B_past)
    #     B_past = B
    # pygame.draw.line(window, 0xff0000, B_past, point2)



def generate_x(theta):
    return matrix([
        [1, 0, 0],
        [0, cos(theta), -sin(theta)],
        [0, sin(theta), cos(theta)]
    ])

def generate_y(theta):
    return matrix([
        [cos(theta), 0, -sin(theta)],
        [0, 1, 0],
        [sin(theta), 0, cos(theta)]
    ])

def generate_z(theta):
    return matrix([
        [cos(theta), -sin(theta), 0],
        [sin(theta), cos(theta), 0],
        [0, 0, 1]
    ])

done = False

rotation = [0, 0, 0]

while not done:
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    
    render_points = []

    for p in points:

        m = matrix([
        [p[0]],
        [p[1]],
        [p[2]]
        ])

        for method, angle in zip((generate_x, generate_y, generate_z), rotation):
            m = method(angle) * m

        x, y, z = map(lambda x: int(WIDTH/2 - x), (m[0,0], m[1,0], m[2,0]))

        render_points.append((x, y))
    
    rotation[0] += pi / randint(100, 200)
    rotation[1] += pi / randint(100, 200)

    # for i in lines:
    #     pygame.draw.line(surface, i[2], render_points[i[0]], render_points[i[1]])
    for p in render_points:
        try:
            # pygame.draw.line(surface, 0xffffff, p[0], p[1])
            surface.set_at((p[0], p[1]), 0xff0000)
        except:
            print(p)
    # print(render_points)

    display.flip()
    # sleep(1/60)
