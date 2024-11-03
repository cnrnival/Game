import pygame
from personagem import Cubo

#pip install pygame

LARGURA = 1000
ALTURA = 800
JANELA = pygame.display.set_mode([LARGURA, ALTURA])

jogando = True

cubo = Cubo(100, 100)

def gestao_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidade
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidade
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidade
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidade


while jogando:
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestao_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jogando = False

    JANELA.fill("black")
    cubo.desenhar(JANELA)
    pygame.display.update()

quit()
