import pygame

class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 50
        self.altura = 50
        self.velocidade = .33
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, janela):
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        pygame.draw.rect(janela, self.color, self.rect)

    def movimentar(self):
        self.y += self.velocidade