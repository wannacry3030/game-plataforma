import pygame
from pygame.locals import*
import sys

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
        self.rect = self.surf.get_rect(center = (10, 420))
        #criando variavels com 2 dimensões
        self.pos = vec((10,385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

#classe        
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((LARGURA, 20))
        self.surf.fill((255,0,0))#função
        self.rect = self.surf.get_rect(center = (LARGURA/2, ALTURA - 10))#get_rect é o metodo, center= é o parametro
        
#objetos= pt1: plataforma1, p1: player1       
PT1 = platform()
P1 = Player()

#GRUPO DE SPRITES E LOOP DO JOGO
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    displaysurface.fill((0,0,0))
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        
    pygame.display.update()
    FramePerSec.tick(FPS)
    
#IMPLEMENTANDO OS MOVIMENTOS, usando kinematics e equações de motion