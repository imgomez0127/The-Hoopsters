import pygame
from pygame.image import load
import os
class Naomi:

    def __init__(self,screen_width=1920):
        self.idle_image = load("assets/NAOMI.png")
        self.render_image = self.idle_image
        self.animations = {}
        self.health = 5
        self.height = 300
        self.width = 300
        self.horizontal_coordinate = 0
        self.ground = 600
        self.vertical_coordinate = 0
        self.min_width = 0
        self.max_width = screen_width-self.width
        self.speed = 25
        self.is_jumping = False
        self.action_frames = 0
        self.jump_counter = 5
        self.jumping_animation = self.idle_image
        self.previous_key = None
        self.populate_walking_animations_dictionary()
        self.is_idle = True
    
    def populate_walking_animations_dictionary(self):
        def image_path(file_name):
            return os.path.join("assets",file_name)
        def reverse_image(image):
            return pygame.transform.flip(image, True, False)

        self.animations[pygame.K_d] = [load(image_path("NAOMIWALK1.png")),load(image_path("NAOMIWALK2.png"))]
        self.animations[pygame.K_a] = [reverse_image(load(image_path("NAOMIWALK1.png"))),reverse_image(load(image_path("NAOMIWALK2.png")))]
        

    def react_to_keypress(self):
        keys = pygame.key.get_pressed()
        jumping = [pygame.K_SPACE,pygame.K_w]
        if keys[pygame.K_a]:
            if self.previous_key != pygame.K_a and self.previous_key not in jumping:
                self.previous_key = pygame.K_a
                self.action_frames = 0
            self.horizontal_coordinate = max(0,self.horizontal_coordinate-self.speed)
            self.render_image = self.animations[pygame.K_a][self.action_frames%2]
            self.action_frames += 1
        if keys[pygame.K_d]:
            if self.previous_key != pygame.K_d and self.previous_key not in jumping:
                self.previous_key = pygame.K_d
                self.action_frames = 0
            self.horizontal_coordinate= min(self.max_width,self.horizontal_coordinate+self.speed)
            self.render_image = self.animations[pygame.K_d][self.action_frames%2]
            self.action_frames += 1
        if self.is_jumping == False:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                self.is_jumping = True
            if keys[pygame.K_s]:
                self.vertical_coordinate -= self.height/2
            else:
                self.vertical_coordinate = 0
        else:
            self.vertical_coordinate += 7 * ((self.jump_counter ** 2) * (1 - 2 * (self.jump_counter > 0)))
            self.jump_counter -= 1 
            if self.jump_counter == -6:
                self.jump_counter = 5
                self.is_jumping = False
                self.previous_key = None
                self.action_frames = 0
        self.is_idle = True
        for key in keys:
            self.is_idle &= key
    def render(self):
        render_vector = (self.horizontal_coordinate,(self.vertical_coordinate+self.ground),self.height,self.width)
        if self.is_jumping:
            pygame.display.get_surface().blit(
                self.jumping_animation,
                render_vector
            )
        elif self.is_idle:
            pygame.display.get_surface().blit(
                self.idle_image,
                render_vector
            )
        else:
            pygame.display.get_surface().blit(
                self.render_image,
                render_vector
            )
