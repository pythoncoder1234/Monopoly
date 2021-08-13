import pygame,Constants
from random import randint
pygame.init()

def CommunityChest(player):
    cardNo = randint(1,15)
    image = pygame.transform.scale2x(
        pygame.image.load('images/Community Chest/chest' + str(cardNo) + '.png').convert())

    from main import screen, board

    screen.blit(image, (330, 380))
    pygame.draw.rect(screen, (255, 235, 67), (330, 595, 370, 30))
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
        player.money += 200
        player.square = 0

    elif cardNo == 2:
        player.money += 100

    elif cardNo == 3:
        player.money += 10

    elif cardNo == 4:
        player.money += 200

    elif cardNo == 5:
        player.money += 45

    elif cardNo == 6:
        player.money += 20

    elif cardNo == 7:
        player.money += 25

    elif cardNo == 8:
        player.money += 100

    elif cardNo == 9:
        player.money += 100

    elif cardNo == 10:
        from main import players

        for allPlayers in players:
            allPlayers.money -= 50

        player.money += len(players) * 50
        player.money += len(players) * 50

        for allPlayers in players:
            allPlayers.drawMoney()

    elif cardNo == 11:
        if player.money >= 50:
            player.money -= 50
        else:
            player.handleNotEnoughMoney(50)

    elif cardNo == 12:
        if player.money >= 100:
            player.money -= 100
        else:
            player.handleNotEnoughMoney(100)

    elif cardNo == 13:
        if player.money >= 150:
            player.money -= 150
        else:
            player.handleNotEnoughMoney(150)

    elif cardNo == 14:
        pass

    elif cardNo == 15:
        player.inJail = True
        player.square = 10

    elif cardNo == 16:
        player.exitJailFreeCard = True

    player.draw()
    player.drawMoney()

    screen.blit(board,(150,150))
    pygame.mouse.set_visible(False)
