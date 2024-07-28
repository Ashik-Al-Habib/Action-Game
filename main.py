import pygame
from fighter import Fighter

pygame.init()

#create game windsow
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Action Game")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for loading bg
def load_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    
#create two fighters
figther_1 = Fighter(200, 310)
figther_2 = Fighter(700, 310)

#game window loop
run = True

while run:
    
    clock.tick(FPS)
    
    #load bg
    load_bg()
    
    #move fighters
    figther_1.move(SCREEN_WIDTH)
    # figther_2.move()
    
    #draw fighters
    figther_1.draw(screen)
    figther_2.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
    
#exit pygame
pygame.QUIT()