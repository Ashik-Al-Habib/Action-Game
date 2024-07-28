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

#define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for loading bg
def load_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#function for showing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    
#create two fighters
figther_1 = Fighter(200, 310)
figther_2 = Fighter(700, 310)

#game window loop
run = True

while run:
    
    clock.tick(FPS)
    
    #load bg
    load_bg()
    
    #show player health
    draw_health_bar(figther_1.health, 20, 20)
    draw_health_bar(figther_2.health, 580, 20)
    
    #move fighters
    figther_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, figther_2)
    # figther_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    
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