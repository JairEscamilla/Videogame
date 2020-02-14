import pygame
import sys
import random

# CONSTANTES
# Dimensiones
ANCHO = 300
ALTO = 600
# Colores
AZUL = (0, 0, 0)
NEGRO = (255, 255, 255)
ROJO = (100, 100, 100)
# Jugador
jugador_size = 50
jugador_pos = [ANCHO / 2, ALTO - jugador_size*2]

# Enemigo
enemigo_size = 50
enemigo_pos = [random.randint(0, 5)*50, 0]


# VENTANA
ventana = pygame.display.set_mode((ANCHO, ALTO))
# PUNTAJE
puntos = 1

game_over = False
clock = pygame.time.Clock()
# Cargando la imagen
imagen = pygame.image.load("fondo.png")
imagen = imagen.convert()
ventana.blit(imagen, (0, 0))
pygame.display.flip()
pygame.key.set_repeat(17)
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
counter = 0.015
dificultad = 200
while not game_over:
	puntos = puntos + (dificultad)/100
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			if event.key == pygame.K_LEFT:
				if(x >= jugador_size):
					x -= jugador_size
			if event.key == pygame.K_RIGHT:
				if(x < ANCHO - 50):
					x += jugador_size
			jugador_pos[0] = x

	ventana.blit(imagen, (0, 0))
	if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
		enemigo_pos[1] += counter * dificultad
	else:
		enemigo_pos[0] = random.randint(0, 5) * 50
		enemigo_pos[1] = 0

	# Colisiones
	if detectarColision(jugador_pos, enemigo_pos):
		game_over = True

	# Dibujar enemigo
	pygame.draw.rect(ventana, AZUL, (enemigo_pos[0], enemigo_pos[1], enemigo_size, enemigo_size))
	dificultad = dificultad + 1
	# Dibujando cuadrado
	pygame.draw.rect(ventana, ROJO, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	clock.tick(60)
	pygame.display.update()
print(int(puntos))
