import pygame
import random

pygame.init()

sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/xwing.png')
gameover = pygame.image.load('immagini/gameover.png')
tfighter = pygame.image.load('immagini/tieFighter.png')

SCHERMO = pygame.display.set_mode((480, 720))
FPS = 50
VEL_AVANZ = 6

class tieFighter:
    def __init__(self):
        self.x = random.choice([210, 60, 360])
        self.x2 = random.choice([210, 60, 360])
        self.y = -120
    def avanza_e_disegna(self):
        self.y += VEL_AVANZ
        SCHERMO.blit(tfighter, (self.x, self.y))
    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 10
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()


def inizializza():
    global uccellox, uccelloy, uccello_vely
    #global basex
    global tubi
    uccellox, uccelloy = 210, 540
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tieFighter())


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def hai_perso():
    SCHERMO.blit(gameover, (50,180))
    aggiorna()
    ricominciamo =  False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox, uccelloy))





inizializza()

while True:
    #basex -= VEL_AVANZ
    #if basex < -307: basex = 0

    #uccello_vely = 0
    #uccelloy += uccello_vely

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_LEFT):
            if uccellox != 60:
                uccellox += -150
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_RIGHT):
            if uccellox != 360:
                uccellox += 150
        if event.type == pygame.QUIT:
            pygame.quit()

    if tubi[-1].y > 140:
        tubi.append(tieFighter())
        tubi.append(tieFighter())
    #for t in tubi:
    #    t.collisione(uccello, uccellox, uccelloy)

    #if uccelloy > 390 or uccelloy < 0:
    #    hai_perso()

    # aggiornamento oggetti
    disegna_oggetti()
    aggiorna()
