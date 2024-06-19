import pygame

class Bird:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect(center=(100, 300))
        self.velocity = 0
    
    def jump(self):
        self.velocity = -10

    def update(self, gravity):
        self.velocity += gravity
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
