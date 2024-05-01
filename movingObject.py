from pygame import Vector2

class MovingObject:
    def __init__(self,x):
        self.pos = Vector2(x,0)
        self.hitbox = (0,0,0,0)

    def Update(self,movingSpeed,enemies):
        self.pos[0] -= movingSpeed
        if self.pos[0] < 0:
            for enemy in enemies:
                enemies.remove(enemy)