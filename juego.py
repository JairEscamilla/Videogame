import pygame
import sys

# CONSTANTES
ANCHO = 800
ALTO = 600
ROJO = (255, 0, 0)

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

	# Dibujando cuadrado
	pygame.draw.rect(ventana, ROJO, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	pygame.display.update() 