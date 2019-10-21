import pygame
from pygame.image import load
class Helga(pygame.sprite.Sprite):

    def __init__(self,screen_width=1920):
        super().__init__()
        self.__health = 10
        self.__height = 300
        self.__width = 200
        self.__horizontal_coordinate = 1600
        self.__vertical_coordinate = 400
        self.__direction = -1 #-1 is left 1 is right it will be a multiple to find the next screen pos
        self.__min_width = 0
        self.__max_width = screen_width-self.__width
        self.__speed = 25
        self.__animations = ["assets/helga/walk1.png","assets/helga/walk2.png","assets/helga/walk3.png","assets/helga/walk4.png"]
        self.__animation_to_load = 1
        self.death_animation = 0

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self,health):
        self.__health = health

    @property
    def horizontal_coordinate(self):
        return self.__horizontal_coordinate
    
    @horizontal_coordinate.setter
    def horizontal_coordinate(self, horizontal_coordinate):
        self.horizontal_coordinate = horizontal_coordinate

    @property 
    def vertical_coordinate(self):
        return self.__vertical_coordinate
    
    @vertical_coordinate.setter
    def vertical_coordinate(self,vertical_coordinate):
        self.vertical_coordinate = vertical_coordinate
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self,direction):
        self.__direction = direction

    def check_direction_for_next_move(self):
        if self.__horizontal_coordinate <= 0:
            self.__direction = 1
        if self.__horizontal_coordinate >= self.__max_width:
            self.__direction = -1

    def move(self):
        self.check_direction_for_next_move()
        if self.health > 0:
            self.__horizontal_coordinate = self.__horizontal_coordinate + (self.direction * self.__speed)

    def die(self):
        pygame.display.get_surface().blit(
            self.death_image[self.death_animation],
            (
                self.horizontal_coordinate,
                self.vertical_coordinate,
                self.width,
                self.height
                    )
        )
        self.death_animation = min(10,self.death_animation+1)

    def render(self):
        render_image = load(self.__animations[self.__animation_to_load]) if self.direction == 1 else pygame.transform.flip(load(self.__animations[self.__animation_to_load]), True, False)

        pygame.display.get_surface().blit(
            render_image,
            (
                self.horizontal_coordinate,
                self.vertical_coordinate,
                self.width,
                self.height
            )
        )
        self.__animation_to_load += 1
        self.__animation_to_load %= len(self.__animations)

    def got_hit(self,game_item):
        if game_item.horizontal_coordinate < self.horizontal_coordinate + self.width and game_item.horizontal_coordinate > self.horizontal_coordinate:
            self.health = self.health - 1 
            return True
        return False
    def collided(self,game_item):        
        if game_item.horizontal_coordinate < self.horizontal_coordinate + self.width and game_item.horizontal_coordinate > self.horizontal_coordinate:
            self.health = self.health -1 

