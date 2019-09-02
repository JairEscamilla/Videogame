import pygame
import sys

ventana = pygame.display.set_mode((800, 600))

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			sys.exit()

	# Dibujando cuadrado
	pygame.draw.rect(ventana, (255, 0, 0), (400, 400, 50, 50))
	pygame.display.update() 