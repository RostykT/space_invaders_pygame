import pygame
import random

# inititilize the pygame
pygame.init()


# create screen with height 600px and width 800px
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpeg')


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


# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.4
enemyY_change = 30


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop
running = True
while running:
    # rgb background
    screen.fill((0, 0, 0))
    # background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.4

        # check  wherther we release the button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # move player
    playerX += playerX_change

    # border
    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 734
    player(playerX, playerY)

    # move enemy
    enemyX += enemyX_change

    # border
    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change
    elif enemyX >= 764:
        enemyX_change = -0.5
        enemyY += enemyY_change

    enemy(enemyX, enemyY)

    pygame.display.update()
