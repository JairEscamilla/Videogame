import pygame
import sys
import random

# CONSTANTES
# Dimensiones
ANCHO = 800
ALTO = 600
# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
# Jugador
jugador_size = 50
jugador_pos = [ANCHO / 2, ALTO - jugador_size*2]

# Enemigo
enemigo_size = 50
enemigo_pos = [random.randint(0, ANCHO - enemigo_size), 0]


# VENTANA
ventana = pygame.display.set_mode((ANCHO, ALTO))

game_over = False
clock = pygame.time.Clock()

# FUNCION QUE DETECTA COLISIONES	
def detectarColision(jugador_pos, enemigo_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	ex = enemigo_pos[0]
	ey = enemigo_pos[1]
	if (ex >= jx and ex < (jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
		if (ey >= jy and ey < (jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
			return True
	return False

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

	if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
		enemigo_pos[1] += 20
	else:
		enemigo_pos[0] = random.randint(0, ANCHO - enemigo_size)
		enemigo_pos[1] = 0
	
	# Colisiones
	if detectarColision(jugador_pos, enemigo_pos):
		game_over = True

	# Dibujar enemigo 
	pygame.draw.rect(ventana, AZUL, (enemigo_pos[0], enemigo_pos[1], enemigo_size, enemigo_size))

	# Dibujando cuadrado
	pygame.draw.rect(ventana, ROJO, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	clock.tick(30)
	pygame.display.update() 

