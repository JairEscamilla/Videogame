import pygame
import sys
import random

# CONSTANTES
# Dimensiones
ANCHO = 600
ALTO = 600
# Colores
AZUL = (0, 0, 0)
NEGRO = (255, 255, 255)
ROJO = (100, 100, 100)
# Jugador
jugador_size = 60
jugador_pos = [30, 510]


# VENTANA
ventana = pygame.display.set_mode((ANCHO, ALTO))


game_over = False
# Cargando la imagen
imagen = pygame.image.load("tablero.png")
imagen = imagen.convert()
ventana.blit(imagen, (0, 0))
pygame.display.flip()
# FUNCION QUE DETECTA COLISIONES
def detectarColision(jugador_pos, enemigo_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]

counter = 0.015
dificultad = 200
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			y = jugador_pos[1]
			if event.key == pygame.K_LEFT:
				if(x >= jugador_size):
					x -= jugador_size * 2
			if event.key == pygame.K_RIGHT:
				if(x < ANCHO - 100):
					x += jugador_size * 2
			if event.key == pygame.K_UP and y > 30:
				y -= jugador_size * 2
			if event.key == pygame.K_DOWN and y < 510:
				y += jugador_size * 2
				
			jugador_pos[0] = x
			jugador_pos[1] = y

	ventana.blit(imagen, (0, 0))

	# Dibujando cuadrado
	pygame.draw.rect(ventana, ROJO, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	pygame.display.update()
print(int(puntos))
