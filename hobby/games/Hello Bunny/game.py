#1
import pygame
from pygame.locals import *
#2
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100,100]
acc = [0,0]
boomerangs = []
#3
player = pygame.image.load("dude.png")
player = pygame.transform.scale(player, (150, 100))
boomerangs = pygame.image.load("boomerang.png")
boomerangs = pygame.transform.scale(boomerangs, (30,30))
#4
while 1:
	#5
	screen.fill(0)
	#6
	screen.blit(player, playerpos)
	#7
	pygame.display.flip()
	#8
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
		if keys[0]:
			playerpos[1] -= 5
		elif keys[2]:
			playerpos[1] += 5
		if keys[1]:
			playerpos[0] -= 5
		elif keys[3]:
			playerpos[0] += 5
		if event.type == pygame.MOUSEBUTTONDOWN:
			position = pygame.mouse.get_pos()
			acc[1] += 1
			boomerangs.append()