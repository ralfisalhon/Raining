import pygame
import time
from pygame.locals import *
from random import randint, randrange, uniform
from timeit import default_timer
pygame.init()

pygame.display.set_caption("Raining")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

dropletCount = 40 #Enter value between 20-70
Height = dropletCount*10
Width = Height
waitBetween = 1.0/dropletCount

screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

positions = []


def newDroplet():
	list = [randrange(0, Width), 0]
	positions.append(list)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()
	
	newDroplet()
	time.sleep(waitBetween)
	
	pygame.display.update()
	screen.blit(background,(0,0))
	
	for x in range(len(positions)):
		try:
			pygame.draw.rect(screen, darkBlue, (positions[x][0], positions[x][1], 5, 10), 0)
			positions[x][1] += 10
			if positions[x][1] > Height:
				positions.pop(x)
		except:
			pass
		pygame.display.set_caption("Droplet count = " + str(len(positions)-1))