# Here will be set all elements regarding the spaceship
import pygame


class Spaceship:
    """Here is the Spaceship class where all elements related to it wil be stored"""

    def __init__(self, screen):
        """Defining ship outlook and position on screen"""
        self.screen = screen

        self.image = pygame.image.load('images/spaceship_black.png')
        self.rect = self.image.get_rect()
        