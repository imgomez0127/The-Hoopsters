import pygame
import os 
from helga import Helga
from naomi import Naomi
class main:
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("The Hoopsters")
        background_image = pygame.image.load("assets/background.png")
        enemey = Helga()
        naomi = Naomi()

    def check_if_game_should_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def run_game(self):
        game_is_running = True
        while game_is_running:
            game_is_running = self.check_if_game_should_exit()
            naomi.react_to_keypress()
            helga.move()
            win.blit(background_image,(0,0)) 
            naomi.render()
            helga.render()
    
    
if __name__ == "__main__":
    main()
