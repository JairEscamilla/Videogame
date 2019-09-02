import pygame
import sys

# CONSTANTES
# Dimensiones
ANCHO = 800
ALTO = 600
# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
# Jugador
jugador_pos = [400, 400]
jugador_size = 50

# VENTANA
ventana = pygame.display.set_mode((ANCHO, ALTO))

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			if event.key == pygame.K_LEFT:
				x -= jugador_size
			if event.key == pygame.K_RIGHT:
				x += jugador_size
			jugador_pos[0] = x

	ventana.fill(NEGRO)

	# Dibujando cuadrado
	pygame.draw.rect(ventana, ROJO, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	pygame.display.update() 

