import pygame
import sys
import random
import time 

pygame.init()
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Polígono")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
cores = [RED, GREEN, BLUE]

def setPixel(superficie, x, y, cor):
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)

def scanline(superficie, pontos, cor_preenchimento):
    # Encontra Y mínimo e máximo
    ys = [p[1] for p in pontos]
    y_min = min(ys)
    y_max = max(ys)

    n = len(pontos)

    for y in range(y_min, y_max):
        intersecoes_x = []

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            # Ignora arestas horizontais
            if y0 == y1:
                continue

            # Garante y0 < y1
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0

            # Regra Ymin ≤ y < Ymax
            if y < y0 or y >= y1:
                continue

            # Calcula interseção
            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            intersecoes_x.append(x)

        # Ordena interseções
        intersecoes_x.sort()

        # Preenche entre pares
        for i in range(0, len(intersecoes_x), 2):
            if i + 1 < len(intersecoes_x):
                x_inicio = int(round(intersecoes_x[i]))
                x_fim = int(round(intersecoes_x[i + 1]))

                for x in range(x_inicio, x_fim + 1):
                    setPixel(superficie, x, y, cor_preenchimento)

def drawPolygon(vertices, color):
    n = len(vertices)
    for i in range(n):

        (x0, y0) = vertices[i]
        (x1, y1) = vertices[(i + 1) % n]
        pygame.draw.line(tela, color, (x0, y0), (x1, y1))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    num = 3
    vertices =[]
    for i in range(num):
        x= random.randint(1, largura-1)
        y= random.randint(1, altura-1)
        vertices.append((x,y))
    
    tela.fill((255,255,255))
    cor = random.choice(cores)

    drawPolygon(vertices, cor)
    scanline(tela, vertices, cor)
    
    pygame.display.flip()
    time.sleep(3)

pygame.quit()
sys.exit()