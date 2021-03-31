import config
import tkinter
import random
import time
import block_main
import bug_main
import adder_main
import boss_main
import image

blocks 	= [] 	#阻碍行星的集合
adders	= [] 	#加分星球的集合
bosses	= []
life 	= 0		#生命值
score 	= 0  	#得分
count 	= 0		#计数值
hp_count= 0

game_state	= config.GAME_START
game_window	= tkinter.Tk()		#窗体创建	
game_window.title("贪吃星球")
screenwidth = game_window.winfo_screenwidth()
screenheight = game_window.winfo_screenheight()
size = '%dx%d+%d+%d' % (config.GAME_WIDTH, config.GAME_HEIGHT, (screenwidth-config.GAME_WIDTH)/2, 20)
game_window.geometry(size)
back, bug_image, block_image, adder_image, boss_image, none= image.load_image(tkinter)	#相关图片素材载入
start_image,stop_image = image.load_state_image(tkinter)				#相关图片素材载入
window_canvas = tkinter.Canvas(game_window)
window_canvas.pack(expand=tkinter.YES,fill=tkinter.BOTH)

#生成新的行星，放入集合中
def new_block(a,b,c):
	block = ""
	block = block_main.Block(a,b,c)
	a += 1
	return block

#生成新的加分项，放入集合中
def new_adder():
	adder = ""
	adder = adder_main.Adder(adder_image)
	return adder

#生成最终boss
def new_boss():
	boss = ""
	boss = boss_main.Boss(boss_image)
	return boss

#阻碍物和加分项入场	
def enter_action():
	global count
	#global hp_count
	count += 1
	#hp_count += 1
	if count%60 == 0:
		a = 0
		for x in range(5):
			b = random.randint(1,5)
			if b <= 2:
				block = new_block(a,0,none)
				blocks.append(block)
				window_canvas.create_image(block.x,block.y,anchor = tkinter.NW,image=block.image,tag=block.tag)
				a += 1
			else :
				c = random.randint(1,7)  	#生命值
				block = new_block(a,c,block_image)
				blocks.append(block)
				window_canvas.create_image(block.x,block.y,anchor = tkinter.NW,image=block.image,tag=block.tag)
				window_canvas.create_text(block.x+30,block.y+17,text="%d"%(block.hp),anchor=tkinter.NW,fill="white",font="time 18 bold",tag="BLOCK_HP")
				a += 1
	elif count%30 == 0:
		adder = new_adder()
		adders.append(adder)
		window_canvas.create_image(adder.x,adder.y,anchor = tkinter.NW,image=adder.image,tag=adder.tag)
	elif count == 5000:
		boss = new_boss()
		bosses.append(boss)
		window_canvas.create_image(boss.x,boss.y,anchor = tkinter.NW,image=boss.image,tag=boss.tag)

#阻碍物和加分项的运动方式和速度
def step_action():
	for block in blocks:
		block.step(window_canvas)
	window_canvas.move("BLOCK_HP", 0, 4)
	for adder in adders:
		adder.step(window_canvas)
	for boss in bosses:
		boss.step(window_canvas)

#判定出界移除
def out_of_bounds_action():
	for block in blocks:
		if block.out_of_bounds():
			window_canvas.delete(block.tag)
			#window_canvas.delete("BLOCK_HP")
			blocks.remove(block)
	for adder in adders:
		if adder.out_of_bounds():
			window_canvas.delete(adder.tag)
			#window_canvas.delete("ADDER_HP")
			adders.remove(adder)
	for boss in bosses:
		if boss.out_of_bounds():
			window_canvas.delete(boss.tag)
			bosses.remove(boss)

#碰撞判定
def bmob_action():
	global life
	global score
	for block in blocks:
		for x in range(block.hp):
			if bug.bomb(block,life):
				life -= 1
				block.hp -= 1
				score += 1
				if block.hp == 0:
					blocks.remove(block)
					window_canvas.delete(block.tag)
					#window_canvas.delete("BLOCK_HP")
				if life == 0:
					global game_state
					game_state = config.GAME_STOP
					game_over()
	for adder in adders:
		for x in range(adder.hp):
			if bug.bomb(adder,life):
				life += 1
				adder.hp -= 1
				if adder.hp == 0:
					adders.remove(adder)
					window_canvas.delete(adder.tag)
	for boss in bosses:
		for x in range(boss.hp):
			if bug.bomb(boss,life):
				life -= 1
				boss.hp -= 1
				if boss.hp == 0:
					bosses.remove(boss)
					window_canvas.delete(boss.tag)
				if life == 0:
					game_state = config.GAME_STOP
					game_over()
	
#鼠标操作	
def call_back_click(event):
	global game_state
	if game_state == config.GAME_START:
		game_state = config.GAME_RUNNING
		window_canvas.create_text(10, 10, text="分数：%d" % (score), anchor=tkinter.NW, 
		                          fill="blue", font="time 24 bold",tag="SCORE")
		window_canvas.create_text(10, 50, text="生命：%d" % (life), anchor=tkinter.NW, 
		                          fill="red", font="time 24 bold",tag="LIFE")
		window_canvas.delete('START')
	elif game_state == config.GAME_STOP:
		window_canvas.delete("BACK")
		window_canvas.delete("BUG")
		window_canvas.delete("STOP")
		game_state = config.GAME_START
		game_start()

#鼠标操作		
def call_back_move(event):
	if game_state == config.GAME_RUNNING:
		old_x = bug.x
		old_y = bug.y
		bug.x = event.x - bug.w/2
		bug.y = event.y - bug.h/2
		if bug.y <= 500:
			bug.y = 500
		window_canvas.move("BUG", bug.x-old_x, bug.y-old_y)
		
#起始状态		
def draw_action():
    window_canvas.delete("SCORE")
    window_canvas.delete("LIFE")
    window_canvas.create_text(190,10,text="%d"%(score),anchor=tkinter.NW,fill="blue",font="time 24 bold",tag="SCORE")
    window_canvas.create_text(10,600,text="生命：%d"%(life),anchor=tkinter.NW,fill="red",font="time 24 bold",tag="LIFE")

#游戏失败的判定
def game_over():
	global game_state
	game_state = config.GAME_STOP
	for block in blocks:
		window_canvas.delete(block.tag)
		window_canvas.delete("BLOCK_HP")
	for adder in adders:
		window_canvas.delete(adder.tag)
	for boss in bosses:
		window_canvas.delete(boss.tag)
	blocks.clear()
	adders.clear()
	bosses.clear()
	window_canvas.create_image(0,0,anchor=tkinter.NW,image=stop_image,tag="STOP")

#游戏开始	
def game_start():
	global life
	global score
	score 	= 0
	window_canvas.create_image(0,0,anchor=tkinter.NW,image=back,tag="BACK")
	global bug
	bug 	= bug_main.Bug(bug_image,10)
	life 	= bug.hp
	window_canvas.create_image(bug.x,bug.y,anchor=tkinter.NW,image=bug.image,tag="BUG")
	window_canvas.create_image(0,0,anchor=tkinter.NW,image=start_image,tag="START")

#游戏主体
def game():
	global count
	if game_state == config.GAME_START:
		game_start()
		window_canvas.bind("<Motion>",call_back_move)
		window_canvas.bind("<Button-1>",call_back_click)
	while True:
		if game_state == config.GAME_RUNNING:
			enter_action()
			step_action()
			out_of_bounds_action()
			bmob_action()
			if life >= 0:
				draw_action()
		game_window.update()
		if 1800 >= count >= 600:
			time.sleep(0.005)
		elif count > 1800:
			time.sleep(0.003)
		else :
			time.sleep(0.01)
		
if __name__ == "__main__":
	game()
	game_window.mainloop()