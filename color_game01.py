from tkinter import *
from tkinter import messagebox
import random
#==Props=====================================================================================================================================
mainwin = Tk()
mainwin.geometry('550x550+400+80')
mainwin.config(bg= "#10153D")
mainwin.title('COLOR GAME™')
#==Functions=================================================================================================================================
colors = ['Black','Gray','White','Gold','Silver','Blue','Red','Green','Yellow',
          'Purple','Pink','Brown','Orange','Turquoise','Teal']

score = 0
timeleft = 30
first_round = True 
#____start_game______________________________________________________________________________________________________________________________
def startgame(event):
    global first_round, score
    if timeleft == 30:
        score = 0
        first_round = True
        countdown()
    nextcolor()
#____countdown_timer_________________________________________________________________________________________________________________________
def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo('Times Up!',f"Your Score: {score}")
        reset_game()
    if timeleft > 0:
        timeleft -= 1
        lbl_Timer.config(text="Timer:" + str(timeleft))
        lbl_Timer.after(1000, countdown)
#____Reset___________________________________________________________________________________________________________________________________
def reset_game():
    global timeleft, score, first_round
    timeleft = 30
    score = 0
    first_round = True
    lbl_Timer.config(text=f'Time Left: {timeleft}')
    lbl_color.config(text='')
    eg.delete(0, END)
#____nextcolor_______________________________________________________________________________________________________________________________
def nextcolor():
    global score, timeleft, first_round
    if timeleft > 0:
        if not first_round:  
            if eg.get().lower() == lbl_color.cget("fg").lower():
                score += 1
            else:
                score -= 1
        else:
            first_round = False

        eg.delete(0, END)
        random.shuffle(colors)
        lbl_color.config(fg=colors[1].lower(), text=colors[0])

mainwin.bind('<Return>',startgame)
#==widgets===================================================================================================================================
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
#__labels______________________++____________________________________________________________________________________________________________
lbl_text = Label(text= 'Welcome to the ',font= ("G2 Rubber Stamp LET",18,'bold'),bg= "#10153D",fg= '#FFFF00' )
lbl_text.place(x= 35,y= 15)

lbl_C = Label(text= 'C',font= ("Impact",24,'bold'),bg= "#10153D",fg= "#FF0000" )
lbl_C.place(x= 272,y= 5)

lbl_O = Label(text= 'O',font= ("Impact",24,'bold'),bg= "#10153D",fg= "#FFFF00" )
lbl_O.place(x= 296,y= 10)

lbl_L = Label(text= 'L',font= ("Impact",24,'bold'),bg= "#10153D",fg= "#00FF00" )
lbl_L.place(x= 318,y= 5)

lbl_O2 = Label(text= 'O',font= ("Impact",24,'bold'),bg= "#10153D",fg= '#FF9900' )
lbl_O2.place(x= 336,y= 10)

lbl_R = Label(text= 'R',font= ("Impact",24,'bold'),bg= "#10153D",fg= '#FF00FF' )
lbl_R.place(x= 358,y= 5)

lbl_G = Label(text= 'G',font= ("Impact",24,'bold'),bg= "#10153D",fg= "#FF0000" )
lbl_G.place(x= 393,y= 5)

lbl_A = Label(text= 'A',font= ("Impact",24,'bold'),bg= "#10153D",fg= "#FFFF00" )
lbl_A.place(x= 417,y= 10)

lbl_M = Label(text= 'M',font= ("Impact",24,'bold'),bg= "#10153D",fg= '#0000FF' )
lbl_M.place(x= 441,y= 5)

lbl_E = Label(text= 'E',font= ("Impact",26,'bold'),bg= "#10153D",fg= "#00FF00" )
lbl_E.place(x= 474,y= 10)

lbl_Guide = Label(text= "(Press 'Enter' To Play Game) ",font= ("G2 Rubber Stamp LET",12,'bold'),bg= "#10153D",fg= '#FF0000' )
lbl_Guide.place(x= 125,y= 56)

lbl_Timer = Label(text= "Timer: ",font= ("G2 Rubber Stamp LET",18,'bold'),bg= "#10153D",fg= '#FFFF00' )
lbl_Timer.place(x= 130,y= 85)

lbl_score = Label(text= 'Score: ',font= ("G2 Rubber Stamp LET", 18,'bold'),bg= '#10153D',fg= '#FFFF00')
lbl_score.place(x= 310,y= 85)

lbl_color = Label(mainwin,font= ('comic sans ms', 50,'bold'),bg= '#10153D')
lbl_color.place(x= 150,y= 180)
#__Entry_____________________________________________________________________________________________________________________________________
# Ent_Game = eg
eg = Entry(mainwin,font= ('Cascadia Mono SemiBold',14,'bold'),fg= "#10153D")
eg.place(x= 130 ,y= 360,width= 300)
#==TheEnd====================================================================================================================================
mainwin.mainloop()