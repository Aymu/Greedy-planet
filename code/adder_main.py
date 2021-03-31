import flying
import config
import random

class Adder(flying.Flying):
    adder_count = 0
	
    def __init__(self,image):
        a = random.randint(0,5)
        Adder.adder_count += 1
        self.tag = "Adder_"+str(Adder.adder_count)
        x = 60 * a
        y = 0 
        w = image.width()
        h = image.height()
        hp= 4
        super().__init__(x,y,w,h,hp,image)
		
    def step(self, canvas):
        canvas.move(self.tag, 0, 4)
        self.y += 4
		
    def out_of_bounds(self):
        if self.y > config.GAME_HEIGHT:
            return True
        else:
            return False