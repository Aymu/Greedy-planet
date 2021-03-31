import config

 Block(flying.Flying):
	
    def step(self, canvas):
        canvas.move(self.tag, 0, 4)
        self.y += 4