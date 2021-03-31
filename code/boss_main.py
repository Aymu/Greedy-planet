import flying
import config
import random

class Boss(flying.Flying):
	
    def __init__(self,image):
        self.tag = "Block_"
        x = 0
        y = 0 
        w = image.width()
        h = image.height()
        hp= 80
        super().__init__(x,y,w,h,hp,image)
		
    def step(self, canvas):
        canvas.move(self.tag, 0, 1)
        self.y += 1
		
    def out_of_bounds(self):
        if self.y > config.GAME_HEIGHT:
            return True
        else:
            return False
