def load_image(tkinter):
    return \
        tkinter.PhotoImage(file="../image/background.gif")\
        , tkinter.PhotoImage(file="../image/bug.gif")\
        , tkinter.PhotoImage(file="../image/block.gif")\
        , tkinter.PhotoImage(file="../image/adder.gif")\
        , tkinter.PhotoImage(file="../image/boss.gif")\
        , tkinter.PhotoImage(file="../image/none.gif")
		
def load_state_image(tkinter):
    return tkinter.PhotoImage(file="../image/start.png")\
        , tkinter.PhotoImage(file="../image/gameover.png")