from lib2to3.pgen2 import driver
from turtle import up
from urllib import robotparser
import pygame
pygame.init()

screen = pygame.display.set_mode((1200,400))

path = pygame.image.load('way-1.png')

robo = pygame.image.load('robo-removebg-preview.png')

# Adjust the size of robot
robo = pygame.transform.scale(robo,(30,55))

# change the direction
robo_x = 150
robo_y = 300

focal_distance = 25

cam_x_change = 0
cam_y_change = 0

direction = 'up'

# Create  clock to control the speed

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(55)
    #Create a camera
    cam_x = robo_x + cam_x_change + 16
    cam_y = robo_y + cam_y_change + 22
    #Directions
    up_path = screen.get_at((cam_x,cam_y-focal_distance))[0]
    down_path = screen.get_at((cam_x,cam_y+focal_distance))[0]
    right_path = screen.get_at((cam_x+focal_distance,cam_y))[0]
    print(up_path,right_path,down_path)

    # Take turn

    if direction == 'up' and up_path !=255 and right_path == 255:
        direction = 'right'
        cam_x_change = 15
        cam_y_change = -6

        # Rotating the robo
        robo = pygame.transform.rotate(robo, -90)


    elif direction == 'right' and right_path != 255 and down_path == 255:
        direction = 'down'
        robo_x = robo_x + 22
        cam_x_change = -2
        cam_y_change = 10
        robo = pygame.transform.rotate(robo,-90)


    elif direction == 'down' and down_path != 255 and right_path == 255:
        direction = 'right'
        robo_x = robo_x + 10
        robo_y = robo_y + 15
        cam_x_change = 15
        cam_y_change = 0
        robo = pygame.transform.rotate(robo, 90)


    elif direction == 'right' and right_path != 255 and up_path == 255:
        direction = 'up'
        robo_x = robo_x + 15
        cam_x_change = 0
        robo = pygame.transform.rotate(robo,90)

        
    elif direction == 'down' and down_path == 255:
        robo_y = robo_y + 2
    if direction == 'up' and up_path == 255:
        robo_y = robo_y - 2
    elif direction == 'right' and right_path == 255:
        robo_x = robo_x + 2
    screen.blit(path,(0,0))
    screen.blit(robo,(robo_x,robo_y))
    pygame.draw.circle(screen,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()