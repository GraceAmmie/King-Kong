import pygame
from pygame.locals import *

pygame.init()
width, height = 520, 450

keys = [False, False, False, False]
playerpos  = [240, 300]

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('King Kong')

green = (0, 128, 0)
img1 = pygame.image.load("kingkong.png")

while 1 :
    window.fill(green)
    window.blit(img1, playerpos)
    pygame.display.flip()
    
#move the image using W-A-S-D in the keyboard
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                 keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
                
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5

        exit(0)
