from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0


window = Tk()
window.title('Pomodoro Timer')
canvas = Canvas(width = 200, height =224, bg = YELLOW, highlightthickness = 0)

tomate = PhotoImage(file = 'tomato.png')
tick = PhotoImage(file = 'Green_tick.png')
canvas.create_image(100,112, image = tomate )
window.config(padx = 100, pady=50, bg = YELLOW)
timertext = canvas.create_text(103,135, text='00:00', fill = 'white', font = (FONT_NAME,30,'bold'))
canvas.grid(column=2, row=2)

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    countmin = math.floor(count/60)
    countsec = count%60

    if countsec ==0:
        countsec ='00'
    elif countsec >0 and countsec <10:
        countsec = f'0{countsec}'


    canvas.itemconfig(timertext, text = f'{countmin}:{countsec}')
    if count>0:
        window.after(20,countdown, count - 1)
    else:
        starter()


# ---------------------------- TIMER MECHANISM ------------------------------- #
#buttons


def starter():
    global rep
    rep+=1
    worksec = WORK_MIN*60
    sbsec = SHORT_BREAK_MIN*60
    lbsec = LONG_BREAK_MIN*60
    if rep %8 == 0:
        countdown(lbsec)
        label.configure(text='Break', fg = RED)
    elif rep%2== 0:
        countdown(sbsec)
        label.configure(text='Break', fg=PINK)
    else:
        countdown(worksec)
        label.configure(text='Work', fg=GREEN)
    return

def reseter():
    c = 1+2
    return



# ---------------------------- UI SETUP ------------------------------- #


#Title text
label = Label(text="Pomodoro\nTimer",fg = GREEN, bg= YELLOW, font = (FONT_NAME,30,'bold')  )
label.grid(column = 2 ,row = 1)





#ticks
ticks = Label(text='🍅', fg = GREEN, bg = YELLOW)
ticks.grid(column=2, row=3)

#buttons

start = Button(text="Start", command=starter)
start.grid(column = 1 ,row = 3)

reset = Button(text="Reset", command =reseter)
reset.grid(column = 3 ,row = 3)





window.mainloop()