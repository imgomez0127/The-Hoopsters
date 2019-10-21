import pygame
from pygame.image import load
class Hoop(pygame.sprite.Sprite):
    
    def __init__(self,horizontal_coordinate=0,vertical_coordinate=0,direction=1):
        self.horizontal_coordinate = horizontal_coordinate
        self.vertical_coordinate = vertical_coordinate
        self.direction = direction
        self.image = load("assets/hoop.png")
        self.width = 100
        self.height = 100
        self.speed = 70
    
    def move(self):
        self.horizontal_coordinate = self.horizontal_coordinate + (self.direction * self.speed)
    
    def render(self):
        pygame.display.get_surface().blit(
                    self.image,
                    (
                        self.horizontal_coordinate,
                        self.vertical_coordinate,
                        self.width,
                        self.height
                    )
                )

