import pygame  
import sys  
    
pygame.init()
screen = pygame.display.set_mode((1080, 600))
width = screen.get_width()
height = screen.get_height()
color_light = (170,170,170)


color_dark = (100,100,100)
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")

    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(screen, color_dark, [width/2-150, height/2, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2+150, height/2, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2, height/2+150, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2, height/2-150, 100, 100])

    pygame.draw.rect(screen, color_dark, [width/2-150, height/2-150, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2+150, height/2+150, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2-150, height/2+150, 100, 100])
    pygame.draw.rect(screen, color_dark, [width/2+150, height/2-150, 100, 100])

    if width/2 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+100:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEWHEEL:
                pygame.draw.rect(screen, "blue", [width/2, height/2, 100, 100])
                pygame.display.update()
            else:
                pygame.draw.rect(screen, "red", [width/2, height/2, 100, 100])
                pygame.display.update()
    else:
        pygame.draw.rect(screen, color_light, [width/2, height/2, 100, 100])

    pygame.display.update()

pygame.quit()