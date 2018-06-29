# Here will be set all elements regarding the spaceship
import pygame


class Spaceship:
    """Here is the Spaceship class where all elements related to it wil be stored"""

    def __init__(self, screen):
        """Defining ship outlook and position on screen"""
        self.screen = screen

        # Load the ship image and get it's rect (rectangular zone).
        self.image = pygame.image.load('images/spaceship_blue.png')
        self.image_size = pygame.Surface.get_size(5, 5)
        self.scale = pygame.transform.scale(Spaceship.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Load starting position for the ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)
