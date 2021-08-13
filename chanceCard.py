import pygame, Constants, Property
from random import randint
from CommunityChest import CommunityChest

pygame.init()


def chanceCard(player):
    cardNo = randint(1,15)
    image = pygame.transform.scale2x(
        pygame.image.load('images/Chance Cards/chance' + str(cardNo) + '.png').convert())

    from main import screen, board

    screen.blit(image, (330, 380))
    pygame.draw.rect(screen, (255, 92, 0), (330, 595, 370, 30))
    pygame.draw.rect(screen, (0, 0, 200), (470, 580, 50, 30))
    pygame.draw.rect(screen, (100, 100, 255), (465, 575, 60, 40), 5, 5, 5, 5, 5)

    font = pygame.font.SysFont('calibri', 20)
    text = font.render('Ok', True, (255, 255, 255))
    screen.blit(text, (480, 585))

    pygame.display.update()
    checked = False

    while not checked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Constants.handleExit()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button <= 3:
                    if 425 < event.pos[0] < 530 and 484 < event.pos[1] < 620:
                        checked = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            while keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                keys = pygame.key.get_pressed()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

                pygame.time.delay(100)

            checked = True

        pygame.time.delay(50)

    if cardNo == 1:
        player.square = 0
        player.money += 200

    elif cardNo == 2:
        player.square = 39
        Constants.drawAllPlayers()
        Constants.properties[39].handleActions(player)

    elif cardNo == 3:
        player.square = 24
        Constants.drawAllPlayers()
        Constants.properties[24].handleActions(player)

    elif cardNo == 4:
        if player.square > 11:
            player.money += 200

        Constants.drawAllPlayers()
        player.square = 11
        Constants.properties[11].handleActions(player)

    elif cardNo == 5:
        if player.square > 5:
            player.money += 200

        player.square = 5
        Constants.drawAllPlayers()
        Constants.properties[5].handleActions(player)

    elif cardNo == 6:
        closest = min(
            [abs(5 - player.square), abs(15 - player.square), abs(25 - player.square), abs(35 - player.square)])

        if (player.square - closest) % 5 == 0 and (player.square - closest) % 10 != 0:
            player.square -= closest
        else:
            player.square += closest

        Constants.drawAllPlayers()
        Constants.properties[player.square].handleActions(player, True)

        from main import board
        screen.blit(board, (150, 150))

    elif cardNo == 7:
        closest = min([abs(12 - player.square), abs(28 - player.square)])

        if player.square - closest == 12 or player.square - closest == 28:
            player.square -= closest
        else:
            player.square += closest

        Constants.drawAllPlayers()
        Constants.properties[player.square].handleActions(player, True)

        from main import board
        screen.blit(board, (150, 150))

    elif cardNo == 8:
        player.square -= 3

        Constants.drawAllPlayers()
        if type(Constants.properties[player.square]) == Property.Property:
            Constants.properties[player.square].handleActions(player)

        elif Constants.properties[player.square] == "income tax":
            Property.handleTax(player)

        else:
            CommunityChest(player)

    elif cardNo == 9:
        player.money += 50

    elif cardNo == 10:
        player.money += 150

    elif cardNo == 11:
        if player.money >= 15:
            player.money -= 15
        else:
            player.handleNotEnoughMoney(15)

    elif cardNo == 12:
        from main import players
        if player.money > 50 * (len(players) - 1):
            player.money -= len(players) * 50

            for allPlayers in players:
                allPlayers.money += 50
                allPlayers.drawMoney()

        else:
            player.handleNotEnoughMoney(50 * (len(players) - 1))

    elif cardNo == 13:
        pass

    elif cardNo == 14:
        player.inJail = True
        player.square = 10

    elif cardNo == 15:
        player.exitJailFreeCard = True

    screen.blit(board, (150, 150))
    player.draw()
    player.drawMoney()
    pygame.mouse.set_visible(False)
