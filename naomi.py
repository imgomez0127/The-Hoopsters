import pygame
from pygame.image import load
import os
from bullet import Bullet 
def image_path(file_name):
    return os.path.join("assets",file_name)
def reverse_image(image):
            return pygame.transform.flip(image, True, False)

class Naomi(pygame.sprite.Sprite):

    def __init__(self,screen_width=1920):
        self.idle_image = load("assets/NAOMI.png")
        self.render_image = self.idle_image
        self.animations = {}
        self.health = 5
        self.height = 300
        self.width = 250
        self.horizontal_coordinate = 0
        self.ground = 600
        self.vertical_coordinate = 0
        self.min_width = 0
        self.max_width = screen_width-self.width
        self.speed = 30
        self.is_jumping = False
        self.action_frames = 0
        self.jump_counter = 5
        self.jumping_animation = self.idle_image
        self.previous_key = None
        self.populate_walking_animations_dictionary()
        self.create_jumping_animation()
        self.is_idle = True
        self.facing_right = True
        self.invul = 0
    
    def create_jumping_animation(self):
        self. jumping_animation = [load(os.path.join("assets/JUMPY",image)) for image in sorted(os.listdir("assets/JUMPY"))]

    def populate_walking_animations_dictionary(self):
        self.animations[pygame.K_d] = [load(image_path("NAOMIWALK1.png")),load(image_path("NAOMIWALK2.png"))]
        self.animations[pygame.K_a] = [load(image_path("NAOMIWALK1.png")),load(image_path("NAOMIWALK2.png"))]
        

    def react_to_keypress(self,bullets):
        keys = pygame.key.get_pressed()
        jumping = [pygame.K_SPACE,pygame.K_w]
        if keys[pygame.K_a]:
            if self.previous_key != pygame.K_a and self.previous_key not in jumping:
                self.previous_key = pygame.K_a
                self.action_frames = 0
            self.horizontal_coordinate = max(0,self.horizontal_coordinate-self.speed)
            self.render_image = self.animations[pygame.K_a][self.action_frames%2]
            self.action_frames += 1
            self.facing_right = False
        if keys[pygame.K_d]:
            if self.previous_key != pygame.K_d and self.previous_key not in jumping:
                self.previous_key = pygame.K_d
                self.action_frames = 0
            self.horizontal_coordinate= min(self.max_width,self.horizontal_coordinate+self.speed)
            self.render_image = self.animations[pygame.K_d][self.action_frames%2]
            self.action_frames += 1
            self.facing_right = True
        if keys[pygame.K_s]:
            bullets.append(
                Bullet(
                    horizontal_coordinate = self.horizontal_coordinate,
                    vertical_coordinate = self.vertical_coordinate+self.ground+130,
                    direction = 1 if self.facing_right else -1 
                )
            )
        if self.is_jumping == False:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                self.is_jumping = True
            else:
                self.vertical_coordinate = 0
        else:
            self.vertical_coordinate += 10 * ((self.jump_counter ** 2) * (1 - 2 * (self.jump_counter > 0)))
            self.jump_counter -= 1 
            if self.jump_counter == -6:
                self.jump_counter = 5
                self.is_jumping = False
                self.previous_key = None
                self.action_frames = 0
        self.is_idle = True
        for key in keys:
            self.is_idle &= not key

    def move(self):
        self.horizontal_coordinate = self.horizontal_coordinate + self.speed

    def got_hit(self,game_item):
        if game_item.horizontal_coordinate < self.horizontal_coordinate + self.width and game_item.horizontal_coordinate > self.horizontal_coordinate and not game_item.vertical_coordinate > self.vertical_coordinate + self.height+self.ground and not self.invul:
            self.invul = 5
            self.health = self.health - 1 

    def render(self,is_done):
        self.invul = max(0,self.invul-1)
        render_vector = (self.horizontal_coordinate,(self.vertical_coordinate+self.ground),self.height,self.width)
        if self.is_idle:
            self.render_image = self.idle_image
        self.render_image = self.render_image if self.facing_right else reverse_image(self.render_image)
        if self.is_jumping: 
            pygame.display.get_surface().blit(
                self.jumping_animation[(self.jump_counter-1)+5] if self.facing_right else reverse_image(self.jumping_animation[(self.jump_counter-1)+5]),
                render_vector
            )
        else:
            if is_done:
                self.render_image = self.idle_image
            pygame.display.get_surface().blit(
                self.render_image,
                render_vector
            )
