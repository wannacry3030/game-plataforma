import pygame
from pygame.locals import*
import sys
import random

#INICIANDO E CRIANDO AS CONSTANTES
pygame.init()

vec = pygame.math.Vector2 #definindo 2 dimensões
ALTURA = 450
LARGURA = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("JOGO")

#CLASSE JOGADOR E PLATAFORMA
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        #criando variavels com 2 dimensões
        self.pos = vec((10,385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    #função de movimento
    def move(self):
        self.acc = vec(0,0.5)
        
        pressed_keys = pygame.key.get_pressed()
  #IMPLEMENTANDO OS MOVIMENTOS, usando kinematics e equações de motion
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
    
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > LARGURA:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = LARGURA
            
        self.rect.midbottom = self.pos
        
    def update(self):
         hits = pygame.sprite.spritecollide(P1,platforms,False)
         if P1.vel.y > 0:        
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
        
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15       
    
#classe        
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((LARGURA, 20))
        self.surf.fill((255,0,0))#função
        self.rect = self.surf.get_rect(center = (LARGURA/2, ALTURA - 10))#get_rect é o metodo, center= é o parametro
    
    def move(self):
        pass

        
#objetos= pt1: plataforma1, p1: player1       
PT1 = platform()
P1 = Player()

#GRUPO DE SPRITES E LOOP DO JOGO
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platform.add(PT1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
            
    displaysurface.fill((0,0,0))
    P1.update()
    
    P1.move()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
        
    pygame.display.update()
    FramePerSec.tick(FPS)
    

