import pygame
import sys

pygame.init()

screen_width=200
screen_height=200

blue = (0,0,255)
brown = (150,75,0)
#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue background with Brown rectangle")
#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)
    #draw brown rect at bottom
    rectangle_height = 100
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height)) #sh-rh bc (0,0) is in top left corner of screen and pos x is down aka go down sh amt then back up rh amt to get starting position of brown
    #update the display
    pygame.display.flip()
#quit pygame
pygame.quit()
sys.exit()