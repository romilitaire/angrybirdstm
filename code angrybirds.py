import pygame, sys
from pygame.locals import *
from classes import *

pymunk.pygame_util.positive_y_is_up = True

pygame.init()
NOIR = (0, 0, 0)
taille = 1200, 600

pygame.display.set_caption('Angry Birds Roro')
screen = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
jouer = True
lancer = False
background = pygame.image.load('background.png').convert_alpha()
pygame.mixer.music.load('angry-birds.ogg')
pygame.mixer.music.play(-1)
bird = pygame.image.load('bird.png').convert_alpha()
sling = pygame.image.load('sling.png').convert_alpha()
sling2 = pygame.image.load('sling2.png').convert_alpha()
bird_rect = Rect(160, 380, 64, 64)

p0 = (220, 420)  # extrémité 1
p2 = (173, 425)  # extrémité 2
t0 = 0
game = Game()

while jouer:
    for event in pygame.event.get():
        if event.type == QUIT:
            jouer = False
        if event.type == MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos):
                lancer = True
                
        if event.type == MOUSEMOTION:
            if lancer:
                bird_rect.move_ip(event.rel)
        
        if event.type == MOUSEBUTTONUP:
            lancer = False
            bird_rect = pygame.Rect(160, 380, 64, 64)
            #faut mettre 1000 ou pas, dans pdf y'a pas tt le temps
            t0 = pygame.time.get_ticks() + 1000
            game.launch_bird(p0, p1)
            
        game.do_event(event)
                    

    pygame.display.flip()
    clock.tick(30)
    
    # --- code pour dessiner ---
    screen.blit(background, (0, 0))
    screen.blit(sling, (200, 390))
    p1 = bird_rect.move(10, 40).topleft
    pygame.draw.line(screen, NOIR, p1, p0, 6)
    
    t = pygame.time.get_ticks()
    if t > t0:
        screen.blit(bird, bird_rect)
        
    pygame.draw.line(screen, NOIR, p1, p2, 6)
    screen.blit(sling2, (170, 390))
    game.draw()


pygame.quit()
sys.exit

