class Flying(object):
    " 所有飞行物的父类 "
    def __init__(self,x,y,w,h,hp,image):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp= hp
        self.image = image