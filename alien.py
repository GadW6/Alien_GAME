# This software here will maintain the main settings as well as the main starting point of the game.
import sys
import pygame


def main():
    # Root point for game to start
    pygame.init()
    # Initialize all imported pygame modules
    screen = pygame.display.set_mode((1200, 800))
    # Initialize output size monitor
    pygame.display.set_caption("==Alien==")

    # Start main loop for the game.
    while True:
        # Listen for mouse & keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Full display to screen
        pygame.display.flip()


main()
