from pygame import Vector2,draw
from movingObject import MovingObject
from random import randint

class Cactus(MovingObject):
    smallCactusStart = (446,2)
    smallCactusMargin = (34,70)


    def __init__(self,progress,size,y):
        super().__init__(progress)
        if size == "small":
            self.smallCactusSpriteNum = randint(0,5)

            self.pos[1] = y-self.smallCactusMargin[1]

    def Draw(self,screen,spriteSheet,animationProgress):

        screen.blit(spriteSheet,(self.pos[0],self.pos[1]),(self.smallCactusStart[0]+(self.smallCactusMargin[0]*int(self.smallCactusSpriteNum)),self.smallCactusStart[1],self.smallCactusMargin[0],self.smallCactusMargin[1]))




        self.hitbox = (self.pos[0],self.pos[1],self.smallCactusMargin[0],self.smallCactusMargin[1])

        draw.rect(screen,0x0000ff,self.hitbox,1)



