import pygame

import Constants
import Property
from CommunityChest import CommunityChest
from Player import Player
from chanceCard import chanceCard

pygame.init()

screen = pygame.display.set_mode((950, 950))

# Draw the board
pygame.display.set_caption('Monopoly')
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('images/icon.jpg'), (88, 125)))

board = pygame.image.load('images/Board.jpg').convert()
board = pygame.transform.scale(board, (650, 650))
screen.fill(pygame.Color('gray'))
screen.blit(board, (150, 150))

pygame.mouse.set_visible(False)

font = pygame.font.SysFont('calibri', 32)

running = True
money = 0
debug = False

players = [
    Player(money, (255, 0, 0), (740, 770)),
    Player(money, (0, 255, 0), (730, 770)),
    Player(money, (0, 0, 255), (740, 790)),
    Player(money, (255, 165, 0), (750, 780))
]

for player in players:
    player.draw()
    player.drawMoney()

Constants.drawPlayerText()

pygame.display.update()

while True:
    screen.blit(board, (150, 150))

    for player in players:
        if not player.inJail:
            roll = Constants.rollDice()
            for i in range(roll):
                screen.blit(board, (150, 150))

                if player.square < 39:
                    player.square += 1
                else:
                    player.square = 0
                    player.money += 200
                    player.drawMoney()

                Constants.drawAllPlayers()

                pygame.display.update()
                pygame.time.delay(50)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

            pygame.mouse.set_visible(True)

            prop = Constants.properties[player.square]
            if type(prop) == Property.Property:
                prop.handleActions(player)
                screen.blit(board, (150, 150))
                pygame.display.update()

            else:
                if prop in ('income tax', 'luxury tax'):
                    Property.handleTax(player)

                elif prop == 'chance':
                    chanceCard(player)

                elif prop == 'chest':
                    CommunityChest(player)

                elif prop == 'go to jail':
                    player.inJail = True
                    player.square = 10
                    player.draw()

                Constants.drawPlayerText()
                player.drawMoney()

            pygame.mouse.set_visible(False)

        else:
            player.handleJail()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Constants.handleExit()

        pygame.display.update()
        pygame.time.delay(50)
