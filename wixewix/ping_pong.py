from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("Ping_pong")
clock = time.Clock()
FPS = 60
font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 36)
text_lose1 = font1.render("Player№1 LOSE!", True, (255, 200, 255))
text_lose2 = font2.render("Player№2 LOSE!", True, (255, 200, 255))
background = transform.scale(image.load("Без названия.jpg"),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(widht,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player1(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
gamer1 = Player1("stick.png", 0, 150, 5, 20, 100)
gamer2 = Player2("stick.png", 680, 150, 5, 20, 100)
ball = GameSprite("ball.png", 350, 250, 15, 25, 25)
game = True
finish = False
speed_x = 5
speed_y = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((0,0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > 475:
            speed_y *=- 1
        if sprite.collide_rect(ball, gamer1) or sprite.collide_rect(ball, gamer2):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            text_lose1 = font1.render("Player№1 LOSE!", True, (255, 200, 255))
            window.blit(text_lose1, (250, 230))
        if ball.rect.x >675:
            finish = True
            text_lose2 = font2.render("Player№2 LOSE!", True, (255, 200, 255))
            window.blit(text_lose2, (250, 230))
        
        gamer1.reset()
        gamer2.reset()
        gamer1.update1()
        gamer2.update2()
        ball.reset()
    display.update()
    clock.tick(FPS)