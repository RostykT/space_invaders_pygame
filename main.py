import pygame

# inititilize the pygame
pygame.init()


# create screen with height 800px and width 600px
screen = pygame.display.set_mode((800, 600))


#title and icon
pygame.display.set_caption('Space Invaders by Ross')
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # rgb background
    screen.fill((0, 0, 0))
    pygame.display.update()
