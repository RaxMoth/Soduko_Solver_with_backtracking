# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:
	
	# creating a loop to check events that
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		# checking if keydown event happened or not
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_0:
				print("Key 1 has been pressed")
			
			if event.key == pygame.K_1:
				print("Key 1 has been pressed")
			
			if event.key == pygame.K_2:
				print("Key 2 has been pressed")
				
			if event.key == pygame.K_3:
				print("Key 3 has been pressed")
