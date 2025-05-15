import pygame
import sys

# Initialize Pygame / Pygame ehluuleh
pygame.init()

# Set up the dislay 
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# Define colors (R, G, B) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game loop 
clock = pygame.time.Clock()
running = True

while running:
    # Hardle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(WHITE)

    # Update the display
    pygame.draw.circle(screen, RED, (400, 300), 50)

    #update the display
    pygame.display.flip()
    clock.tick(60) # 60 FPS

# Quit
pygame.quit()
sys.exit()