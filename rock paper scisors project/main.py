from tkinter import *
import random

import PIL.Image
from PIL import Image,ImageTk


#the variables we need
global players_score,pc_score,draws1
players_score=0
pc_score=0
draws1=0
list = ["r", "p", "s"]

global state
state="disabled"






def random_pc_coice():
    pc=random.choice(list)
    return pc




def rock_pick():
    global players_score, pc_score, draws1
    pc = random.choice(list)
    r="r"
    if r == pc:
        label4.config(text="its a draw!", bg="gray")
        label6.config(text=f"draws {draws1+1}", bg="gray")
        draws1+=1
    elif pc == "p":
        label4.config(text="you lost this round!", bg="gray")
        label3.config(text=f"pc score {pc_score+1}", bg="gray")
        pc_score+=1
    else:
        label4.config(text="you won this round!", bg="gray")
        label2.config(text=f"players score {players_score+1}", bg="gray")
        players_score+=1






def paper_pick():
    global players_score, pc_score, draws1
    pc = random.choice(list)
    p = "p"
    if p == pc:
        label4.config(text="its a draw!", bg="gray")
        label6.config(text=f"draws {draws1 + 1}", bg="gray")
        draws1 += 1
    elif pc == "s":
        label4.config(text="you lost this round!", bg="gray")
        label3.config(text=f"pc score {pc_score + 1}", bg="gray")
        pc_score += 1
    else:
        label4.config(text="you won this round!", bg="gray")
        label2.config(text=f"players score {players_score + 1}", bg="gray")
        players_score += 1







def scisors_pick():
    global players_score, pc_score, draws1
    pc = random.choice(list)
    s = "s"
    if s == pc:
        label4.config(text="its a draw!", bg="gray")
        label6.config(text=f"draws {draws1 + 1}", bg="gray")
        draws1 += 1
    elif pc == "r":
        label4.config(text="you lost this round!", bg="gray")
        label3.config(text=f"pc score {pc_score + 1}", bg="gray")
        pc_score += 1
    else:
        label4.config(text="you won this round!", bg="gray")
        label2.config(text=f"players score {players_score + 1}", bg="gray")
        players_score += 1






#those functions are for the draw chance












def reset():
    d=0
    p=0
    pc=0
    label6.config(text=f"draws {d}", bg="gray")
    label3.config(text=f"pc score {pc}", bg="gray")
    label2.config(text=f"players score {p}", bg="gray")
    pass

def stop():
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    label4.config(text="if you are ready,press play")



def play():

    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    label4.config(text="you are playing!")




#this is were the window is generated along with the title
window = Tk()
window.resizable(False,False)
window["bg"] = "gray"
l = random_pc_coice()
#generated images
p_image = ImageTk.PhotoImage(Image.open("papper image.png").resize((80,80)))


r_image = ImageTk.PhotoImage(Image.open("rock image.png").resize((80,80)))


s_image = ImageTk.PhotoImage(Image.open("scissors image.png").resize((80,80)))

#title of window
window.title("rock paper scissors")

#here  is specified the size of the window

window.geometry("700x600")

#define the columns and the rows
window.columnconfigure((0,1,2,3,4,5),weight = 1)

window.rowconfigure((0,1,2,3,4,5,6,),weight = 1)
#here are the labels that we will use
label1=Label(window,text="lets play rock paper scissors!!",bg="gray")
label2=Label(window,text=f"players score {players_score}",bg="gray")
label3=Label(window,text=f"pc score {pc_score}",bg="gray")

label4=Label(window,text="if your ready,press play",bg="gray")
label5=Label(window,bg="gray")
label6=Label(window,text=f"draws {draws1}",bg="gray")

label1.grid(row=0,columnspan = 6,sticky = "nsew")
label2.grid(row=5,columnspan = 2)
label3.grid(row=5,column=4,columnspan = 2,)
label4.grid(row=2,column=1)
label5.grid(row=3,column=1)
label6.grid(row=5,column=2,columnspan=2)


#here are the buttons that we will use

button1=Button(window,text="Rock",command=(rock_pick),image=r_image,bg="gray",state="disabled")
button2=Button(window,text="Paper",command=(paper_pick),image=p_image,bg="gray",state="disabled")
button3=Button(window,text="Scissors",command=(scisors_pick),image=s_image,bg="gray",state="disabled")
button4=Button(window,text="play",command = (play),bg="gray",bd=0)
button5=Button(window,text="stop",bg="gray",command=(stop))
button6=Button(window,text="reset",command=(reset),bg="gray")



button1.grid(row=1,column = 0,columnspan=2)
button2.grid(row=1,column = 2,columnspan=2)
button3.grid(row=1,column = 4,columnspan=2)
button4.grid(row=4,column=0,columnspan=2)
button5.grid(row=4,column=2,columnspan=2)
button6.grid(row=4,column=4,columnspan=2)

#this is the infinite loop that keeps the window runing
window.mainloop()