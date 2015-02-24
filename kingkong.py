import pygame
import math, random
from pygame.locals import *

pygame.init()
width, height = 650, 475
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('King Kong')

acc = [0,0]
bombs=[]

badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

keys = [False, False, False, False]
playerpos  = [160, 300]
green = (0, 128, 0)

#load images
img1 = pygame.image.load("kingkong1.png")
img2 = pygame.image.load ("bananas.png")
img3 = pygame.image.load ("bomb.jpg")
img4 = pygame.image.load("rival.jpg")
rival = img4
#img5 = pygame.image.load ("download.jpg")
#img6 = pygame.image.load ("button.png")
img7 = pygame.image.load ("overs.jpg")
img8 = pygame.image.load ("win.png")

#display images on the screen
running = 1
exitcode = 0
while running :
    badtimer-=1
    window.fill(green)
    window.blit(img2, (0,0))
    window.blit(img2, (0,100))
    window.blit(img2, (0,200))
    window.blit(img2, (0,300))
    window.blit(img2, (0,400))

#move the image
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(img1, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    window.blit(playerrot, playerpos1)

#draw the bombs on the screen
    for bullet in bombs:
        index=0
        velx=math.cos(bullet[0])*8
        vely=math.sin(bullet[0])*8
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            bombs.pop(index)
        index+=1
        for projectile in bombs:
            bomb1 = pygame.transform.rotate(img3, 360-projectile[0]*57.29)
            window.blit(bomb1, (projectile[1], projectile[2]))

#decrement the value of badtimer for each frame         
    badtimer-=1
#draw rivals
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7

#attack bananas
        badrect=pygame.Rect(img4.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
           healthvalue -= random.randint(5,20)
           badguys.pop(index)        
        index+=1

#check for collisions(6.3.1)
        index1=0
        for bullet in bombs:
            bullrect=pygame.Rect(img3.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index1)
                bombs.pop(index1)
            index1+=1
            
    for badguy in badguys:
        window.blit(rival, badguy)

        
        #window.blit(img5, (5,5))
        #for health1 in range(healthvalue):
          #window.blit(img6, (health1+8,8))

#clock           
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    window.blit(survivedtext, textRect)
        
    pygame.display.flip()

#move the image using the arrow keys
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == KEYDOWN:
            if (event.key == K_UP):
                keys[0]=True
            elif (event.key == K_LEFT):
                keys[1]=True
            elif (event.key == K_DOWN):
                keys[2]=True
            elif (event.key == K_RIGHT):
                keys[3]=True
        if event.type == KEYUP:
            if (event.key == K_UP):
                keys[0]=False
            elif (event.key == K_LEFT):
                keys[1]=False
            elif (event.key == K_DOWN):
                keys[2]=False
            elif (event.key == K_RIGHT):
                keys[3]=False

#fire bombs if mouse is clicked
                if event.type==pygame.MOUSEBUTTONDOWN:
                    position=pygame.mouse.get_pos()
                    acc[1]+=1
                bombs.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
                      
    if keys[0]:
        playerpos[1]-=5
    if keys[1]:
         playerpos[0]-=5
    elif keys[2]:
        playerpos[1]+=5
    elif keys[3]:
        playerpos[0]+=5

#win/lose check
        if pygame.time.get_ticks()>=90000:
            running=0
            exitcode=1
        if healthvalue<=0:
            running=0
            exitcode=0
        if acc[1]!=0:
            accuracy=acc[0]*1.0/acc[1]*100
        else:
            accuracy=0
            
#display win or lose images
    if exitcode==0:
        window.blit(img7, (0,0))
    else:
        window.blit(img8, (0,0))

        

        
     
