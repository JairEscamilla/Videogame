import pygame
import sys
import random



class Videojuego():
	# CONSTANTES
	# Dimensiones
	ANCHO = 600
	ALTO = 600
	# Colores
	AZUL = (0, 0, 0)
	NEGRO = (255, 255, 255)
	ROJO = (100, 100, 100)
	def __init__(self):
		# Jugador
		self.jugador_size = 60
		self.jugador_pos = [30, 510]
		self.game_over = False

		# VENTANA
		self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))

		# Cargando la imagen
		self.imagen = pygame.image.load("tablero.png")
		self.imagen = self.imagen.convert()
		self.ventana.blit(self.imagen, (0, 0))
		pygame.display.flip()
	# FUNCION QUE DETECTA COLISIONES
	def detectarColision(self, jugador_pos, enemigo_pos):
		jx = jugador_pos[0]
		jy = jugador_pos[1]


	def startGame(self):
		while not self.game_over:
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
						
					self.jugador_pos[0] = x
					self.jself.ugador_pos[1] = y

			self.ventana.blit(self.imagen, (0, 0))

			# Dibujando cuadrado
			pygame.draw.rect(self.ventana, self.ROJO, (self.jugador_pos[0], self.jugador_pos[1], self.jugador_size, self.jugador_size))
			pygame.display.update()

if __name__ == '__main__':
	game = Videojuego()
	game.startGame()