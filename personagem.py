import pygame

class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 50
        self.altura = 50
        self.velocidade = 5
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, janela):
        pygame.draw.rect(janela, self.color, self.rect)