# This software here will maintain the main settings as well as the main starting point of the game.
import sys
import pygame
from settings import Settings as settings_alien


def main():
    # Root point for game to start
    pygame.init()
    # Initialize all imported pygame modules
    screen = pygame.display.set_mode((settings_alien().screen_height, settings_alien().screen_width))
    # Initialize output size monitor
    pygame.display.set_caption("==Alien==")
    # Output game's banner
    bg_color = settings_alien().bg_color

    # Start main loop for the game.
    while True:
        # Listen for mouse & keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Full display to screen
        screen.fill(bg_color)
        pygame.display.flip()


main()
