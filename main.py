import pygame
import time
from pygame.locals import*
import numpy as np

pygame.init()
window = pygame.display.set_mode((1000, 1000))

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill(0)

    point1Arr = [23,15]
    point2Arr = [390,424]
    controlPointArr = pygame.mouse.get_pos()
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
    for times in range(0, 1000):
        # t = time/100
        # B(t) = (1-t)[(1-t)p0+tp1]+t[(1-t)p1+tp2]
        t = times/1000
        B = (1-t)*((1-t)*point1+t*controlPoint)+t*((1-t)*controlPoint+t*point2)
        # window.set_at((round(B[0]), round(B[1])), 0xff0000)
        pygame.draw.line(window, 0xff0000, B, B_past)
        B_past = B
    pygame.draw.line(window, 0xff0000, B_past, point2)

        # time.sleep(0.0001)

    pygame.draw.circle(window, 0x00ff00, (point1[0], point1[1]), 5)
    pygame.draw.circle(window, 0x00ff00, (point2[0], point2[1]), 5)
    pygame.draw.circle(window, 0x00ffff, (controlPoint[0], controlPoint[1]), 5)

    pygame.display.flip()

pygame.quit()
exit()
