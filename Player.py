import pygame, Constants

import Property

pygame.init()


class Player:
    def __init__(self, money, color, startPos):
        self.exitJailFreeCard = False
        self.money = money
        self.square = 0
        self.color = color
        self.startPos = startPos
        self.bankrupt = False

        self.inJail = False
        self.escapeAttempts = 0

        import main
        self.screen = main.screen
        self.font = pygame.font.SysFont('calibri', 32)
        self.board = main.board

    def draw(self):
        # Complicated equations for drawing the player on the current square
        if 0 <= self.square < 10:
            pos = (self.startPos[0] - 530 + (53 * (10 - self.square)), self.startPos[1])

        elif self.square == 10:
            if self.inJail:
                pos = (self.startPos[0] - 553, 790)
            else:
                pos = (self.startPos[0] - 553, 750)

        elif 10 < self.square < 21:
            pos = (self.startPos[0] - 530, 973 - self.startPos[1] + 53 * (20 - self.square))

        elif 21 <= self.square < 31:
            pos = ((self.startPos[0] - 583) + 53 * (self.square - 19), self.startPos[1] - 580)

        else:
            pos = (self.startPos[0], 1000 - self.startPos[1] + 53 * (self.square - 30))

        pygame.draw.circle(self.screen, self.color, pos, 10)
        pygame.display.update((pos[0] - 80, pos[1] - 80), (pos[0], pos[1]))

    def drawMoney(self):
        money = self.money
        subtract = [500, 100, 50, 20, 10, 5, 1]
        types = 0

        if self.color == pygame.Color('red'):
            self.screen.fill(pygame.Color('gray'), (150, 0, 750, 150))
        elif self.color == pygame.Color('green'):
            self.screen.fill(pygame.Color('gray'), (850, 0, 150, 850))
        elif self.color == pygame.Color('blue'):
            self.screen.fill(pygame.Color('gray'), (0, 150, 150, 750))
        elif self.color == pygame.Color('orange'):
            self.screen.fill(pygame.Color('gray'), (150, 800, 850, 150))
        Constants.drawPlayerText()

        for number in subtract:
            if money // number > 0:
                types += 1
                for i in range(money // number):
                    money -= number
                    if self.color == pygame.Color('red'):
                        bill = pygame.image.load('images/bills/$' + str(number) + '.png')
                        self.screen.blit(bill, (i * 10 + types * 200 - 50, 10 + i * 10))

                    elif self.color == pygame.Color('green'):
                        bill = pygame.transform.rotate(
                            pygame.image.load('images/bills/$' + str(number) + '.png'), 90)
                        self.screen.blit(bill, (850 + i * 10, 850 + i * 10 - types * 200))

                    elif self.color == pygame.Color('blue'):
                        bill = pygame.transform.rotate(
                            pygame.image.load('images/bills/$' + str(number) + '.png'), -90)
                        self.screen.blit(bill, (10 + i * 10, i * 10 + types * 200 - 50))

                    elif self.color == pygame.Color('orange'):
                        bill = pygame.image.load('images/bills/$' + str(number) + '.png')
                        self.screen.blit(bill, (i * 10 + types * 200 - 50, 850 + i * 10))

        pygame.display.update()

    def handleJail(self):
        self.square = 10
        pygame.mouse.set_visible(True)

        font = pygame.font.SysFont('calibri', 32)
        buttonFont = pygame.font.SysFont('calibri', 24)
        pygame.draw.rect(self.screen, (250, 250, 250), (350, 250, 300, 400))

        text = font.render('You can get out', True, (0, 0, 0))
        self.screen.blit(text, (400, 300))

        text = font.render('of jail by:', True, (0, 0, 0))
        self.screen.blit(text, (430, 340))

        icon = pygame.image.load('images/jail.png')
        self.screen.blit(icon, (430, 400))

        if self.exitJailFreeCard:
            pygame.draw.rect(self.screen, (0, 0, 200), (425, 545, 135, 30))
            pygame.draw.rect(self.screen, (100, 100, 255), (425, 540, 140, 40), 5, 5, 5, 5, 5)
            text = pygame.font.SysFont('calibri', 16).render('Using Get Out', True, (255, 255, 255))
            self.screen.blit(text, (445, 545))
            text = pygame.font.SysFont('calibri', 16).render('of Jail Free Card', True, (255, 255, 255))
            self.screen.blit(text, (440, 560))

        else:
            if (self.money >= 50 or self.exitJailFreeCard) or (self.money < 50 and not self.exitJailFreeCard and self.escapeAttempts >= 3):
                pygame.draw.rect(self.screen, (0, 0, 200), (425, 545, 130, 30))
                pygame.draw.rect(self.screen, (100, 100, 255), (420, 540, 140, 40), 5, 5, 5, 5, 5)
                text = buttonFont.render('Paying $50', True, (255, 255, 255))
                self.screen.blit(text, (440, 550))

            else:
                pygame.draw.rect(self.screen, (128, 128, 200), (425, 545, 130, 30))
                pygame.draw.rect(self.screen, (150, 150, 255), (420, 540, 140, 40), 5, 5, 5, 5, 5)
                text = buttonFont.render('Paying $50', True, (255, 255, 255))
                self.screen.blit(text, (440, 550))

        if self.escapeAttempts < 3:
            pygame.draw.rect(self.screen, (0, 0, 200), (415, 603, 165, 30))
            pygame.draw.rect(self.screen, (100, 100, 255), (415, 598, 170, 40), 5, 5, 5, 5, 5)
            text = buttonFont.render('Rolling Doubles', True, (255, 255, 255))
            self.screen.blit(text, (430, 605))

        pygame.display.update()

        clock = pygame.time.Clock()
        checked = False
        while not checked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Constants.handleExit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if 420 < event.pos[0] < 560 and 540 < event.pos[1] < 580 and (self.money >= 50 or (self.money < 50 and not self.exitJailFreeCard and self.escapeAttempts >= 3)):
                        if self.money >= 50:
                            self.money -= 50
                            self.drawMoney()
                            checked = True

                            self.inJail = False

                            self.screen.blit(self.board, (150, 150))
                            Constants.drawAllPlayers()
                            pygame.display.update()

                            roll = Constants.rollDice()

                            for i in range(roll):
                                self.screen.blit(self.board, (150, 150))

                                if self.square < 39:
                                    self.square += 1
                                else:
                                    self.square = 0
                                    self.money += 200
                                    self.drawMoney()

                                Constants.drawAllPlayers()

                                clock.tick(60)

                        else:
                            self.handleNotEnoughMoney(50)

                    elif 415 < event.pos[0] < 585 and 498 < event.pos[1] < 538 and self.exitJailFreeCard:
                        self.screen.blit(self.board, (150, 150))
                        Constants.drawAllPlayers()
                        pygame.display.update()

                        self.inJail = False
                        self.exitJailFreeCard = False

                        roll = Constants.rollDice()
                        for i in range(roll):
                            self.screen.blit(self.board, (150, 150))

                            self.square += 1

                            Constants.drawAllPlayers()
                            pygame.display.update()

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Constants.handleExit()

                            clock.tick(60)

                        checked = True

                    elif 415 < event.pos[0] < 585 and 598 < event.pos[1] < 638 and self.escapeAttempts < 3:
                        self.screen.blit(self.board, (150, 150))
                        Constants.drawAllPlayers()
                        pygame.display.update()

                        roll1, roll2 = Constants.rollDice(True)
                        self.escapeAttempts += 1

                        if roll1 == roll2:
                            self.inJail = False

                            for i in range(roll1 + roll2):
                                self.screen.blit(self.board, (150, 150))

                                self.square += 1

                                Constants.drawAllPlayers()
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        Constants.handleExit()

                                clock.tick(60)

                        checked = True
                        self.escapeAttempts = 0

            clock.tick(60)

    def handleNotEnoughMoney(self, money, owner=None):
        from main import screen
        import Constants

        money -= self.money

        clock = pygame.time.Clock()

        font = pygame.font.SysFont('calibri', 32)
        buttonFont = pygame.font.SysFont('calibri', 24)
        smallFont = pygame.font.SysFont('calibri', 20)
        pygame.draw.rect(screen, (250, 250, 250), (350, 250, 300, 400))

        canSell = []
        for prop in Constants.properties:
            if type(prop) is Property.Property and prop.owner is self:
                canSell.append(prop)

        if len(canSell) > 0:
            text = font.render('You can get', True, (0, 0, 0))
            screen.blit(text, (430, 300))

            text = font.render('money by:', True, (0, 0, 0))
            screen.blit(text, (430, 340))

            pygame.draw.rect(screen, (0, 0, 200), (415, 603, 165, 30))
            pygame.draw.rect(screen, (100, 100, 255), (415, 598, 170, 40), 5, 5, 5, 5, 5)
            text = buttonFont.render('Selling Property', True, (255, 255, 255))
            screen.blit(text, (430, 605))

            pygame.display.update()

            moneyType = 0
            while moneyType == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if 415 < event.pos[0] < 635 and 598 < event.pos[1] < 638:
                            moneyType = 1

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    moneyType = 1

                clock.tick(60)

            if moneyType == 1:
                pageNum = 1

                pygame.draw.rect(screen, (250, 250, 250), (250, 150, 450, 550))
                pygame.draw.rect(screen, (0, 0, 0), (250, 150, 450, 550), 1)
                text = font.render('You can sell:', True, (0, 0, 0))
                screen.blit(text, (350, 200))

                text = smallFont.render("Property:", True, (0, 0, 0))
                screen.blit(text, (300, 250))

                text = smallFont.render("Mortgage Value:", True, (0, 0, 0))
                screen.blit(text, (500, 250))

                for i in range((pageNum - 1) * 7, pageNum * 7):
                    pygame.draw.rect(screen, (0, 0, 0), (300, 300 + i * 40, 15, 15), 1)
                    text = smallFont.render(canSell[i].name, True, (0, 0, 0))
                    screen.blit(text, (330, 300 + i * 40))

                    text = smallFont.render(str(int(canSell[i].cost * 0.8)), True, (0, 0, 0))
                    screen.blit(text, (600, 300 + i * 40))

                text = buttonFont.render('Click on the properties you', True, (0, 0, 0))
                screen.blit(text, (350, 630))
                text = buttonFont.render('want to sell.', True, (0, 0, 0))
                screen.blit(text, (410, 660))

                screen.blit(pygame.transform.scale(pygame.image.load('images/previous button.png'), (50, 50)),
                            (275, 625))
                screen.blit(pygame.transform.scale(pygame.image.load('images/next button.png'), (50, 50)), (625, 625))

                pygame.display.update()

                selected = [False] * len(canSell)

                checked = False
                moneySelected = 0

                while not checked:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Constants.handleExit()

                        # Check if any of the checkboxes are clicked
                        elif event.type == pygame.MOUSEBUTTONUP:
                            try:
                                for i in range(7):
                                    if 300 < event.pos[0] < 400 and 300 + i * 40 < event.pos[1] < 315 + i * 40:
                                        selected[i + (pageNum - 1) * 7] = not selected[i + (pageNum - 1) * 7]

                                        if selected[i + (pageNum - 1) * 7]:
                                            pygame.draw.line(screen, (0, 255, 0), (300, 305 + i * 40),
                                                             (310, 310 + i * 40), 2)
                                            pygame.draw.line(screen, (0, 255, 0), (310, 310 + i * 40),
                                                             (320, 295 + i * 40), 2)

                                            moneySelected += int(canSell[i + (pageNum - 1) * 7].cost * 0.8)
                                        else:
                                            screen.fill((250, 250, 250), (300, 290 + i % 7 * 40, 20, 30))
                                            pygame.draw.rect(screen, (0, 0, 0), (300, 300 + i % 7 * 40, 15, 15), 1)

                                            moneySelected -= int(canSell[i + (pageNum - 1) * 7].cost * 0.8)

                                        screen.fill((250, 250, 250), (350, 570, 270, 120))

                                        text = smallFont.render('Money paid: ' + str(moneySelected), True, (0, 0, 0))
                                        screen.blit(text, (400, 570))

                                        if money > moneySelected:
                                            text = smallFont.render('Money remaining: ' + str(money - moneySelected),
                                                                    True, (0, 0, 0))
                                        else:
                                            text = smallFont.render("Money remaining: 0", True, (0, 0, 0))
                                        screen.blit(text, (380, 600))

                                        if moneySelected >= money:
                                            pygame.draw.rect(screen, (0, 0, 200), (385, 643, 165, 30))
                                            pygame.draw.rect(screen, (100, 100, 255), (385, 638, 170, 40), 5, 5, 5, 5,
                                                             5)
                                            text = buttonFont.render('Sell Property', True, (255, 255, 255))
                                            screen.blit(text, (403, 645))

                                        else:
                                            pygame.draw.rect(screen, (128, 128, 200), (385, 643, 165, 30))
                                            pygame.draw.rect(screen, (150, 150, 255), (385, 638, 170, 40), 5, 5, 5, 5,
                                                             5)
                                            text = buttonFont.render('Sell Property', True, (200, 200, 200))
                                            screen.blit(text, (403, 645))

                                        pygame.display.update()
                                        break

                            except IndexError:
                                pass

                            # Sell Property button
                            if 385 < event.pos[0] < 555 and 638 < event.pos[1] < 678 and moneySelected >= money:
                                for j in range(len(canSell)):
                                    if selected[j]:
                                        canSell[j].owner = owner

                                self.money = moneySelected - money
                                checked = True

                            # Previous page button
                            elif 275 < event.pos[0] < 325 and 625 < event.pos[1] < 675 and pageNum > 1:
                                pageNum -= 1

                                screen.fill((250, 250, 250), (300, 300, 350, 270))

                                try:
                                    for i in range((pageNum - 1) * 7, pageNum * 7):
                                        pygame.draw.rect(screen, (0, 0, 0), (300, 300 + i * 40, 15, 15), 1)
                                        text = smallFont.render(canSell[i].name, True, (0, 0, 0))
                                        screen.blit(text, (330, 300 + i * 40))

                                        text = smallFont.render(str(int(canSell[i].cost * 0.8)), True, (0, 0, 0))
                                        screen.blit(text, (600, 300 + i * 40))

                                        if selected[i]:
                                            pygame.draw.line(screen, (0, 255, 0), (300, 305 + (i % 7) * 40),
                                                             (310, 310 + (i % 7) * 40), 2)
                                            pygame.draw.line(screen, (0, 255, 0), (310, 310 + (i % 7) * 40),
                                                             (320, 295 + (i % 7) * 40), 2)

                                except IndexError:
                                    pass

                                pygame.display.update()

                            # Next page button
                            elif 625 < event.pos[0] < 675 and 625 < event.pos[1] < 675 and pageNum <= len(
                                    canSell) // 7:
                                pageNum += 1

                                screen.fill((250, 250, 250), (300, 300, 350, 270))

                                try:
                                    for i in range((pageNum - 1) * 7, pageNum * 7):
                                        text = smallFont.render(canSell[i].name, True, (0, 0, 0))
                                        screen.blit(text, (330, 300 + (i % 7) * 40))
                                        pygame.draw.rect(screen, (0, 0, 0), (300, 300 + (i % 7) * 40, 15, 15), 1)

                                        text = smallFont.render(str(int(canSell[i].cost * 0.8)), True, (0, 0, 0))
                                        screen.blit(text, (600, 300 + (i % 7) * 40))

                                        if selected[i]:
                                            pygame.draw.line(screen, (0, 255, 0), (300, 305 + (i % 7) * 40),
                                                             (310, 310 + (i % 7) * 40), 2)
                                            pygame.draw.line(screen, (0, 255, 0), (310, 310 + (i % 7) * 40),
                                                             (320, 295 + (i % 7) * 40), 2)

                                except IndexError:
                                    pass

                                pygame.display.update()

                            elif 385 < event.pos[0] < 555 and 638 < event.pos[1] < 678:
                                self.money = moneySelected - money
                                if owner:
                                    for i in range(len(selected)):
                                        if selected[i]:
                                            canSell[i].owner = owner
                                            checked = True

                    clock.tick(60)

        else:
            text = buttonFont.render('You are bankrupt!', True, (0, 0, 0))
            screen.blit(text, (410, 300))

            pygame.draw.rect(screen, (0, 0, 200), (425, 603, 125, 30))
            pygame.draw.rect(screen, (100, 100, 255), (425, 598, 130, 40), 5, 5, 5, 5, 5)
            text = buttonFont.render('Exit Game', True, (255, 255, 255))
            screen.blit(text, (440, 605))

            pygame.display.update()

            checked = False
            while not checked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Constants.handleExit()

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if 415 < event.pos[0] < 545 and 598 < event.pos[1] < 638:
                            checked = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    while keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                        keys = pygame.key.get_pressed()
                        pygame.event.get()
                        pygame.time.delay(100)

                    checked = True

                clock.tick(60)

            self.money = 0
            self.screen.blit(self.board, (150, 150))
            Constants.drawAllPlayers()
            self.drawMoney()

            import main

            main.players.remove(self)

            if len(main.players) == 1:
                colors = {
                    (255, 0, 0): '1',
                    (0, 255, 0): '2',
                    (0, 0, 255): '3',
                    (255, 165, 0): '4',
                }

                pygame.draw.rect(screen, (250, 250, 250), (350, 250, 300, 400))
                pygame.draw.rect(screen, (0, 0, 0), (350, 250, 300, 400), 1)

                text = pygame.font.SysFont('calibri', 60, True).render("Player " + colors[main.players[0].color], True, main.players[0].color)
                main.screen.blit(text, (395, 300))
                text = font.render('wins!', True, (0,0,0))
                main.screen.blit(text, (455, 365))

                pygame.draw.rect(screen, (0, 0, 200), (425, 603, 125, 30))
                pygame.draw.rect(screen, (100, 100, 255), (425, 598, 130, 40), 5, 5, 5, 5, 5)
                text = buttonFont.render('Quit Game', True, (255, 255, 255))
                screen.blit(text, (440, 605))

                pygame.display.update()

                clock = pygame.time.Clock()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Constants.handleExit()

                        elif event.type == pygame.MOUSEBUTTONUP:
                            if 425 < event.pos[0] < 555 and 598 < event.pos[1] < 638:
                                pygame.display.quit()
                                pygame.quit()
                                quit()

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                        pygame.display.quit()
                        pygame.quit()
                        quit()

                    clock.tick(60)
