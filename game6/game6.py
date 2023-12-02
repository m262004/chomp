import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish
# Initialize Pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")
# Load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
clock = pygame.time.Clock()

# Main loop
running = True
background = screen.copy()
draw_background(background)
# place fish off the right side of the screen in random positions
add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
# initialize score and a custom font to display it
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
    # draw the background
    screen.blit(background, (0, 0))
    # update game objects
    fishes.update()
    player.update()

    # check for collisions between player and fish
    # update score and remove fish if there is a collision
    # use group collision detection
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        # add new fish
        add_fish(len(result))

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE*2, random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
    # draw game objects
    fishes.draw(screen)
    player.draw(screen)

    # draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    # Update the display
    pygame.display.flip()
    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
