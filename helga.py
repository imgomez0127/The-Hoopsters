import pygame

class Helga(pygame.sprite.Sprite):

    def __init__(self,screen_width=1920):
        super().__init__()
        self.__image = pygame.image.load_image("assets/helga.png")
        self.__health = 5
        self.__height = 300
        self.__width = 300
        self.__horizontal_coordinate = 0
        self.__vertical_coordinate = 0
        self.__direction = -1 #-1 is left 1 is right it will be a multiple to find the next screen pos
        self.__min_width = 0
        self.__max_width = screen_width-width
        self.__speed = 25

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
        self.health = health

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

    def check_direction_for_next_move():
        if self.__horizontal_coordinate == 0:
            self.__direction = 1
        if self.__horizontal_coordinate == self.__max_width:
            self.__direction = -1

    def move(self):
        self.check_direction_for_next_move()
        self.__horizontal_coordinate = horizontal_coordinate + (self.direction * self.__speed)
    
    def render(self):
        pygame.display.get_surface.blit(
            self.__image,
            (
                self.horizontal_coordinate,
                self.vertical_coordinate,
                self.width,
                self.height
            )
        )
