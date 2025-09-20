from tkinter import *
from tkinter import messagebox
import random
#==Props=====================================================================================================================================
mainwin = Tk()
mainwin.geometry('550x550+400+80')
mainwin.config(bg= "#10153D")
mainwin.title('COLOR GAME™')

is_dark_mode = True
bg_dark = "#10153D"
bg_light = "#F0F0F0"
fg_dark = "#FFFF00"
fg_light = "#000000"
mainwin.config(bg=bg_dark)

#==Functions=================================================================================================================================
colors = ['Black','Gray','White','Gold','Silver','Blue','Red','Green','Yellow','Purple','Pink','Brown','Orange','Turquoise','Teal']
#============================================================================================================================================
score = 0

timeleft = 30
#____start_game______________________________________________________________________________________________________________________________
def startgame(event):
    global timeleft, score
    if timeleft == 30:
        score = 0
        lbl_score.config(text=f"Score: {score}")
        countdown()
    nextcolor()

def nextcolor():
    global score, timeleft
    if timeleft > 0:
        if eg.get().lower() == lbl_color.cget("text").lower():
            score += 1
        eg.delete(0, END)
        random.shuffle(colors)
        lbl_color.config(fg=colors[1], text=colors[0])
        lbl_score.config(text=f"Score: {score}")

def countdown():
    global timeleft, score
    if timeleft == 0:
        messagebox.showinfo('Times Up!', f"Your Score: {score}")
        timeleft = 30
        score = 0
        lbl_Timer.config(text=f'Time Left: {timeleft}')
        lbl_score.config(text=f'Score: {score}')
        lbl_color.config(text='')
        eg.delete(0, END)
        return
    timeleft -= 1
    lbl_Timer.config(text=f"Timer: {timeleft}")
    lbl_Timer.after(1000, countdown)


mainwin.bind('<Return>',startgame)
#__toggle_mode_______________________________________________________________________________________________________________________________
def toggle_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    bg = bg_dark if is_dark_mode else bg_light
    fg = fg_dark if is_dark_mode else fg_light
    btn_mode.config(text= '🌙',bg= bg_dark,fg= fg_dark) if is_dark_mode else btn_mode.config(text= '☀',bg= bg_light,fg= fg_dark)
    mainwin.config(bg=bg)
    for widget in mainwin.winfo_children():
        if isinstance(widget, Label) or isinstance(widget, Button):
            widget.config(bg=bg, fg=fg)
#==widgets===================================================================================================================================
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
#__labels______________________++____________________________________________________________________________________________________________
lbl_text = Label(text= 'Welcome to the ',font= ("G2 Rubber Stamp LET",18,'bold'),bg= bg_dark,fg= fg_dark )
lbl_text.place(x= 35,y= 15)

lbl_C = Label(text= 'C',font= ("Impact",24,'bold'),bg= bg_dark,fg= "#FF0000" )
lbl_C.place(x= 272,y= 5)

lbl_O = Label(text= 'O',font= ("Impact",24,'bold'),bg= bg_dark,fg= fg_dark )
lbl_O.place(x= 296,y= 10)

lbl_L = Label(text= 'L',font= ("Impact",24,'bold'),bg= bg_dark,fg= "#00FF00" )
lbl_L.place(x= 318,y= 5)

lbl_O2 = Label(text= 'O',font= ("Impact",24,'bold'),bg= bg_dark,fg= '#FF9900' )
lbl_O2.place(x= 336,y= 10)

lbl_R = Label(text= 'R',font= ("Impact",24,'bold'),bg= bg_dark,fg= '#FF00FF' )
lbl_R.place(x= 358,y= 5)

lbl_G = Label(text= 'G',font= ("Impact",24,'bold'),bg= bg_dark,fg= "#FF0000" )
lbl_G.place(x= 393,y= 5)

lbl_A = Label(text= 'A',font= ("Impact",24,'bold'),bg= bg_dark,fg= fg_dark )
lbl_A.place(x= 417,y= 10)

lbl_M = Label(text= 'M',font= ("Impact",24,'bold'),bg= bg_dark,fg= '#0000FF' )
lbl_M.place(x= 441,y= 5)

lbl_E = Label(text= 'E',font= ("Impact",26,'bold'),bg= bg_dark,fg= "#00FF00" )
lbl_E.place(x= 474,y= 10)

lbl_Guide = Label(text= "(Press 'Enter' To Play Game) ",font= ("G2 Rubber Stamp LET",12,'bold'),bg= bg_dark,fg= '#FF0000' )
lbl_Guide.place(x= 125,y= 56)

lbl_Timer = Label(text= "Timer: ",font= ("G2 Rubber Stamp LET",18,'bold'),bg= bg_dark,fg= fg_dark )
lbl_Timer.place(x= 130,y= 85)

lbl_score = Label(text= 'Score: ',font= ("G2 Rubber Stamp LET", 18,'bold'),bg= bg_dark,fg= fg_dark)
lbl_score.place(x= 310,y= 85)

lbl_color = Label(mainwin,font= ('comic sans ms', 50,'bold'),bg= bg_dark)
lbl_color.place(x= 150,y= 180)
#__Entry_____________________________________________________________________________________________________________________________________
# Ent_Game = eg
eg = Entry(mainwin,font= ('Cascadia Mono SemiBold',14,'bold'),fg= bg_dark)
eg.place(x= 130 ,y= 360,width= 300)
#__Button____________________________________________________________________________________________________________________________________
btn_mode = Button(mainwin,text= "🌙",font= ("G2 Rubber Stamp LET", 18,'bold'),bg= bg_dark,fg= fg_dark, command=toggle_mode)
btn_mode.place(x=310,y=420,width=120)
#==TheEnd====================================================================================================================================
mainwin.mainloop()