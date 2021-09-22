import pygame

# inititilize the pygame
pygame.init()


# create screen with height 600px and width 800px
screen = pygame.display.set_mode((800, 600))


#title and icon
pygame.display.set_caption('Space Invaders by Ross')
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500

playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    # rgb background
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.3

        # check  wherther we release the button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    pygame.display.update()
