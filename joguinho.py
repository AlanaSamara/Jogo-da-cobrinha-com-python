import pygame
from random import randint  

pygame.init()

x = 320
y = 280
bloco = 40
x_maca = 0
y_maca = 0
verde = (0,255,0)
cinza = (150,150,150)
vermelho = (255,0,0)
maca_eaten = True
walk = "right"
pontos=0

# texto para pontuação
font = pygame.font.SysFont('ariel black', 25)
texto = font.render("pontos: "+str(pontos), True, (0,0,0),(211,211,211))
pos_texto = texto.get_rect()
pos_texto.center = (50,50)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Joguinho")

janela_aberta = True
while janela_aberta:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # mudar o sentido da cobrinha pelas teclas
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and y >= 40:
        walk = "up"
    if comandos[pygame.K_DOWN] and y <= 520:
        walk = "down"
    if comandos[pygame.K_LEFT] and x >= 40:
        walk = "left"
    if comandos[pygame.K_RIGHT] and x <= 720:
        walk = "right"
    janela.fill(cinza)
    
    pygame.time.delay(200)
    # Sistema para manter a "cobrinha" andando na direção da cabeça dela
    if walk == "up" and y >= 40:
        y-= bloco
    if walk == "down" and y <= 520:
        y+= bloco
    if walk == "left" and x >= 40:
        x-= bloco
    if walk == "right" and x <= 720:
        x+= bloco

    # pontuação para quando se comer a maça
    if x == x_maca and y == y_maca:
        maca_eaten = True
        pontos+=1
        texto = font.render("pontos: "+str(pontos), True, (0,0,0),(211,211,211))
   
   # gerar uma nova coordenada para a maça
    if maca_eaten == True:

        # máx 20 blocos eixo x, 15 blocos eixo y
        x_maca = randint(0,19)*40
        y_maca = randint(0,14)*40

        maca_eaten = False
    
    pygame.draw.rect(janela, verde, (x, y, 40, 40))
    pygame.draw.rect(janela, vermelho, (x_maca, y_maca, 40, 40))
    janela.blit(texto,pos_texto)
    pygame.display.update()

pygame.quit()