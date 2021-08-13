from random import randint

import pygame

from Property import Property

pygame.init()
properties = [
    'go',
    Property('Mediterranean Avenue', 60, 4, (149, 84, 54)),
    'chest',
    Property('Baltic Avenue', 60, 2, (149, 84, 54)),
    'income tax',
    Property('Reading Railroad', 200, 'special', None, 'images/train icon.png'),
    Property('Oriental Avenue', 100, 6, (170, 224, 250)),
    'chance',
    Property('Vermont Avenue', 100, 6, (170, 224, 250)),
    Property('Connecticut Avenue', 120, 8, (170, 224, 250)),
    'jail',
    Property('St. Charles Place', 140, 10, (217, 58, 150)),
    Property('Electric Company', 150, 'special', None, 'images/light icon.png'),
    Property('States Avenue', 140, 10, (217, 58, 150)),
    Property('Virginia Avenue', 160, 12, (217, 58, 150)),
    Property('Pennsylvania Railroad', 200, 'special', None, 'images/train icon.png'),
    Property('St. James Place', 180, 14, (247, 148, 29)),
    'chest',
    Property('Tennessee Avenue', 180, 14, (247, 148, 29)),
    Property('New York Avenue', 200, 16, (247, 148, 29)),
    'parking',
    Property('Kentucky Avenue', 220, 18, (237, 27, 36)),
    'chance',
    Property('Indiana Avenue', 220, 18, (237, 27, 36)),
    Property('Illinois Avenue', 240, 20, (237, 27, 36)),
    Property('B. & O. Railroad', 200, 'special', None, 'images/train icon.png'),
    Property('Atlantic Avenue', 260, 22, (254, 242, 0)),
    Property('Ventnor Avenue', 260, 22, (254, 242, 0)),
    Property('Water Works', 150, 'special', None, 'images/hose icon.png'),
    Property('Marvin Gardens', 280, 24, (254, 242, 0)),
    'go to jail',
    Property('Pacific Avenue', 300, 26, (34, 176, 90)),
    Property('North Carolina Avenue', 300, 26, (34, 176, 90)),
    'chest',
    Property('Pennsylvania Avenue', 320, 28, (34, 176, 90)),
    Property('Short Line', 200, 'special', None, 'images/train icon.png'),
    'chance',
    Property('Park Place', 350, 35, (0, 114, 187)),
    'luxury tax',
    Property('Boardwalk', 400, 50, (0, 114, 187))
]

prevkey = 'none'
debugFont = pygame.font.SysFont('calibri', 16)


def drawAllPlayers():
    from main import players, screen, board

    screen.blit(board, (150, 150))
    for player in players:
            player.draw()

def drawPlayerText():
    from main import font, screen
    text = font.render('Player 1', True, pygame.Color('black'))
    screen.blit(text, (400, 100))
    pygame.draw.circle(screen, pygame.Color('red'), (540, 110), 20)

    text = pygame.transform.rotate(font.render('Player 3', True, pygame.Color('black')), -90)
    screen.blit(text, (100, 400))
    pygame.draw.circle(screen, pygame.Color('blue'), (120, 530), 20)

    text = pygame.transform.rotate(font.render('Player 2', True, pygame.Color('black')), 90)
    screen.blit(text, (820, 400))
    pygame.draw.circle(screen, pygame.Color('green'), (835, 370), 20)

    text = font.render('Player 4', True, pygame.Color('black'))
    screen.blit(text, (400, 820))
    pygame.draw.circle(screen, pygame.Color('orange'), (530, 835), 20)


def drawDice(dots, dice2=False):
    import main

    if dice2:
        xAdd = 100
        pygame.draw.rect(main.screen, (250, 250, 250), (625, 525, 50, 50), 0, 5, 5, 5, 5)
    else:
        xAdd = 0
        pygame.draw.rect(main.screen, (250, 250, 250), (525, 525, 50, 50), 0, 5, 5, 5, 5)

    dots += 1

    if dots == 1 or dots == 3 or dots >= 5:
        pygame.draw.circle(main.screen, pygame.Color('black'), (550 + xAdd, 550), 4)
    if dots != 1:
        pygame.draw.circle(main.screen, pygame.Color('black'), (540 + xAdd, 540), 4)
        pygame.draw.circle(main.screen, pygame.Color('black'), (560 + xAdd, 560), 4)
    if 4 <= dots <= 6:
        pygame.draw.circle(main.screen, pygame.Color('black'), (540 + xAdd, 560), 4)
        pygame.draw.circle(main.screen, pygame.Color('black'), (560 + xAdd, 540), 4)
    if dots == 6:
        pygame.draw.circle(main.screen, pygame.Color('black'), (540 + xAdd, 550), 4)
        pygame.draw.circle(main.screen, pygame.Color('black'), (560 + xAdd, 550), 4)

    pygame.display.update((525, 525, 50 + xAdd, 50))


def rollDice(returnTuple=False):
    from main import screen, board, players

    roll1 = randint(1, 6)
    roll2 = randint(1, 6)

    drawAllPlayers()

    for i in range(roll1):
        for j in range(3):
            drawDice(i)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    drawPlayerText()
                    handleExit()
                    screen.blit(board, (150, 150))
                    pygame.display.update()

            pygame.time.delay(100)

    for i in range(roll2):
        for j in range(3):
            drawDice(i, True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    drawPlayerText()
                    handleExit()
                    screen.blit(board, (150, 150))
                    pygame.display.update()

            pygame.time.delay(100)

    for i in range(10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawPlayerText()
                handleExit()
                screen.blit(board, (150, 150))
                pygame.display.update()

        pygame.time.delay(100)

    if not returnTuple:
        return roll1 + roll2
    else:
        return roll1, roll2


def handleExit():
    """
    This uses an experimental feature in PyGame,
    but it is a really simple solution to open another window.

    This may break in future PyGame releases.
    """

    from pygame._sdl2.video import messagebox

    if messagebox("Exit?", "Are you sure you want to exit?", warn=True, buttons=("Yes", "No"), return_button=0, escape_button=1) == 0:
        pygame.display.quit()
        pygame.quit()
        quit()
