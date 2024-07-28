import pygame

pygame.init()

#create game windsow
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Action Game")

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for loading bg
def load_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#game window loop
run = True

while run:
    #load bg
    load_bg()
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
    
#exit pygame
pygame.QUIT()