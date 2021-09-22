import pygame
import random
import math

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
enemyX = random.randint(0, 764)
enemyY = random.randint(50, 150)
enemyX_change = 0.4
enemyY_change = 30


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletY_change = 3
# ready state - it's mean you can't see the bullet on the screen
# fire  - bullet is currently moving
bullet_state = 'ready'

counter = 0


def fire_bullet(x, y):
    global bullet_state

    bullet_state = 'fire'

    screen.blit(bulletImg, (x+16, y+10))


def is_Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    if distance < 27:
        return True
    else:
        return False


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

            # bullet fire
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

    # collision
    collision = is_Collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        counter += 1
        enemyX = random.randint(0, 764)
        enemyY = random.randint(50, 150)

    enemy(enemyX, enemyY)

    # bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    pygame.display.update()
