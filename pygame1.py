import pygame
from personagem import Cubo

#pip install pygame

LARGURA = 1000
ALTURA = 800
JANELA = pygame.display.set_mode([LARGURA, ALTURA])

jogando = True

cubo = Cubo(100, 100)

while jogando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jogando = False

    cubo.desenhar(JANELA)
    pygame.display.update()

quit()
