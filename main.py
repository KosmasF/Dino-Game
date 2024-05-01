import pygame
import sys
from bird import Bird
import random

pygame.init()
X,Y = 1920/2,1080/2
screen = pygame.display.set_mode((X,Y))
clock = pygame.Clock()
progress = 0
groundProgress = 0
walkingProgress= 0 
groundMovingSpeed = 10


dinoFrameStart = (1854 , 5)
dinoFrameMargin = (88 ,93)
walkingFrames = 2
dinoPos = (50,500-(dinoFrameMargin[1])+30)
groundDinoPos = dinoPos
velocity = pygame.Vector2(0,0)
dinoJumpStart = (1678,5)
dinoShiftStart = (2204,5)
dinoShiftMargin = (118 ,93)
shiftingFrames = 2
dinoRect = pygame.Rect(0,0,0,0)


spriteSheet = pygame.image.load("assets/sprite_sheet.png").convert_alpha()#https://getspritexy.netlify.app/


enemiesSpawnDistance = 100
enemiesSpawnProgress = enemiesSpawnDistance



enemies = []


font = pygame.font.Font(None, 64)





while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_SPACE or event.key == pygame.K_UP)and not dinoPos[1] < groundDinoPos[1]:
				velocity.y = -17


	screen.fill(0xffffff)


	#Ground
	screen.blit(spriteSheet,(-groundProgress*groundMovingSpeed,500),(0,100,2341,30))
	screen.blit(spriteSheet,((-groundProgress*groundMovingSpeed)+2340,500),(0,100,2441,30))
	if groundProgress*groundMovingSpeed > 2340:
		groundProgress = 0


	#Dino
	if walkingProgress >= walkingFrames:
		walkingProgress = 0

	dinoPos+=velocity

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LSHIFT] or keys[pygame.K_DOWN]:
		shifting = True
	else:
		shifting = False

	dinoRect.x = dinoPos[0]
	dinoRect.y = dinoPos[1]
	dinoRect.w = dinoFrameMargin[0]
	dinoRect.h = dinoFrameMargin[1]


	if dinoPos[1] < groundDinoPos[1]:
		velocity.y += 1
		if shifting:
			velocity.y += 1
		screen.blit(spriteSheet,dinoPos,(dinoJumpStart[0],dinoJumpStart[1],dinoFrameMargin[0],dinoFrameMargin[1]))
	else:
		velocity.y = 0
		dinoPos = groundDinoPos
		if shifting:
			screen.blit(spriteSheet,dinoPos,(dinoShiftStart[0]+(dinoShiftMargin[0]*int(walkingProgress)),dinoShiftStart[1],dinoShiftMargin[0],dinoShiftMargin[1]))
			dinoRect.y+=30
			dinoRect.h-=30
		else:
			screen.blit(spriteSheet,dinoPos,(dinoFrameStart[0]+(dinoFrameMargin[0]*int(walkingProgress)),dinoFrameStart[1],dinoFrameMargin[0],dinoFrameMargin[1]))




	#Bird
	for enemy in enemies:
		enemy.Update(groundMovingSpeed,enemies)
		enemy.Draw(screen,spriteSheet,walkingProgress)
		if dinoRect.colliderect(enemy.hitbox):
			raise InterruptedError("YOU LOST \n HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
		

	#Enemies
	if enemiesSpawnProgress <= 0:
		enemiesSpawnProgress = enemiesSpawnDistance
		enemies.append(Bird(random.randint(0,2),enemiesSpawnDistance*groundMovingSpeed))
	


	#Score
	text = font.render(f'HI {(progress//groundMovingSpeed):04d}  {(progress//groundMovingSpeed):04d}', False,0x000000)
	textRect:pygame.Rect = text.get_rect()
	textRect.topright = (X,0)
	screen.blit(text,textRect)


	#Cleanup
	pygame.draw.rect(screen,0x00ff00,dinoRect,1)



	progress+=1
	groundProgress+=1
	walkingProgress+=0.15
	enemiesSpawnProgress-=1
	pygame.display.update()
	clock.tick(60)