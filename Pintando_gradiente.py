import pygame
import sys

pygame.init()
largura, altura = 255, 255
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pintando em degradê")

def setPixel(superficie, x, y, cor):
    superficie.set_at((x,y), cor)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))
    
    for x in range(largura):
        for y in range(altura):
            setPixel(tela, x, y, (y+1,0,0))

    pygame.display.flip()

pygame.quit()
sys.exit()