import pygame
import random

class Pipe:
    def __init__(self, image, x, gap, screen_height):
        self.image = image
        self.screen_height = screen_height
        self.gap = gap
        self.top_rect = self.image.get_rect(midbottom=(x, random.randint(100, screen_height - gap - 100)))
        self.bottom_rect = self.image.get_rect(midtop=(x, self.top_rect.bottom + gap))
        self.passed = False
    
    def update(self, speed):
        self.top_rect.x -= speed
        self.bottom_rect.x -= speed
    
    def draw(self, screen):
        """screen.blit(self.image, self.top_rect)
        screen.blit(self.image, self.bottom_rect)"""
        flipped_top_image = pygame.transform.flip(self.image, False, True)
        screen.blit(flipped_top_image, self.top_rect)
        screen.blit(self.image, self.bottom_rect)
    
    def is_off_screen(self):
        return self.top_rect.right < 0
    
    def has_collided_with(self, bird):
        return bird.rect.colliderect(self.top_rect) or bird.rect.colliderect(self.bottom_rect)
