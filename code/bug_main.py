import flying

class Bug(flying.Flying):
    def __init__(self, image, x=150, y=450, hp=10):
        w = image.width()
        h = image.height()
        super().__init__(x,y,w,h,hp,image)
		
    def bomb(self, block,life):
        for x in range(life):
            if block.x - self.w <= self.x <= block.x + block.w:
                if block.y-self.h <= self.y <= block.y + block.h:
                    return True
            return False	