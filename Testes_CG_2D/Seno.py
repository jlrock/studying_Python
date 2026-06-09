import pygame 
import sys
import math

pygame.init()
largura, altura = 400, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Seno")

def setPixel(superficie, x, y, cor):
    superficie.set_at((x, y), cor)

def desenhar_seno(superficie, cor):
    amplitude = altura // 4
    centro_y = altura // 2
    frequencia = 2*math.pi / largura
    
    for x in range(largura):
        y = centro_y - int(math.sin(x*frequencia)*amplitude)
        
        setPixel(superficie, x, y, (0, 0, 0))
  
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    tela.fill((255, 255, 255))
    desenhar_seno(tela, (0, 0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()