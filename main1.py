import pygame
import math
import time

pygame.init()

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
    
myfont = pygame.font.SysFont('Comic Sans MS', 70)
myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
myfont2 = pygame.font.SysFont('Comic Sans MS', 85)
def read():
    f = open("test.txt", "r")
    writegold = f.read()
    return writegold
    
def add_gold(writegold,minus,gold):
    writegold = float(str(writegold))
    writegold = int(float(writegold))
    writegold += gold - minus
    return writegold
    
def write(writegold):
    f = open("test.txt", "w")
    f.write(str(writegold))
    f.close()
    return writegold

4

def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True
    
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

WIDTH,HEIGHT = 800,800

window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player_1:
    def __init__(self,x,y,width,height,speed,mode):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.mode = mode
    def draw(self,window):
        pygame.draw.rect(window,pygame.Color(255,255,255),pygame.Rect(self.x, self.y, self.width,self.height))
    def move(self,keys,ball_y):
        if self.mode == 0:
            if self.y >= 0:
                if keys[pygame.K_w]:
                    self.y -= self.speed
                    
            if self.y <= 675:
                if keys[pygame.K_s]:
                    self.y += self.speed
                
        if self.mode == 1:
            
            if self.y >= 0:
                if keys[pygame.K_UP]:
                    self.y -= self.speed
                
            if self.y <= 675:
                if keys[pygame.K_DOWN]:
                    self.y += self.speed
        if self.mode == 2:
            if self.y <= 675:
                if ball_y > self.y + self.height / 2:
                    self.y += self.speed
                
            if self.y >= 0:
                if ball_y < self.y + self.height / 2:
                    self.y -= self.speed
            
            
p1 = Player_1(75,337.5,25,125,0.2,0)

bot = Player_1(725,337.5,25,125,0.2,2)

p2 = Player_1(725,337.5,25,125,0.2,1)

class Button:
    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.my_font = pygame.font.SysFont('Comic Sans MS', 70)
        self.my_font1 = pygame.font.SysFont('Comic Sans MS', 20)
    def draw(self,window,player,myfont1):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        
        text_surface1 = myfont1.render(self.text, True, (255,0,0))
        window.blit(text_surface1, (self.x + 20,self.y + self.height / 2 - 50))

class Ball:
    def __init__(self,x,y,speed,size,dx,dy):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.dx = dx
        self.dy = dy
        
    def draw(self,window):
        pygame.draw.circle(window,pygame.Color("White"),(self.x,self.y),self.size)

    def move(self,p1_score,p2_score,times,player1_x,player2_x,player1_y,player2_y):
        if self.y  <= 15:
            self.dy *= -1
            
        if self.y  >= 785:
            self.dy *= -1
            
        if self.x  >= 785:
            p1_score += 1
            times = 3000
            self.x = 400
            self.y = 400
            player1_x = 75
            player1_y = 337.5
            player2_x = 725
            player2_y = 337.5
            self.dx = 1
            self.dy = -0.5
            
        if self.x  <= 15:
            p2_score += 1
            times = 3000
            self.x = 400
            self.y = 400
            player1_x = 75
            player1_y = 337.5
            player2_x = 725
            player2_y = 337.5
            self.dx = -1
            self.dy = -0.5
            
        if times <= -1:
            self.x += (self.speed * self.dx)
            self.y += (self.speed * self.dy)
        return [times,p1_score,p2_score]


        



ball = Ball(400,400,0.3,15,-1,-0.5)



button = Button(200,300,250,150, "Play")

play_bot = Button(200,550,350,150,"Play bot")

predx = 0
predy = 0
times = 0
main_menu = 1
play_againts_bot = 0
game = 0
was_holding = False
p1_score = 0
p2_score = 0
re = 0
er = 0

while True:
    if main_menu != 1:
        window.fill("Black")
    if main_menu == 1:
        window.fill("White")
    keys = pygame.key.get_pressed()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()   
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    if main_menu == 1:
        text_surface1 = myfont.render("Main menu", True, (255,0,0))
        window.blit(text_surface1, (button.x + button.width / 2 - 135,button.y + button.height / 2 - 325))
        button.draw(window,p1,myfont2)
        play_bot.draw(window,p1,myfont2)
        
        if button_colision(button.width,button.height,button.x,button.y,mousePos,mouseState):
            game = 1
            main_menu = 0
            play_againts_bot = 0
            
        if button_colision(play_bot.width,play_bot.height,play_bot.x,play_bot.y,mousePos,mouseState):
            game = 0
            main_menu = 0
            play_againts_bot = 1
            
    if play_againts_bot == 1:
        text_surface11 = myfont.render(f"{int(p1_score)}", True, (255,255,255))
        window.blit(text_surface11, (150,100))
        text_surface111 = myfont.render(f"{int(p2_score)}", True, (255,255,255))
        window.blit(text_surface111, (550,100))
        
        ball_rect = pygame.Rect(ball.x - ball.size, ball.y - ball.size, ball.size * 2,ball.size * 2)
        
        p1_rect = pygame.Rect(p1.x, p1.y, p1.width,p1.height)
        
        p2_rect = pygame.Rect(p2.x, p2.y, p2.width,p2.height)
        
        bot_rect = pygame.Rect(bot.x,bot.y,bot.width,bot.height)
        
        times = times - 1
        bot.draw(window)
        p1.move(keys,ball.y)
        times,p1_score,p2_score = ball.move(p1_score,p2_score,times,p1.x,p2.x,p1.y,p2.y)
        
        bot.move(keys,ball.y)
        ball.draw(window)
        p1.draw(window)
        
        if re <= 0:
            if colision1(ball_rect,p1_rect):
                ball.dx *= -1
                re = 150
        
        if er <= 0:
            if colision1(ball_rect,bot_rect):
                er = 150
                ball.dx *= -1
        
    if game == 1:
        text_surface11 = myfont.render(f"{int(p1_score)}", True, (255,255,255))
        window.blit(text_surface11, (150,100))
        text_surface111 = myfont.render(f"{int(p2_score)}", True, (255,255,255))
        window.blit(text_surface111, (550,100))
        times = times - 1
        p2.move(keys,ball.y)
        p1.move(keys,ball.y)
        times,p1_score,p2_score = ball.move(p1_score,p2_score,times,p1.x,p2.x,p1.y,p2.y)
        
        ball.draw(window)
        p1.draw(window)
        p2.draw(window)

        ball_rect = pygame.Rect(ball.x - ball.size, ball.y - ball.size, ball.size * 2,ball.size * 2)
        
        p1_rect = pygame.Rect(p1.x, p1.y, p1.width,p1.height)
        
        p2_rect = pygame.Rect(p2.x, p2.y, p2.width,p2.height)
        
        if colision1(ball_rect,p1_rect):
            ball.dx *= -1
        
            
        if colision1(ball_rect,p2_rect):
            ball.dx *= -1
        
            
    if keys[pygame.K_ESCAPE]:
        if main_menu == 0:
            game = 0
            main_menu = 1
            was_holding = True
            p1_score = 0
            p2_score = 0
    if keys[pygame.K_ESCAPE]:
        if main_menu == 1:
            if was_holding == False:
                exit()
    else:
        was_holding = False
    er -= 1
    re -= 1
    pygame.display.update()