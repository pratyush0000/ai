import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("THE TIC TAC TOE")

#fps
FPS = 60
#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)




def drawwindow(): #watever is drawn later, comes on top.
    WIN.fill(RED)
    pygame.display.update()


def main():
    clock= pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawwindow()

    pygame.quit()

if __name__ == "__main__":
    main()