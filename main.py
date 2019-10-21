import pygame
from pygame.image import load
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
        self.bullets = []
    def remove_bullets(self):
        for bullet in self.bullets:
            if bullet.horizontal_coordinate <= 0 or bullet.horizontal_coordinate >= 1920-bullet.width:
                self.bullets.remove(bullet)

    def render_bullets(self):
        for bullet in self.bullets:
            bullet.render()

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move()
    
    def check_if_helga_got_hit(self):
        for bullet in self.bullets:
            if self.helga.got_hit(bullet):
                self.bullets.remove(bullet)
            

    def check_if_game_should_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    def run_game(self):
        game_is_running = True
        while game_is_running:
            pygame.time.delay(30)
            game_is_running = not self.check_if_game_should_exit()
            self.game_is_running = self.check_if_game_should_exit()
            self.win.blit(self.background_image,(0,0))
            if self.helga.health > 0:
                self.helga.move()
                self.naomi.react_to_keypress(self.bullets)
                self.move_bullets()
                self.check_if_helga_got_hit()
                self.naomi.got_hit(self.helga)
                self.helga.render()
                if self.naomi.health > 0:
                    self.naomi.render(False)
                self.render_bullets()
                self.remove_bullets()        
            else:
                self.win.blit(load("assets/mitsuwa.png"),(800,475,300,300))
                self.naomi.horizontal_coordinate = 600
                self.naomi.render(True)

            pygame.display.update()

    
if __name__ == "__main__":
    main().run_game()
