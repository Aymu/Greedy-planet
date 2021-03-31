import flying
import config
import random

class Block(flying.Flying):
    block_count = 0
	
    def __init__(self,a,b,image):
        Block.block_count += 1
        self.tag = "Block_"+str(Block.block_count)
        x = 80 * a
        y = 0 
        w = image.width()
        h = image.height()
        hp= b
        super().__init__(x,y,w,h,hp,image)
		
    def step(self, canvas):
        canvas.move(self.tag, 0, 4)
        self.y += 4
		
    def out_of_bounds(self):
        if self.y > config.GAME_HEIGHT:
            return True
        else:
            return False