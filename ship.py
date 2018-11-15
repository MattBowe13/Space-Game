import pygame
from PIL import Image

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize ship and set starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Start each new ship at the bottom center of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value at the bottom center of screen.
        self.center = float(self.rect.centerx)
        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ships center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship and its current location."""
        self.screen.blit(self.image, self.rect)
