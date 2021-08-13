import pygame, Constants

pygame.init()


class Property:
    def __init__(self, name: str, cost: int, rent, color, icon=None):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None
        self.color = color
        self.icon = icon

    def drawCard(self, x2):
        from main import screen, roll, player

        font = pygame.font.SysFont('arial', 20)
        pygame.draw.rect(screen, (250, 250, 250), (350, 250, 300, 400))

        if self.rent != 'special':
            pygame.draw.rect(screen, (0, 0, 0), (349, 249, 302, 402), 1)
            pygame.draw.rect(screen, self.color, (350, 251, 300, 100))
            pygame.draw.rect(screen, (0, 0, 0), (349, 249, 302, 102), 1)
            pygame.draw.rect(screen, (0, 0, 0), (349, 249, 302, 102), 1)

            text = font.render(self.name.upper(), True, (0, 0, 0))
            if self.icon:
                screen.blit(pygame.image.load(self.icon).convert(), (450, 260))
                screen.blit(text, (430 - (len(self.name) / 2) * 10, 370))
                text = font.render('Cost: ' + str(self.cost) + '          Rent: ' + str(self.rent), True, (0, 0, 0))
                screen.blit(text, (400, 390))
            else:
                screen.blit(text, (430 - len(self.name) / 2, 370))
                text = font.render('Cost: ' + str(self.cost) + '          Rent: ' + str(self.rent), True, (0, 0, 0))
                screen.blit(text, (400, 410))

        else:
            specialFont = pygame.font.SysFont('arial', 16)

            text = font.render(self.name.upper(), True, (0, 0, 0))
            if self.icon:
                screen.blit(pygame.image.load(self.icon).convert(), (450, 270))
                screen.blit(text, (500 - (len(self.name) / 2) * 10, 360))
                text = font.render('Cost: ' + str(self.cost) + '          Rent: ' + str(self.rent), True, (0, 0, 0))
                screen.blit(text, (400, 400))
            else:
                screen.blit(text, (500 - len(self.name) / 2, 370))
                text = font.render('Cost: ' + str(self.cost) + '          Rent: ' + str(self.rent), True, (0, 0, 0))
                screen.blit(text, (400, 420))

            if 'Railroad' in self.name or self.name == 'Short Line':
                train = pygame.image.load('images/train icon.png').convert()
                train = pygame.transform.scale(train, (30, 20))

                for i in range(1, 5):
                    screen.blit(train, (400, 400 + i * 30))
                    if i == 1:
                        text = specialFont.render('If ' + str(i) + ' railroad owned: ' + str(i * 25), True, (0, 0, 0))
                    else:
                        text = specialFont.render('If ' + str(i) + ' railroads owned: ' + str(i * 25), True, (0, 0, 0))
                    screen.blit(text, (450, 400 + i * 30))

            if self.name in ('Electric Company', 'Water Works'):
                text = specialFont.render('If one Utility is owned,', True, (0, 0, 0))
                screen.blit(text, (420, 440))
                if self.owner is None:
                    text = specialFont.render('rent is 4 times the dice roll.', True, (0, 0, 0))
                else:
                    text = specialFont.render('rent is 4 times the dice roll (' + str(roll) + ').', True, (0, 0, 0))
                screen.blit(text, (420, 460))

                text = specialFont.render('If both Utilities are owned,', True, (0, 0, 0))
                screen.blit(text, (420, 490))
                if self.owner is None:
                    text = specialFont.render('rent is 10 times the dice roll.', True, (0, 0, 0))
                else:
                    text = specialFont.render('rent is 10 times the dice roll (' + str(roll) + ').', True, (0, 0, 0))
                screen.blit(text, (420, 510))

        if self.owner is None:
            if not x2:
                if player.money >= self.cost:
                    pygame.draw.rect(screen, (0, 0, 200), (380, 590, 70, 30))
                    pygame.draw.rect(screen, (100, 100, 255), (375, 585, 80, 40), 5, 5, 5, 5, 5)

                else:
                    pygame.draw.rect(screen, (128, 128, 200), (380, 590, 70, 30))
                    pygame.draw.rect(screen, (150, 150, 255), (375, 585, 80, 40), 5, 5, 5, 5, 5)

                text = font.render('Buy', True, pygame.Color('white'))
                screen.blit(text, (400, 590))

                pygame.draw.rect(screen, (200, 200, 200), (550, 590, 70, 30))
                pygame.draw.rect(screen, (150, 150, 150), (545, 585, 80, 40), 5, 5, 5, 5, 5)
                text = font.render('Cancel', True, pygame.Color('black'))
                screen.blit(text, (560, 590))

            else:
                pygame.draw.rect(screen, (0, 0, 200), (450, 590, 100, 30))
                pygame.draw.rect(screen, (100, 100, 255), (445, 585, 110, 40), 5, 5, 5, 5, 5)

                text = font.render('Get for free', True, pygame.Color('white'))
                screen.blit(text, (460, 590))

        else:
            playerNo = {
                (255, 0, 0): '1',
                (0, 255, 0): '2',
                (0, 0, 255): '3',
                (255, 165, 0): '4',
            }

            if self.owner == player:
                text = font.render("Owner: yourself!", True, (0, 0, 0))
            else:
                text = font.render("Owner: Player " + playerNo[self.owner.color], True, (0, 0, 0))
                pygame.draw.circle(screen, self.owner.color, (540, 610), 10)

            screen.blit(text, (430, 550))

            pygame.draw.rect(screen, (0, 0, 200), (450, 590, 100, 30))
            pygame.draw.rect(screen, (100, 100, 255), (445, 585, 110, 40), 5, 5, 5, 5, 5)

            if self.owner == player:
                text = font.render('Ok', True, pygame.Color('white'))
                screen.blit(text, (490, 590))
            else:
                text = font.render('Pay rent', True, pygame.Color('white'))
                screen.blit(text, (470, 590))

        pygame.display.update()

    def handleActions(self, player, x2=False):
        from Constants import drawPlayerText
        from main import screen
        self.drawCard(x2)

        if self.owner is None:
            checked = False
            selectedBuy = True
            prevkey = 'none'

            while not checked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button <= 3:
                            if (375 < event.pos[0] < 455 and 585 < event.pos[1] < 625) and not x2:
                                if player.money >= self.cost:
                                    self.owner = player
                                    player.money -= self.cost

                                    checked = True

                        elif (545 < event.pos[0] < 625 and 585 < event.pos[1] < 625) and not x2:
                            checked = True

                        elif (450 < event.pos[0] < 550 and 590 < event.pos[1] < 620) and x2:
                            self.owner = player
                            checked = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                    if selectedBuy and player.money >= self.cost:
                        self.owner = player
                        player.money -= self.cost

                    checked = True

                elif keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                    if prevkey != 'changeBuy':
                        selectedBuy = not selectedBuy
                        prevkey = 'changeBuy'

                        if selectedBuy:
                            pygame.draw.rect(screen, (100, 100, 255), (375, 585, 80, 40), 5, 5, 5, 5, 5)
                            pygame.draw.rect(screen, (150, 150, 150), (545, 585, 80, 40), 5, 5, 5, 5, 5)
                        else:
                            pygame.draw.rect(screen, (100, 100, 255), (545, 585, 80, 40), 5, 5, 5, 5, 5)
                            pygame.draw.rect(screen, (0, 0, 150), (375, 585, 80, 40), 5, 5, 5, 5, 5)

                        pygame.display.update()

                else:
                    prevkey = 'none'

                pygame.time.delay(50)

        else:
            checked = False
            while not checked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button <= 3:
                            if 425 < event.pos[0] < 530 and 484 < event.pos[1] < 620:
                                if self.owner is not player:
                                    self.payRent(player, x2)
                                    self.owner.drawMoney()
                                    player.drawMoney()

                                checked = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    while keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                        keys = pygame.key.get_pressed()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Constants.handleExit()

                        pygame.time.delay(100)

                    if self.owner is not player:
                        self.payRent(player, x2)
                        self.owner.drawMoney()
                        player.drawMoney()

                    while keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                        keys = pygame.key.get_pressed()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Constants.handleExit()

                        pygame.time.delay(100)

                    checked = True

                elif keys[pygame.K_F3] and keys[pygame.K_b]:
                    player.money = 80
                    player.handleNotEnoughMoney(100)
                    checked = True

                pygame.time.delay(50)

        drawPlayerText()
        player.drawMoney()

    def payRent(self, player, x2=False):
        if self.rent != 'special':
            if player.money >= self.rent * (int(x2) + 1):
                player.money -= self.rent * (int(x2) + 1)
                self.owner.money += self.rent * (int(x2) + 1)
            else:
                player.handleNotEnoughMoney(self.rent, self.owner)

        else:
            if 'Railroad' in self.name or self.name == 'Short Line':
                railroadsOwned = 0
                for prop in Constants.properties:
                    if type(prop) == Property and (
                            'Railroad' in prop.name or prop.name == 'Short Line') and prop.owner == self.owner:
                        railroadsOwned += 1

                rent = 25 * railroadsOwned * (int(x2) + 1)
                if player.money >= rent:
                    player.money -= rent
                    self.owner.money += rent
                else:
                    player.handleNotEnoughMoney(rent, self.owner)

            elif self.name in ('Electric Company', 'Water Works'):
                from main import roll
                if Constants.properties[28].owner is Constants.properties[12].owner:
                    if x2:
                        multiply = 20
                    else:
                        multiply = 10
                else:
                    if x2:
                        multiply = 8
                    else:
                        multiply = 4

                rent = multiply * roll
                if player.money >= rent:
                    player.money -= rent
                    self.owner.money += rent

                else:
                    player.handleNotEnoughMoney(rent, self.owner)

        player.drawMoney()
        self.owner.drawMoney()


def handleTax(player):
    from main import screen, font, prop, board

    pygame.draw.rect(screen, (250, 250, 250), (350, 250, 300, 400))

    if player.square == 4:
        text = font.render('INCOME TAX', True, (0, 0, 0))
        screen.blit(text, (420, 300))

    else:
        text = font.render('LUXURY TAX', True, (0, 0, 0))
        screen.blit(text, (420, 300))

        ring = pygame.image.load('images/luxury icon.png').convert()
        screen.blit(ring, (420, 400))

    pygame.draw.rect(screen, (0, 0, 200), (450, 590, 100, 30))
    pygame.draw.rect(screen, (100, 100, 255), (445, 585, 110, 40), 5, 5, 5, 5, 5)
    pygame.font.SysFont('calibri', 24).render('Pay tax', True, pygame.Color('white'))
    screen.blit(text, (470, 595))

    pygame.mouse.set_visible(True)

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
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            checked = True

        pygame.time.delay(50)

    if prop == 'income tax':
        if player.money > 200:
            player.money -= 200
        else:
            player.handleNotEnoughMoney(200)
    else:
        if player.money > 100:
            player.money -= 100
        else:
            player.handleNotEnoughMoney(100)

    screen.blit(board, (150, 150))
    player.drawMoney()
    pygame.mouse.set_visible(False)
