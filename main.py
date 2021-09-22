import pygame

# inititilize the pygame
pygame.init()


# create screen with height 800px and width 600px
screen = pygame.display.set_mode((800, 600))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
