import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones
ancho = 600
alto = 400

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Culebrita 🐍")

reloj = pygame.time.Clock()
tamaño_bloque = 20
velocidad = 15

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)

def mensaje(msg, color):
    texto = fuente.render(msg, True, color)
    pantalla.blit(texto, [ancho / 6, alto / 3])

def juego():
    game_over = False
    game_cerrado = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    cuerpo_culebra = []
    largo_culebra = 1

    comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20.0

    while not game_over:

        while game_cerrado:
            pantalla.fill(blanco)
            mensaje("Perdiste. Presiona C para continuar o Q para salir", rojo)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_bloque
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_bloque
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_cerrado = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])
        cabeza_culebra = []
        cabeza_culebra.append(x1)
        cabeza_culebra.append(y1)
        cuerpo_culebra.append(cabeza_culebra)

        if len(cuerpo_culebra) > largo_culebra:
            del cuerpo_culebra[0]

        for x in cuerpo_culebra[:-1]:
            if x == cabeza_culebra:
                game_cerrado = True

        for segmento in cuerpo_culebra:
            pygame.draw.rect(pantalla, negro, [segmento[0], segmento[1], tamaño_bloque, tamaño_bloque])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20.0
            largo_culebra += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

juego()
