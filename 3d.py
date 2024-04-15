import pygame
from math import cos, sin, pi
import numpy as np
from numpy import matrix
from time import sleep
from random import randint

WHITE = (255, 255, 255)
WIDTH = 500
HEIGHT = 500

pygame.init()
display = pygame.display
surface = display.set_mode((WIDTH, HEIGHT))
display.set_caption("3D Bezeir Viewer")

base_font = pygame.font.Font(None, 32) 
user_text = 'Hex code here' 
  
input_rect = pygame.Rect(10, 10, 150, 30) 
color_active = pygame.Color('0xffffff') 
color_passive = pygame.Color('0x555555') 
color = color_passive 

points = [ ]

lines = [ ]

def quadraticCurve():

    resolution = 100

    point1Arr = [-100, -100, 0]
    point2Arr = [100, 100, 0]
    # controlPointArr = pygame.mouse.get_pos()
    controlPointArr = [0, 0, 100]
    point1 = np.array(point1Arr)
    point2 = np.array(point2Arr)
    controlPoint = np.array(controlPointArr)

    # Δ = change

    # slope = Δy/Δdsurface.set_at((x, y), color)

    # slope of point 1 and control point
    # slope1 = (point1[1] - controlPoint[1])/(point1[0] - controlPoint[0])
    # slope of point 2 and control point
    # slope2 = (point2[1] - controlPoint[1])/(point2[0] - controlPoint[0])
    B_past = point1Arr
    for times in range(0, resolution):
        # t = time/100
        # B(t) = (1-t)[(1-t)p0+tp1]+t[(1-t)p1+tp2]
        t = times/resolution
        B = (1-t)*((1-t)*point1+t*controlPoint)+t*((1-t)*controlPoint+t*point2)

        points.append(B)
        if times != 0:
            lines.append((times, times-1, 0xff0000))
        B_past = B

quadraticCurve()

print(points)
print(lines)

done = False

rotation = [0, 0, 0]


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

active = False

while not done:

    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    pygame.draw.rect(surface, color, input_rect) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break


        if event.type == pygame.MOUSEBUTTONDOWN: 
            # print("mouse down")
            if input_rect.collidepoint(event.pos): 
                active = True
                # print("clicked textbox")
            else: 
                active = False
  
        if event.type == pygame.KEYDOWN: 
  
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode

    if active: 
        color = color_active 
    else: 
        color = color_passive 

    text_surface = base_font.render(user_text, True, (0, 0, 0)) 
      
    # render at position stated in arguments 
    surface.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(150, text_surface.get_width()+10) 

    #render 3d stuff

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

    for i in lines:
        try:
            pygame.draw.line(surface, user_text, render_points[i[0]], render_points[i[1]])
        except:
            pygame.draw.line(surface, i[2], render_points[i[0]], render_points[i[1]])


    # pygame.draw.line(surface, WHITE, render_points[0], render_points[2])

    rotation[0] += pi / randint(100, 200)
    rotation[1] += pi / randint(100, 200)

    display.flip()
    sleep(1/45)
