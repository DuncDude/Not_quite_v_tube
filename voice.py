#!/usr/bin/env python3
import numpy as np
import sounddevice as sd
import pygame
import sys

DURATION = 10 #in seconds
RADIUS =15
AVATAR = pygame.image.load('hair.png')
SPEECH_THRESHOLD = 30

SCREEN_HEIGHT = 254
SCREEN_WIDTH = 254
MOUTH_X = 110
MOUTH_Y = 120
MOUTH_WIDTH = 40

#pygame options
pygame.display.set_caption("N0t quite v-tubing")
pygame.display.set_icon(AVATAR)

def game():
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])

	running = True
	while running:
		print('Running, USE CTR + C TO QUIT')
		print('	 ⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀')
		print('⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷')
		print('⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇')
		print('⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇')
		print('⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇')
		print('⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼')
		print('⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀')
		print('⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
		print('⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀')
		print('⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀')
		print('⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀')
		print('⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀')
		def audio_callback(indata, frames, time, status):
			screen.fill((255, 255, 255))
			screen.blit(AVATAR, [0, 0])
			volume_norm = np.linalg.norm(indata) * 10
			if volume_norm > SPEECH_THRESHOLD:
				print('somebody spoke')
				RADIUS = 20
			else:
				RADIUS = 10
			pygame.draw.rect(screen, (0, 0, 0), (MOUTH_X, MOUTH_Y, MOUTH_WIDTH, RADIUS), 0)
	    	# Flip the display
			pygame.display.flip()

		stream = sd.InputStream(callback=audio_callback)
		with stream:
			sd.sleep(DURATION * 8000)
	
game()


