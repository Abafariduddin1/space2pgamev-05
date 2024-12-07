import pygame
import sys

screen1=pygame.display.set_mode((900,500))
pygame.display.set_caption("New1")

bg = pygame.image.load("L.4/space.jpg")
backg = pygame.transform.scale(bg,(900,500))


rectonyship = pygame.Rect(50,250,60,60)
rectonrship = pygame.Rect(790,250,60,60)


yship = pygame.image.load("L.4/yelowship.jpg")
yeship = pygame.transform.scale(yship,(60,60))
yeeship = pygame.transform.rotate(yeship,90)

rship = pygame.image.load("L.4/redship.jpg")
reship = pygame.transform.scale(rship,(60,60))
reeship = pygame.transform.rotate(reship,270)

def bitl():
    screen1.blit(backg,(0,0))
    screen1.blit(reeship,(rectonrship.x,rectonrship.y))
    screen1.blit(yeeship,(rectonyship.x,rectonyship.y))
    ret = pygame.Rect(425,0,50,500)
    pygame.draw.rect(screen1,"black",ret)


def ymove():
    keyp = pygame.key.get_pressed()
    if keyp[pygame.K_w]:
        rectonyship.y=rectonyship.y-3
    if keyp[pygame.K_s]:
        rectonyship.y=rectonyship.y+3
    if keyp[pygame.K_a]:
        rectonyship.x=rectonyship.x-3
    if keyp[pygame.K_d]:
        rectonyship.x=rectonyship.x+3
    if rectonyship.y<0:
        rectonyship.y=500   
    if rectonyship.y>500:
        rectonyship.y=0
    if rectonyship.x<0:
        rectonyship.x=400
    if rectonyship.x>400:
        rectonyship.x=0 

    if keyp[pygame.K_UP]:
        rectonrship.y=rectonrship.y-3
    if keyp[pygame.K_DOWN]:
        rectonrship.y=rectonrship.y+3
    if keyp[pygame.K_LEFT]:
        rectonrship.x=rectonrship.x-3
    if keyp[pygame.K_RIGHT]:
        rectonrship.x=rectonrship.x+3
    if rectonrship.y<0:
        rectonrship.y=500   
    if rectonrship.y>500:
        rectonrship.y=0
    if rectonrship.x>900:
        rectonrship.x=450
    if rectonrship.x<450:
        rectonrship.x=900        

         





clock = pygame.time.Clock()
while True:
    clock.tick(60)
    ymove()
    bitl()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()