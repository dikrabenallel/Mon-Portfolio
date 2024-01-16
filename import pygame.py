import pygame
import random 

pygame.init()

#set up display
screen_width = 800
screen_height = 600
screen = pygame.display.
set_model((screen_width,
screen_height))

pygame.display.set_caption
("Plane Fighting Game")

clock = pygame.time.Clock()

player_image = pygame.image.
load("player_plane.png")
enemy_image = pygame.image.
load("enemy_plane.png")
bullet_image.fill((255, 0, 0))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =
        player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20
        self.speed = 5
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.defeated = False

    def update(self):
        if self.defeated:
            return
        

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:

            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.x = max(0,min(self.rect.x,screen_width - self.rect.width))
