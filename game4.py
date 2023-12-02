import pygame
import sys
import random
from fish import Fish, FishOpposite, fishes


# Initialize Pygame
pygame.init()

# Screen dimensions
tile_size = 64
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

clock = pygame.time.Clock()

# load game font
custom_font = pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 72)

#create text object with the message "chomp" to display, and tuple (253, 69, 0) as font color
text = custom_font.render("Chomp", True, (253, 69, 0))

def draw_background(screen):
    # Load tiles from the assets folder into surfaces
    water = pygame.image.load("../chomp/assets/sprites/water.png").convert()
    sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()
    # use the png transparency
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))
    # fill the screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))
    # draw the sand top along the bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height-tile_size))
    # distribute seagrass randomly across the sand, and not too close to the top
    for _ in range(5):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height-tile_size*2+20))



# Main loop
running = True
background = screen.copy()
draw_background(background)

#place fish off right side of screen in random positions
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height-tile_size)))
    fishes.add(FishOpposite(random.randint(0, screen_width*2), random.randint(tile_size, screen_height-tile_size)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    screen.blit(background, (0, 0))
    # draw text at center of display
    screen.blit(text, (screen_width/2-text.get_width()/2, 16))

    #update game objects
    fishes.update()

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height-tile_size)))



    fishes.draw(screen)


    # Update the display
    pygame.display.flip()

    #limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()



# import pygame
# import sys
# import  random
# #from random import randrange
#
# pygame.init()
#
# #screen dimensions
# screen_width=800
# screen_height=600
# tile_size = 64
#
# #create screen
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("using tiles and blit to draw on surface")
#
# #load game font
# custom_font=pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 64)
# #create message
# text= custom_font.render("Chomp", True, (225, 69, 0))
#
# def draw_background(screen):
#     #load tile
#     water = pygame.image.load("../chomp/assets/sprites/water.png").convert()  #("../assets/sprites/water.png")
#     sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()  #("..C:/Users/m262004/Programming/github/chomp/assets/sprites/sand.png")
#     seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()  #("../assets/sprites/seagrass.png")
#
#     #use png transparency
#     water.set_colorkey((0,0,0))
#     sand.set_colorkey((0,0,0))
#     seagrass.set_colorkey((0,0,0))
#
#     #fill screen with water
#     for x in range(0, screen_width, tile_size):
#         for y in range(0, screen_height, tile_size): #tile is a square
#             screen.blit(water,(x,y))
#     #sand
#     for x in range(0, screen_width, tile_size):
#         for y in range(screen_height-tile_size, screen_height, tile_size): #tile is a square
#             screen.blit(sand,(x,y))
#     #seagrass
#     for _ in range(5):
#         x = random.randint(0, screen_width)
#         #for y in range(screen_height-tile_size, screen_height, tile_size): #tile is a square
#         screen.blit(seagrass, (x, screen_height - tile_size * 2 + 20))
#
#     screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))
# background = screen.copy()
# draw_background(background)
#
# #main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     #draw background
#     screen.blit(background, (0,0))
#
#     #draw text at center of display
#     screen.blit(text, (screen_width/2-text.get_width()/2, 16))
#
#     #update the display
#     pygame.display.flip()
# #quit pygame
# pygame.quit()
# sys.exit()