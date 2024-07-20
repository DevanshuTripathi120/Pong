import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

def gameLoop():
    length = 100
    score = 0
    x = 0
    y = 250 - length/2

    X = 485
    Y = 250 - length/2

    rad = 10
    ballx = 15 + rad
    bally = 250
    ex=1
    ey=1

    running = True

    sped=0.01

    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("blue")
        ball = pygame.draw.circle(screen, "green", (ballx, bally), rad)
        player = pygame.draw.rect(screen, "red", pygame.Rect(x, y, 15, length))
        comp = pygame.draw.rect(screen, "red", pygame.Rect(X, Y, 15, length))

        vel = 300 * dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= vel
        if keys[pygame.K_s]:
            y += vel
        if y < 0:
            y=0
        if y > screen.get_width() - length:
            y=500 - length

        if keys[pygame.K_UP]:
            Y -= vel
        if keys[pygame.K_DOWN]:
            Y += vel
        if Y < 0:
            Y=0
        if Y > screen.get_width() - length:
            Y=500 - length

        xb = ballx
        yb = bally
        
        if (ballx < 15 + rad and (bally<y or bally> y + length)) or (ballx > 500 - 15 - rad and (bally<Y or bally> Y + length)):
            running = False
            gameMenu(score)
        elif (ballx == 15 + rad and (bally>=y and bally<= y + length/2)):
            ballx = xb
            ex = 1
            bally = yb
            ey = -1
            score+=1
            diff = abs(y+length/2 - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx == 15 + rad and (bally>y + length/2 and bally< y + length)):
            ballx = xb
            ex = 1
            bally = yb
            ey = 1
            score+=1
            diff = abs(length - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx == 500 - 15 - rad and (bally>=Y and bally<= Y + length/2)):
            ballx = xb
            ex = -1
            bally = yb
            ey = -1
            score+=1
            diff = abs(Y+length/2 - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx == 500 - 15 - rad and (bally>Y + length/2 and bally< Y + length)):
            ballx = xb
            ex = -1
            bally = yb
            ey = 1
            score+=1
            diff = abs(length - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        
        ballx += 300 * sped * ex
        bally += 300 * 0.02 * ey
        if bally > 500 - rad:
            bally = yb
            ey*= -1
        if bally < rad:
            bally = yb
            ey*= -1

        pygame.display.update()

        dt = clock.tick(60) / 500

def gameMenu(score):

    sc = score

    font = pygame.font.Font('freesansbold.ttf', 32)
    start = font.render('Start', True, "black", "gray")
    startRect = start.get_rect()
    startRect.center = (250,200)

    swidth = start.get_width()
    sheight = start.get_height()

    font = pygame.font.Font('freesansbold.ttf', 32)
    quit = font.render('Quit', True, "black", "gray")
    quitRect = quit.get_rect()
    quitRect.center = (250,300)

    qwidth = quit.get_width()
    qheight = quit.get_height()

    font = pygame.font.Font('freesansbold.ttf', 32)
    scored = font.render(f'Score: {sc}', True, "black", "gray")
    scoredRect = scored.get_rect()
    scoredRect.center = (250,250)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 250 - swidth/2 <= x <= 250 + swidth/2 and 200 - sheight/2 <= y <= 200 + sheight/2 :
                    gameLoop()
                    running = False
                if 250 - qwidth/2 <= x <= 250 + qwidth/2 and 300 - qheight/2 <= y <= 300 + qheight/2 :
                    running = False

        screen.fill("blue")
        screen.blit(start, startRect)
        screen.blit(quit, quitRect)
        screen.blit(scored, scoredRect)

        pygame.display.update()

        clock.tick(60)

gameMenu(0)
pygame.quit()