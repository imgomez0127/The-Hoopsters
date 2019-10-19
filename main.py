import pygame
import os 
from helga import Helga
from naomi import Naomi
class main:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("The Hoopsters")
        self.background_image = pygame.image.load("assets/background.png")
        self.helga = Helga()
        self.naomi = Naomi()

    def check_if_game_should_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def run_game(self):
        game_is_running = True
        while game_is_running:
            pygame.time.delay(50)
            game_is_running = not self.check_if_game_should_exit()
            self.game_is_running = self.check_if_game_should_exit()
            self.helga.move()
            self.naomi.react_to_keypress()
            self.win.blit(self.background_image,(0,0))
            self.helga.render()
            self.naomi.render()
            pygame.display.update()
    
if __name__ == "__main__":
    main().run_game()
