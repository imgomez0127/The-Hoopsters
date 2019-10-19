import pygame
import os
pygame.init()
win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Test Game")
x = 50
y = 800
velocity = 50
width = 50
height = 100
jump_counter = 5
is_jumping = False
run_game = True
while run_game:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x = max(0,x-velocity)
    if keys[pygame.K_d]:
        x = min(1920-width,x+velocity)
    if is_jumping == False:
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            is_jumping = True
        if keys[pygame.K_s]:
            render_height = height/2
            render_y = y + height/2
        else:
            render_height = height
            render_y = y
    else:
        render_y += 2 * ((jump_counter ** 2) * (1 - 2 * (jump_counter > 0)))
        jump_counter -= 1 
        if jump_counter == -6:
            jump_counter = 5
            is_jumping = False
    pygame.draw.rect(win, (255,0,0), (x,render_y,width,render_height))
    pygame.display.update() 
pygame.quit()
