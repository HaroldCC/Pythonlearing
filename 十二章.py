#12-1
'''
import sys

import pygame

def blue_screen():
	pygame.init()
	screen = pygame.display.set_mode((600,800))
	bg_color = (0,0,255)
	pygame.display.set_caption("蓝色背景")

	while True:
		screen.fill(bg_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		pygame.display.flip()

blue_screen()
'''
#12-2
import sys

import pygame

class Image():
	"""创建加载图片的类"""
	def __init__(self,screen):
		self.screen = screen

		self.image = pygame.image.load(r'C:\Users\19211\Desktop\python\.vscode\ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将飞船放在中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitem(self):
		self.screen.blit(self.image,self.rect)


def blue_screen():
	"""加载蓝色背景屏幕"""
	pygame.init()
	screen = pygame.display.set_mode((600,800))
	bg_color = (0,0,255)
	pygame.display.set_caption("蓝色背景")

	while True:
		screen.fill(bg_color)
		image = Image(screen)
		image.blitem()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		pygame.display.flip()

blue_screen()