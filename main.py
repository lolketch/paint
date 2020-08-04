import sys 
import pygame
from pygame.constants import *

class Painting():
	def __init__(self):
		"""Создание окна и холста для рисования"""
		self.window = pygame.display.set_mode((600,600))
		self.canvas = pygame.Surface((600,600))
		self.canvas.fill((255,255,255))
		self.x=None 
		self.y=None
		self.draw = False

	def get_x_y(self):
		self.x, self.y = pygame.mouse.get_pos()

	def drawing(self):
		if self.draw:
			pygame.draw.circle(self.canvas,
								(0,0,0),
								(self.x, self.y),
								10)

	def events(self):
		"""Обработка событий"""
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				self.draw = True
			if event.type == MOUSEBUTTONUP:
				self.draw = False

	def run(self):
		while True:
			self.get_x_y()
			self.drawing()
			self.events()
			self.window.blit(self.canvas,(0,0))
			pygame.display.flip()
def main():
	painting_class = Painting()
	painting_class.run()

main()