import pygame
import sys
import random 
import time

pygame.init()

red2 = (180, 44, 0)
black = (0, 0, 0)
green = (50, 205, 50)
brown = (131, 63, 12)

dis_width = 960
dis_height = 760

displayg = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('Resources/snake.png')
pygame.display.set_icon(icon)

fpsClock = pygame.time.Clock()
appl = pygame.image.load('Resources/app.png')
hdImg = pygame.image.load('Resources/snakehd.png')
bod = pygame.image.load('Resources/snakebd.png')
background = pygame.image.load('Resources/grass.png')
tail = pygame.image.load('Resources/snaketail.png')
direction = 'right'
sqr_size = 20
fps = 12
large_font = pygame.font.SysFont("SansSerif", 105)
mid_font = pygame.font.SysFont("SansSerif", 60)
big_font = pygame.font.SysFont("SansSerif", 75)
sqr_x_change = 0 
sqr_y_change = 0
sqr_mov = 20
scr = 0
intro = True

def game_intro():
    global intro
    
    while intro:
        displayg.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
                    
        show_message('Welcome to Snake game!', brown, 36, 200, large_font)
        show_message('Press S to start.', black, 288, 350, big_font)
        show_message('Controls:', black, 288, 450, mid_font)
        show_message('WASD: move snake.', black, 288, 510, mid_font)
        show_message('P: pause game.', black, 288, 570, mid_font)
        
        
        pygame.display.update()
        
        
def snake(sqr_size, snakelist):
    tl = tail
    
    if ([snakelist[0][0], snakelist[0][1] + sqr_size] in snakelist) and ([snakelist[0][0], snakelist[0][1] - sqr_size] not in snakelist): 
        tl = pygame.transform.rotate(tail, 180)
    elif [snakelist[0][0], snakelist[0][1] - sqr_size] in snakelist and [snakelist[0][0], snakelist[0][1] + sqr_size] not in snakelist:
        tl = tail     
    elif [snakelist[0][0]   + sqr_size, snakelist[0][1]] in snakelist and [snakelist[0][0] - sqr_size, snakelist[0][1]] not in snakelist:
        tl = pygame.transform.rotate(tail, 270)    
    elif [snakelist[0][0]   - sqr_size, snakelist[0][1]] in snakelist and [snakelist[0][0] + sqr_size, snakelist[0][1]] not in snakelist:
        tl = pygame.transform.rotate(tail, 90)
    
    if len(snakelist) > 1:    
        displayg.blit(tl, snakelist[0])
        
    for XnY in snakelist[1:-1]:
        displayg.blit(bod, (XnY[0], XnY[1]))
        
    if direction == 'right':
        hd = pygame.transform.rotate(hdImg, 270)
    elif direction == 'left':
        hd = pygame.transform.rotate(hdImg, 90)
    elif direction == 'up':
        hd = hdImg
    elif direction == 'down':
        hd = pygame.transform.rotate(hdImg, 180)
    displayg.blit(hd, snakelist[-1])
        
def show_message(msg, col,x=None, y=None, fnt=mid_font):
    if (x and y) is not None:
        screen_text = fnt.render(msg, True, col)
        displayg.blit(screen_text, (x, y)) 
    else:   
        screen_text = fnt.render(msg, True, col)
        text_rect = screen_text.get_rect()
        text_rect.center = (dis_width / 2, dis_height / 2)
        displayg.blit(screen_text, text_rect)
    
def score(scr):
    show_message('Score: {}'.format(str(scr)), black, 10, 10)
    
def gameLoop():
    global fps
    global direction
    global scr
    global intro 
    gameExit = False
    gameOver = False
    app_thick = 28
    sqr_x = dis_width / 2
    sqr_y = dis_height / 2
    sqr_x_change = 0 
    sqr_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX = random.randrange(0, dis_width - app_thick)
    randAppleY = random.randrange(0, dis_height - app_thick)
    game_intro()

    while not gameExit:
        displayg.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stp = True
                    while stp:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    stp = False            
                if event.key == pygame.K_a and sqr_x_change != sqr_mov:
                    direction = 'left'
                    sqr_x_change = -sqr_mov
                    sqr_y_change = 0
                elif event.key == pygame.K_d and sqr_x_change != -sqr_mov:
                    direction = 'right'
                    sqr_x_change = sqr_mov
                    sqr_y_change = 0
                elif event.key == pygame.K_s and sqr_y_change != -sqr_mov:
                    direction = 'down'
                    sqr_y_change = sqr_mov
                    sqr_x_change = 0
                elif event.key == pygame.K_w and sqr_y_change != sqr_mov:
                    direction = 'up'
                    sqr_y_change = -sqr_mov
                    sqr_x_change = 0
    
        if sqr_x >= dis_width - sqr_size or sqr_x <= 0 or sqr_y >= dis_height - sqr_size or sqr_y <= 0:
            time.sleep(2)
            gameOver = True
    
        sqr_x += sqr_x_change 
        sqr_y += sqr_y_change  
        displayg.blit(appl, (randAppleX, randAppleY))  
        
        snakeHead = []
        snakeHead.append(sqr_x)
        snakeHead.append(sqr_y) 
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
              
        snake(sqr_size, snakeList) 
         
        score(scr)
             
        pygame.display.update()
        
        if snakeHead in snakeList[:-1]:
            time.sleep(2)
            gameOver = True
            
        if ((sqr_x + sqr_size  > randAppleX and sqr_x < randAppleX + app_thick) and 
            (sqr_y + sqr_size  > randAppleY and sqr_y < randAppleY + app_thick)):
            applSound = pygame.mixer.Sound('Resources\eat_apple.wav')
            applSound.play()
            fps += 0.4
            snakeLength += 2
            scr += 1
            randAppleX = random.randrange(0, dis_width - app_thick)
            randAppleY = random.randrange(0, dis_height - app_thick) 
              
        fpsClock.tick(fps)
        
        while gameOver:
            fps = 12
            shwscr = scr
            displayg.blit(background, (0, 0))
            show_message('Game over!', red2, 280, 170, large_font)
            show_message('Score: {}'.format(str(shwscr)), black, dis_width / 2 - 90, dis_height / 2 - 100, big_font)
            show_message('Press R to play again or Q to quit.', black, dis_width / 2 - 320, dis_height / 2 - 10)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        direction = 'right'
                        scr = 0
                        gameLoop()
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

    pygame.quit()
    sys.exit()
 
if __name__ == '__main__':  
    gameLoop()
