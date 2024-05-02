from movingObject import MovingObject
from pygame import draw

class Bird(MovingObject):
    birdStart = (260 ,2)
    birdMargin = (92  ,80)
    birdFrames = 2


    def __init__(self,height,progress):
        super().__init__(progress)
        self.animationProgress = 0

        if height == 0:
            self.pos[1] = 300
        elif height == 1:
            self.pos[1] = 375
        elif height == 2:
            self.pos[1] = 440


    def Draw(self,screen,spriteSheet,animationProgress):
        self.animationProgress = animationProgress
        screen.blit(spriteSheet,(self.pos[0],self.pos[1]),(self.birdStart[0]+(self.birdMargin[0]*int(self.animationProgress)),self.birdStart[1],self.birdMargin[0],self.birdMargin[1]))

        self.hitbox = (self.pos[0],self.pos[1],self.birdMargin[0],self.birdMargin[1])

        draw.rect(screen,0xff0000,self.hitbox,1)
    