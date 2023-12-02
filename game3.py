import pygame
import sys
import  random
#from random import randrange


pygame.init()

#screen dimensions
screen_width=800
screen_height=600
tile_size = 64

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("using tiles and blit to draw on surface")

#load game font
custom_font=pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 128)
#create message
text= custom_font.render("Chomp", True, (225, 69, 0))

def draw_background(screen):
    #load tile
    water = pygame.image.load("../chomp/assets/sprites/water.png").convert()  #("../assets/sprites/water.png")
    sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()  #("..C:/Users/m262004/Programming/github/chomp/assets/sprites/sand.png")
    seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()  #("../assets/sprites/seagrass.png")

    #use png transparency
    water.set_colorkey((0,0,0))
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size): #tile is a square
            screen.blit(water,(x,y))
    #sand
    for x in range(0, screen_width, tile_size):
        for y in range(screen_height-tile_size, screen_height, tile_size): #tile is a square
            screen.blit(sand,(x,y))
    #seagrass
    for x in range(0, screen_width, tile_size):
        pos = random.randint(0, screen_width)
        #for y in range(screen_height-tile_size, screen_height, tile_size): #tile is a square
        screen.blit(seagrass,(pos,screen_height-1.75*tile_size)) #(random.randrange(0, screen_width, tile_size)

background = screen.copy()
draw_background(background)

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    #draw text at center of display
    screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()/2))

    #update the display
    pygame.display.flip()
#quit pygame
pygame.quit()
sys.exit()